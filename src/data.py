import urllib.request
from html.parser import HTMLParser
import re
from math import floor, ceil
from collections import defaultdict
from tqdm.auto import tqdm
import bs4 as bs

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.courselist = []
        self.datalist = []
    
    def handle_data(self, data):        
        p_course = re.compile('[EF][1-9]+')
        #single integer between 1 and 18
        p_integer = re.compile('^([1-9]|[0-9][0-8])$') 
        match = p_course.match(data)
        if match != None:
            #print("Mafound  course :", match.group())
            self.courselist.append(match.group())
        match = p_integer.match(data)
        if match != None:
            #print("found integer  :", match.group())
            self.datalist.append(int(match.group()) )

def result_dictionary(page_url):
    #print('Retrieveing: ',page_url)
    local_filename, headers = urllib.request.urlretrieve(page_url)
    html = open(local_filename)

    parser = MyHTMLParser()
    parser.feed(html.read())

    results = parser.datalist
    num_columns = floor(len(results) /18)
    round_tag = parser.courselist[:num_columns-1]
    results = results[:(num_columns)*18]
    
    lane_results = defaultdict(list)
    #print('Found results for',round_tag)
    
    for i,res in enumerate(results):
        c = i%num_columns
        l = ceil((i+1)/num_columns)
        if c>0:
            if round_tag[c-1][0] == 'F':
                lane_results['F'+str(l)].append(res)
            if round_tag[c-1][0] == 'E':
                lane_results['E'+str(l)].append(res)
    return lane_results

def player_url(player_id):
    url_base = 'https://minigolf-live.com/turnier1304a/'
    return url_base+str(player_id)+'.htm'

def printProgress(i, n):
    width = 30
    n_max = n-1
    n_progress = round(width*i/n_max)
    print('\r|{}{}| {}% '.format(  n_progress*'=',(width-n_progress)*' ',round(100*n_progress/width)),end='')
    if (i==n-1):
        print('| Done!')
    

def parse(player_id):
    DATA = dict()
    for i,el in enumerate(tqdm(player_id)):
        data = result_dictionary(player_url(player_id[el]))
        DATA[el] = data

    return DATA

class LaneData():
    def __init__(self, url):
        # setting up player ID's
        source=urllib.request.urlopen(url).read()
        soup=bs.BeautifulSoup(source,'html.parser')

        self.DATA = dict()
        self.player2id = dict()
        
        names = soup.find_all("td", {"class": "namn"})
        for namerow in names:
            player = namerow.find("a").text
            link = namerow.find("a").get("href")            
            self.player2id[player]= link[:-4]

        print('INIT DONE')

    def __getitem__(self, key):
        if key in self.DATA:
            return self.DATA[key]
        else:
            print('Retrieving data for ', key)
            self.DATA[key] = result_dictionary(player_url(self.player2id[key]))
        return self.DATA[key]


    
