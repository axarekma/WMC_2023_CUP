
from collections import Counter
import pandas as pd
import matplotlib as mpl
from matplotlib import gridspec
import matplotlib.colors as colors
import numpy as np
from game import Game
import matplotlib.pyplot as plt


def get_names(data):
    a = Counter([el[0] for el in data]).most_common(10)
    b = Counter([el[1] for el in data]).most_common(10)
    c = Counter([el[2] for el in data]).most_common(10)
    names = set([el[0] for el in a]).union(set([el[0] for el in b])).union(set([el[0] for el in c]))
    return names
    
def medalists(data):
    n_MC = len(data)
    rows = []
    for name in get_names(data):
        [el[0] for el in data].count('Beat Wartenweiler')
        rows.append({'Player':name, 
                     'Gold':np.round([el[0] for el in data].count(name)*100/n_MC).astype(int),
                     'Silver':np.round([el[1] for el in data].count(name)*100/n_MC).astype(int),
                     'Bronze':np.round([el[2] for el in data].count(name)*100/n_MC).astype(int),                
                    })
    df = pd.DataFrame(rows).sort_values(by=['Gold'],ascending = False)

    return df



def getL(res):
    L = 0
    for p in res:
        L = max(L,p[0])
        L = max(L,p[1])
    return L+1


def plotGame(player1,player2,key,data,lanes, n_max):
    def wGame(p1,p2,k,MC = True):
        return Game(p1,p2,k,data,lanes,MC)

    def gen_Game(player1,player2,key,n_max, MC = True):
        for n in range(n_max):
            yield wGame(player1,player2,key, MC = MC)  
            
    res = [el.score for el in gen_Game(player1,player2,key,n_max,MC = True) ]
    res_b = [el[0]>el[1] for el in res ]
    L = getL(res)
    counter = np.zeros((L,L))
    for p in res:
        counter[p[0],p[1]] = counter[p[0],p[1]] + 1


    fig = plt.figure(figsize=(5, 5))
    gs = gridspec.GridSpec(1, 2, width_ratios=[13, 1])
    ax = fig.add_axes([0.1, 0.1, 0.7, 0.7])  
    img1 = ax.imshow(counter,origin='lower')
    plt.ylabel('{} {:.3} %'.format(player1,100*np.sum(res_b)/len(res) ))
    plt.xlabel('{} {:.3} %'.format(player2,100*(len(res_b)-np.sum(res_b))/len(res)))

    # Make a figure and axes with dimensions as desired.
    cNorm2  = colors.Normalize(vmin=0, vmax=np.max(counter) )
    #ax1 = fig.add_subplot(gs[1])
    ax2 = fig.add_axes([0.85, 0.1, 0.05, 0.7])   
    viridis = cm = plt.get_cmap('viridis') 
    cb1 = mpl.colorbar.ColorbarBase(ax2, cmap=viridis,
                                    norm=cNorm2,
                                    orientation='vertical')

    cb1.set_label('Realizations')
    f_name = player1+'_'+player2+'_'+key
    plt.savefig('../FIG/'+format(f_name.lower().replace(" ", "_")))
    