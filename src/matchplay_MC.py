from game import Game
import numpy as np
import matplotlib.pyplot as plt

class MC_Game():
    def __init__(self, player1,player2, lane, data, lanes, n_iter):
            self.player1 = player1
            self.player2 = player2

            res = [Game(player1,player2, lane, data, lanes,MC = True).score for el in range(n_iter) ]
            winner1 = [el[0]>el[1] for el in res ]   
            winner2 = [el[0]<el[1] for el in res ]
            if np.sum(winner2)>np.sum(winner1):
                self.winner = player2
                self.loser = player1
                self.percentage = np.sum(winner2)/n_iter
            else:
                self.winner = player1
                self.loser = player2
                self.percentage = np.sum(winner1)/n_iter 

class Cup_16:
    def __init__(self,rank,data,lanesA,lanesB, mc_iter = 100):
        self.data = data
        self.lanes = lanesA+lanesB
        self.mc_iter = mc_iter

        # helper lists for easier indexing (starting lanes from invitation)
        A = ['']+lanesA
        B = ['']+lanesB


        self.games = dict()
        self.games['G1'] = self.game(rank[1],rank[16],A[2])
        self.games['G2'] = self.game(rank[8],rank[9],A[3])
        self.games['G3'] = self.game(rank[5],rank[12],A[4])
        self.games['G4'] = self.game(rank[4],rank[13],A[5])
        self.games['G5'] = self.game(rank[3],rank[14],A[6])
        self.games['G6'] = self.game(rank[6],rank[11],A[7])
        self.games['G7'] = self.game(rank[7],rank[10],A[8])
        self.games['G8'] = self.game(rank[2],rank[15],A[9])
        #bo8
        self.games['G9'] = self.game(self.games['G1'].winner ,
                                self.games['G2'].winner,A[1])
        self.games['G10'] = self.game(self.games['G3'].winner ,
                                 self.games['G4'].winner,A[3])
        self.games['G11'] = self.game(self.games['G5'].winner ,
                                 self.games['G6'].winner,A[5])
        self.games['G12'] = self.game(self.games['G7'].winner ,
                                 self.games['G8'].winner,A[7])
        #bo4
        self.games['S1'] = self.game(self.games['G9'].winner ,
                                self.games['G10'].winner,B[1])
        self.games['S2'] = self.game(self.games['G11'].winner ,
                                self.games['G12'].winner,B[1])
        #bronze
        self.games['Bronze'] = self.game(self.games['S1'].loser ,
                                    self.games['S2'].loser,B[1])
        #bronze
        self.games['Final'] = self.game(self.games['S1'].winner ,
                                    self.games['S2'].winner,B[1])
        
    @property
    def winner(self):
        return self.games['Final'].winner
                
    @property
    def medals(self):
        return (self.games['Final'].winner,
               self.games['Final'].loser,
               self.games['Bronze'].winner)
    def game(self,player1,player2,lane,MC = True):
        return MC_Game(player1,player2, lane, self.data, self.lanes, self.mc_iter)
    
    def plot(self):
        import matplotlib as mpl
        import matplotlib.cm as cm
        norm = mpl.colors.Normalize(vmin=0.5, vmax=1)
        cmap = cm.viridis
        m = cm.ScalarMappable(norm=norm, cmap=cmap)


        fig, ax = plt.subplots(figsize = (13,5))

        games = [self.games[f'G{n}'] for n in range(1,9)]
        for i,game in enumerate(games):
            textstr = f'{game.player1}\n{game.player2}'
            props = dict(boxstyle='round', facecolor=m.to_rgba(game.percentage), alpha=0.5)
            ax.text(0, 16-2*i, textstr,  fontsize=10,
            verticalalignment='center', bbox=props)

        games = [self.games[f'G{n}'] for n in range(9,13)]
        for i,game in enumerate(games):
            textstr = f'{game.player1}\n{game.player2}'
            props = dict(boxstyle='round', facecolor=m.to_rgba(game.percentage), alpha=0.5)
            ax.text(10, 15-4*i, textstr,  fontsize=10,
            verticalalignment='center', bbox=props)

        games = [self.games[f'S1'] ,self.games[f'S2'] ]
        for i,game in enumerate(games):
            textstr = f'{game.player1}\n{game.player2}'
            props = dict(boxstyle='round', facecolor=m.to_rgba(game.percentage), alpha=0.5)
            ax.text(20, 13-8*i, textstr,  fontsize=10,
            verticalalignment='center', bbox=props)

        games = [self.games[f'Final'] ,self.games[f'Bronze'] ]
        for i,game in enumerate(games):
            textstr = f'{game.player1}\n{game.player2}'
            props = dict(boxstyle='round', facecolor=m.to_rgba(game.percentage), alpha=0.5)
            ax.text(30, 9-8*i, textstr,  fontsize=10,
            verticalalignment='center', bbox=props)

    
        textstr = f"== FINAL ==\nI:  {self.games['Final'].winner}\nII: {self.games['Final'].loser}\nIII:{self.games['Bronze'].winner}"
        props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
        ax.text(34,15, textstr,  fontsize=10,
        verticalalignment='center', bbox=props)



        props = dict(boxstyle='round', facecolor='white', alpha=0.5)
        ax.text(0, -1, 'Probability:',  fontsize=10,
            verticalalignment='center', bbox=props)
        for i,val in enumerate([0.5,0.6,0.7,0.8,0.9,1.0]):
            props = dict(boxstyle='round', facecolor=m.to_rgba(val), alpha=0.5)
            ax.text(5+2*i, -1, val,  fontsize=10,
            verticalalignment='center', bbox=props)    
        ax.set(title='Womens Cup',
           aspect=1, xlim=(0, 40), ylim=(0, 18))
        
        ax.set_axis_off()



class Cup_32:
    def __init__(self,rank,data,lanesA,lanesB, mc_iter = 100):
        self.data = data
        self.lanes = lanesA+lanesB
        self.mc_iter = mc_iter

        # helper lists for easier indexing (starting lanes from invitation)
        A = ['']+lanesA
        B = ['']+lanesB

        self.games = dict()
        self.games['G1'] = self.game(rank[1],rank[32],A[2])
        self.games['G2'] = self.game(rank[16],rank[17],A[3])
        self.games['G3'] = self.game(rank[9],rank[24],A[4])
        self.games['G4'] = self.game(rank[8],rank[25],A[5])
        self.games['G5'] = self.game(rank[5],rank[28],A[6])
        self.games['G6'] = self.game(rank[12],rank[21],A[7])
        self.games['G7'] = self.game(rank[13],rank[20],A[8])
        self.games['G8'] = self.game(rank[4],rank[29],A[9])

        self.games['G9'] = self.game(rank[3],rank[30],B[1])
        self.games['G10'] = self.game(rank[14],rank[19],B[2])
        self.games['G11'] = self.game(rank[11],rank[22],B[3])
        self.games['G12'] = self.game(rank[6],rank[27],B[4])
        self.games['G13'] = self.game(rank[7],rank[26],B[5])
        self.games['G14'] = self.game(rank[10],rank[23],B[6])
        self.games['G15'] = self.game(rank[15],rank[18],B[7])
        self.games['G16'] = self.game(rank[2],rank[31],B[8])
        #bo8
        self.games['G17'] = self.game(self.games['G1'].winner ,
                                 self.games['G2'].winner,B[1])
        self.games['G18'] = self.game(self.games['G3'].winner ,
                                 self.games['G4'].winner,B[2])
        self.games['G19'] = self.game(self.games['G5'].winner ,
                                 self.games['G6'].winner,B[3])
        self.games['G20'] = self.game(self.games['G7'].winner ,
                                 self.games['G8'].winner,B[4])
        self.games['G21'] = self.game(self.games['G9'].winner ,
                                 self.games['G10'].winner,B[5])
        self.games['G22'] = self.game(self.games['G11'].winner ,
                                 self.games['G12'].winner,B[6])
        self.games['G23'] = self.game(self.games['G13'].winner ,
                                 self.games['G14'].winner,B[7])
        self.games['G24'] = self.game(self.games['G15'].winner ,
                                 self.games['G16'].winner,B[8])
        #bo8
        self.games['G25'] = self.game(self.games['G17'].winner ,
                                 self.games['G18'].winner,B[1])
        self.games['G26'] = self.game(self.games['G19'].winner ,
                                 self.games['G20'].winner,B[3])
        self.games['G27'] = self.game(self.games['G21'].winner ,
                                 self.games['G22'].winner,B[5])
        self.games['G28'] = self.game(self.games['G23'].winner ,
                                 self.games['G24'].winner,B[7])
        
        #bo4
        self.games['S1'] = self.game(self.games['G25'].winner ,
                                self.games['G26'].winner,B[1])
        self.games['S2'] = self.game(self.games['G27'].winner ,
                                self.games['G28'].winner,B[1])
        #bronze
        self.games['Bronze'] = self.game(self.games['S1'].loser ,
                                    self.games['S2'].loser,B[1])
        #bronze
        self.games['Final'] = self.game(self.games['S1'].winner ,
                                    self.games['S2'].winner,B[1])
                
    @property
    def winner(self):
        return self.games['Final'].winner
                
    @property
    def medals(self):
        return (self.games['Final'].winner,
               self.games['Final'].loser,
               self.games['Bronze'].winner)
    def game(self,player1,player2,lane,MC = True):
        return MC_Game(player1,player2, lane, self.data, self.lanes, self.mc_iter)
    
    def plot(self):
        fs = 8
        import matplotlib as mpl
        import matplotlib.cm as cm
        norm = mpl.colors.Normalize(vmin=0.5, vmax=1)
        cmap = cm.viridis
        m = cm.ScalarMappable(norm=norm, cmap=cmap)


        fig, ax = plt.subplots(figsize = (13,8))

        games = [self.games[f'G{n}'] for n in range(1,17)]
        for i,game in enumerate(games):
            textstr = f'{game.player1}\n{game.player2}'
            props = dict(boxstyle='round', facecolor=m.to_rgba(game.percentage), alpha=0.5)
            ax.text(0, 32-2*i, textstr,  fontsize=fs,
            verticalalignment='center', bbox=props)

        games = [self.games[f'G{n}'] for n in range(17,25)]
        for i,game in enumerate(games):
            textstr = f'{game.player1}\n{game.player2}'
            props = dict(boxstyle='round', facecolor=m.to_rgba(game.percentage), alpha=0.5)
            ax.text(10, 31-4*i, textstr,  fontsize=fs,
            verticalalignment='center', bbox=props)

        games = [self.games[f'G{n}'] for n in range(25,29)]
        for i,game in enumerate(games):
            textstr = f'{game.player1}\n{game.player2}'
            props = dict(boxstyle='round', facecolor=m.to_rgba(game.percentage), alpha=0.5)
            ax.text(20, 29-8*i, textstr,  fontsize=fs,
            verticalalignment='center', bbox=props)

        games = [self.games[f'S1'] ,self.games[f'S2'] ]
        for i,game in enumerate(games):
            textstr = f'{game.player1}\n{game.player2}'
            props = dict(boxstyle='round', facecolor=m.to_rgba(game.percentage), alpha=0.5)
            ax.text(30, 25-16*i, textstr,  fontsize=10,
            verticalalignment='center', bbox=props)

        games = [self.games[f'Final'] ,self.games[f'Bronze'] ]
        for i,game in enumerate(games):
            textstr = f'{game.player1}\n{game.player2}'
            props = dict(boxstyle='round', facecolor=m.to_rgba(game.percentage), alpha=0.5)
            ax.text(40, 16-8*i, textstr,  fontsize=10,
            verticalalignment='center', bbox=props)

    
        textstr = f"== FINAL ==\nI:  {self.games['Final'].winner}\nII: {self.games['Final'].loser}\nIII:{self.games['Bronze'].winner}"
        props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)
        ax.text(42,30, textstr,  fontsize=10,
        verticalalignment='center', bbox=props)



        props = dict(boxstyle='round', facecolor='white', alpha=0.5)
        ax.text(0, -1, 'Probability:',  fontsize=10,
            verticalalignment='center', bbox=props)
        for i,val in enumerate([0.5,0.6,0.7,0.8,0.9,1.0]):
            props = dict(boxstyle='round', facecolor=m.to_rgba(val), alpha=0.5)
            ax.text(5+2*i, -1, val,  fontsize=10,
            verticalalignment='center', bbox=props)    
        ax.set(title='Mens Cup',
           aspect=1, xlim=(0, 50), ylim=(0, 34))
        
        ax.set_axis_off()


    
