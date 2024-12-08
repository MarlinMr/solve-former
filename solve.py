import random
import sys
import time
from copy import deepcopy
game={}
items=["K","O","N","D"]
gameWidth=7
gameHeight=9
pathsFile="results_8_test"
nTakenFile="ntaken_8_test"
low=19
high=0
limit=63
tested=0
downLevel=int(sys.argv[1])
topLevel=int(sys.argv[2])
checker=int(sys.argv[3])

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
movesTaken=[]

def testGame(game,movesTaken,low,tested,nTaken,high):
    currentGame=deepcopy(game)
    localMoves=[]
    checkingGame=deepcopy(game)
    for i in range(1,gameWidth+1):
        for j in range(1,gameHeight+1):
            if checkingGame[j][i] in items:
                localMoves.append([i,j])
                localChecked=[]
                equal=[]
                checkGame(checkingGame,i,j,checkingGame[j][i],localChecked,equal)
                for a in equal:
                    checkingGame[a[1]][a[0]]="X"
    if len(localMoves)==0:
        if low>=len(movesTaken):
            low=len(movesTaken)
            with open(pathsFile, "a") as f:
                result=f"\nDONE! Found {len(movesTaken)} after {tested} branches. nTaken {nTaken}. DownLevel {downLevel}, TopLevel {topLevel}. {movesTaken}"
                f.write(result)
        return(low,tested,high)
    if len(movesTaken)>=topLevel:
        random.shuffle(localMoves)
    for move in localMoves:
        #print(f"\nTesting: {tested}, nTaken: {nTaken}, low: {low}, high: {high}, lowLevel: {downLevel}, topLevel: {topLevel}, {len(movesTaken)} movesTaken: {movesTaken}", end="")
        movesTaken.append(move)
        if ((tested % downLevel) == 0) and (len(movesTaken)>topLevel):
            movesTaken.pop()
            break
        tested=tested+1
        if len(movesTaken)>low:
            print(f"\nBreaking: {tested}, nTaken: {nTaken}, low: {low}, high: {high}, lowLevel: {downLevel}, topLevel: {topLevel}, {len(movesTaken)} movesTaken: {movesTaken}", end="")
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
        nTaken=nTaken+len(remove)
        if len(movesTaken)<=checker and nTaken >= high:
            with open(nTakenFile, "a") as f:
                result=f"\n{nTaken} {movesTaken}"
                f.write(result)
            high=nTaken
        for ii in range(gameHeight):
            for i in range(1,gameHeight+1):
                for j in range(1,gameWidth+1):
                    if nextGame[i-1][j]=="X":
                        nextGame[i-1][j]=nextGame[i][j]
                        nextGame[i][j]="X"
        low,tested,high=testGame(nextGame,movesTaken,low,tested,nTaken,high)
        nTaken=nTaken-len(remove)
        movesTaken.pop()
    #print(f"Status: {tested}, nTaken: {nTaken}, low: {low}, high: {high}, lowLevel: {downLevel}, topLevel: {topLevel}, {len(movesTaken)} movesTaken: {movesTaken}")
    return(low,tested,high)

try:
    with open("global_low", "r") as f:
        k=int(f.read())
        if low>k:
            low=k
except Exception as e:
    pass
nTaken=0
while True:
    low,tested,high=testGame(game,movesTaken,low,tested,nTaken,high)
#low,tested,high=testGame(game,movesTaken,low,tested,nTaken,high)
#print(f"Ended: {tested}, nTaken: {nTaken}, low: {low}, high: {high}, lowLevel: {downLevel}, topLevel: {topLevel}, {len(movesTaken)} movesTaken: {movesTaken}")
    #with open("nTakenFile", "a") as f:
    #    result=f"\nEnded: {tested}, nTaken: {nTaken}, low: {low}, high: {high}, lowLevel: {downLevel}, topLevel: {topLevel}, {len(movesTaken)} movesTaken: {movesTaken}"
    #    f.write(result)
