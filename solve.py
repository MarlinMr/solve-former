import random
from colorama import Fore, Back, Style
game={}
e="K"
remove=[]
checked=[]
legalMoves=[]
movesTaken=[]
items=["K","O","N","D"]
gameWidth=7
gameHeight=9
low=gameWidth*gameHeight
tested=0

def printGame():
    for i in range(gameHeight+2):
        for j in range(gameWidth+2):
            if [j,i] in remove:
                print(Fore.RED + game[i][j], end="")
                print(Style.RESET_ALL, end="")
            else:
                print(game[i][j], end="")
        print()

def makeGame(game):
    for i in range(gameHeight+2):
        game[i]={}
        for j in range(gameWidth+2):
            if (((i==0) or (i==gameHeight+1))or((j==0)or(j==gameWidth+1))):
                game[i][j]="."
            else:
                legalMoves.append([j,i])
                game[i][j]=random.choice(items)
    print(game)
    print(legalMoves)
    printGame()

def checkGame(game,x,y):
    current=game[y][x]
    checked.append([x,y])
    if game[y-1][x]==e:
        if ([x,y-1] not in remove):
            #print("1:append",[x,y-1],game[y-1][x])
            remove.append([x,y-1])
        if ([x,y-1] not in checked):
            checkGame(game,x,y-1)
    if game[y+1][x]==e:
        if ([x,y+1] not in remove):
            #print("2:append",[x,y+1],game[y+1][x])
            remove.append([x,y+1])
        if ([x,y+1] not in checked):
            checkGame(game,x,y+1)
    if game[y][x-1]==e:
        if ([x-1,y] not in remove):
            #print("3:append",[x-1,y],game[y][x-1])
            remove.append([x-1,y])
        if ([x-1,y] not in checked):
            checkGame(game,x-1,y)
    if game[y][x+1]==e:
        if ([x+1,y] not in remove):
            #print("append",[x+1,y],game[y][x+1])
            remove.append([x+1,y])
        if ([x+1,y] not in checked):
            checkGame(game,x+1,y)

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

def calcTurn():
    remove.clear()
    x=selVal("x: ",gameWidth)
    y=selVal("y: ",gameHeight)
    move=[y,x]
    #move=random.choice(legalMoves)
    #x=move[0]
    #y=move[1]
    movesTaken.append(move)
    remove.append([x,y])
    e=game[y][x]
    checkGame(game,x,y)
    printGame()
    for a in remove:
        game[a[1]][a[0]]=" "
    remove.clear()
    for ii in range(gameHeight):
        for i in range(1,gameHeight+1):
            for j in range(1,gameWidth+1):
                if game[i-1][j]==" ":
                    game[i-1][j]=game[i][j]
                    game[i][j]=" "
    for a in legalMoves:
        if game[a[1]][a[0]] == " ":
            legalMoves.remove(a)

while True:
    #makeGame(game)
    tested=tested+1
    movesTaken.clear()
    game={0: 
       {0: '.', 1: '.', 2: '.', 3: '.', 4: '.', 5: '.', 6: '.', 7: '.', 8: '.'},
    1: {0: '.', 1: 'K', 2: 'O', 3: 'K', 4: 'O', 5: 'N', 6: 'N', 7: 'D', 8: '.'},
    2: {0: '.', 1: 'D', 2: 'D', 3: 'K', 4: 'K', 5: 'K', 6: 'N', 7: 'D', 8: '.'},
    3: {0: '.', 1: 'N', 2: 'D', 3: 'D', 4: 'O', 5: 'O', 6: 'D', 7: 'D', 8: '.'},
    4: {0: '.', 1: 'D', 2: 'D', 3: 'N', 4: 'O', 5: 'O', 6: 'K', 7: 'D', 8: '.'},
    5: {0: '.', 1: 'K', 2: 'N', 3: 'D', 4: 'D', 5: 'N', 6: 'O', 7: 'N', 8: '.'},
    6: {0: '.', 1: 'D', 2: 'K', 3: 'D', 4: 'O', 5: 'D', 6: 'O', 7: 'O', 8: '.'},
    7: {0: '.', 1: 'D', 2: 'K', 3: 'D', 4: 'D', 5: 'K', 6: 'K', 7: 'O', 8: '.'},
    8: {0: '.', 1: 'N', 2: 'D', 3: 'D', 4: 'O', 5: 'N', 6: 'D', 7: 'D', 8: '.'},
    9: {0: '.', 1: 'K', 2: 'O', 3: 'O', 4: 'K', 5: 'O', 6: 'N', 7: 'O', 8: '.'},
    10:{0: '.', 1: '.', 2: '.', 3: '.', 4: '.', 5: '.', 6: '.', 7: '.', 8: '.'}}
    legalMoves=[[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9]]
    while len(movesTaken)<low and len(legalMoves)>0:
        printGame()
        calcTurn()
    print("Number of moves: ", len(movesTaken))
    if len(movesTaken)<low:
        low=len(movesTaken)
    print("Lowest: ", low)
    print("Tested :", tested)
    print(movesTaken)
