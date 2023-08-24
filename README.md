# WMC_2023_CUP

## Monte carlo simulations of the cup finals
Axel Ekman

For earlier introduction, please refer to The analysis of [WMC 2017](https://github.com/axarekma/WMC_2017_CUP)


Disclamer:
- I parsed the standings after the intermediate rounds. Tiebrakers may be wrong. 
- Player data for the simulation includes final round.

Shown here are MC siumulations of the brackets and the probability of the winner.

## Most Common Medalists
The most common medalists is counted from 10000 realizations of a MC bracket. Numbers shown are normalized to 100. 

I.e., if we were to rerun the bracket 100 times, Melanie is expected to win 32 times, and be on the podium a total of 67 times.

#### Womens CUP
| Player                |   Gold |   Silver |   Bronze |
|:----------------------|-------:|---------:|---------:|
| Melanie Hammerschmidt |     32 |       25 |       10 |
| Anna Bandera          |     20 |       12 |       14 |
| Stefanie Blendermann  |     17 |       13 |       20 |
| Michaela Krane        |     10 |       10 |       12 |
| Sandra Kungsman       |      6 |        8 |       10 |
| Karin Olsson          |      4 |        7 |        3 |
| Jasmin Bothmann       |      4 |        7 |        9 |
| Lara Jehle            |      3 |        7 |        8 |
| Michaela Irxenmayer   |      2 |        5 |        5 |
| Julia Sjöberg         |      1 |        3 |        1 |
| Carolin Svensson      |      0 |        1 |        2 |

#### Mens Cup
| Player            |   Gold |   Silver |   Bronze |
|:------------------|-------:|---------:|---------:|
| Carl-Johan Ryner  |     23 |       17 |        8 |
| Ulf Kristiansson  |     19 |       12 |       12 |
| Eirik Seljelid    |     11 |       10 |       13 |
| Fredrik Persson   |     11 |       10 |        5 |
| Lukas Neumann     |     10 |        7 |        8 |
| Ondřej Škaloud    |      9 |        8 |       12 |
| Yannick Müller    |      7 |        9 |       12 |
| Beat Wartenweiler |      3 |        5 |        6 |
| Paolo Porta       |      1 |        2 |        2 |
| Sebastian Piekorz |      1 |        2 |        3 |
| Zdenek Majkus     |      1 |        2 |        3 |
| Sebastian Heine   |      1 |        2 |        1 |

## Bracket with match probabilities
Here each match is played 10000 times. The Color of the box indicates the probability of the winner.

![png](FIG/matchplay_W_lanes.png)

![png](FIG/matchplay_M_lanes.png)
