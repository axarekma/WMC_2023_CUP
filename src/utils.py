
from collections import Counter
import pandas as pd
import numpy as np



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