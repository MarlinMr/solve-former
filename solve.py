import random
import sys
import time
from copy import deepcopy
from colorama import Fore, Back, Style
game={}
items=["K","O","N","D"]
gameWidth=7
gameHeight=9
low=63
limit=63
tested=0
downLevel=int(sys.argv[1])
topLevel=int(sys.argv[2])

def printGame(currentGame):
    for i in reversed(range(gameHeight+2)):
        for j in range(gameWidth+2):
            print(currentGame[i][j], end="")
        print()

def checkGame(game,x,y,e,checked,remove):
    checked.append([x,y])
    if game[y+1][x]==e:
        if ([x,y+1] not in remove):
            remove.append([x,y+1])
        if ([x,y+1] not in checked):
            checkGame(game,x,y+1,e,checked,remove)
    if game[y-1][x]==e:
        if ([x,y-1] not in remove):
            remove.append([x,y-1])
        if ([x,y-1] not in checked):
            checkGame(game,x,y-1,e,checked,remove)
    if game[y][x+1]==e:
        if ([x+1,y] not in remove):
            remove.append([x+1,y])
        if ([x+1,y] not in checked):
            checkGame(game,x+1,y,e,checked,remove)
    if game[y][x-1]==e:
        if ([x-1,y] not in remove):
            remove.append([x-1,y])
        if ([x-1,y] not in checked):
            checkGame(game,x-1,y,e,checked,remove)

def selVal(text,lim):
    v=input(text)
    if v=="q":
        exit()
    if v.isnumeric():
        v=int(v)
        if v in range(1,lim+1):
            return v
        else:
            pass
    else:
        pass

game={
    10:{0: ' ', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''},
    9: {0: '9 ', 1: 'D', 2: 'O', 3: 'D', 4: 'N', 5: 'O', 6: 'K', 7: 'K', 8: ''},
    8: {0: '8 ', 1: 'D', 2: 'N', 3: 'D', 4: 'K', 5: 'D', 6: 'O', 7: 'N', 8: ''},
    7: {0: '7 ', 1: 'N', 2: 'O', 3: 'D', 4: 'O', 5: 'O', 6: 'N', 7: 'K', 8: ''},
    6: {0: '6 ', 1: 'K', 2: 'K', 3: 'D', 4: 'D', 5: 'K', 6: 'O', 7: 'D', 8: ''},
    5: {0: '5 ', 1: 'D', 2: 'N', 3: 'D', 4: 'K', 5: 'O', 6: 'N', 7: 'D', 8: ''},
    4: {0: '4 ', 1: 'K', 2: 'D', 3: 'K', 4: 'N', 5: 'D', 6: 'O', 7: 'N', 8: ''},
    3: {0: '3 ', 1: 'K', 2: 'N', 3: 'O', 4: 'O', 5: 'N', 6: 'D', 7: 'K', 8: ''},
    2: {0: '2 ', 1: 'N', 2: 'K', 3: 'O', 4: 'O', 5: 'O', 6: 'K', 7: 'K', 8: ''},
    1: {0: '1 ', 1: 'K', 2: 'N', 3: 'O', 4: 'O', 5: 'D', 6: 'K', 7: 'D', 8: ''},
    0: {0: '  ', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: ''}}
#game={
#    5:{0: ' ', 1: '', 2: '', 3: '', 4: '', 5: ''},
#    4: {0: '4 ', 1: 'D', 2: 'K', 3: 'N', 4: 'K', 5: ''},
#    3: {0: '3 ', 1: 'O', 2: 'N', 3: 'O', 4: 'D', 5: ''},
#    2: {0: '2 ', 1: 'K', 2: 'D', 3: 'K', 4: 'N', 5: ''},
#    1: {0: '1 ', 1: 'N', 2: 'D', 3: 'O', 4: 'O', 5: ''},
#    0: {0: '  ', 1: '1', 2: '2', 3: '3', 4: '4', 5: ''}}
#legalMoves=[[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9]]
movesTaken=[]

def testGame(game,movesTaken,low,tested):
    currentGame=deepcopy(game)
    localMoves=[]
    for i in range(1,gameWidth+1):
        for j in range(1,gameHeight+1):
            if currentGame[j][i] in items:
                localMoves.append([i,j])
    if len(localMoves)==0:
        print(f"DONE! Found {len(movesTaken)} after {tested} branches. {movesTaken}")
        if low>len(movesTaken):
            low=len(movesTaken)
        return(low,tested)
    #print(f"{len(localMoves)} localMoves: {localMoves}")
    #nMoves=nMoves*len(localMoves)
    if len(movesTaken)>=topLevel:
        random.shuffle(localMoves)
    for move in localMoves:
        #print(f"Breaking: {tested} low: {low}, {len(movesTaken)} movesTaken: {movesTaken}")
        movesTaken.append(move)
        if ((tested % downLevel) == 0) and (len(movesTaken)>topLevel):
            movesTaken.pop()
            #print(f"Breaking: {tested} low: {low}, {len(movesTaken)} movesTaken: {movesTaken}")
            break
        tested=tested+1
        if len(movesTaken)>=low:
            print(f"Continue: {tested} low: {low}, {len(movesTaken)} movesTaken: {movesTaken}")
            movesTaken.pop()
            break
        nextGame=deepcopy(currentGame)
        e=nextGame[move[1]][move[0]]
        checked=[]
        remove=[]
        remove.append(move)
        checkGame(nextGame,move[0],move[1],e,checked,remove)
        for a in remove:
            nextGame[a[1]][a[0]]="X"
        for ii in range(gameHeight):
            for i in range(1,gameHeight+1):
                for j in range(1,gameWidth+1):
                    if nextGame[i-1][j]=="X":
                        nextGame[i-1][j]=nextGame[i][j]
                        nextGame[i][j]="X"
        low,tested=testGame(nextGame,movesTaken,low,tested)
        movesTaken.pop()
    #print(f"Tested: {tested} low: {low}, {len(movesTaken)} movesTaken: {movesTaken}")
    return(low,tested)

try:
    with open("global_low", "r") as f:
        k=int(f.read())
        if low>k:
            low=k
except Exception as e:
    pass
nMoves=1
while True:
    low,tested=testGame(game,movesTaken,low,tested)
