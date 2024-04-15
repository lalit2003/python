import random

board=["-","-","-",
       "-","-","-",
       "-","-","-"]
currentplayer="X"
winner=None
gamerunning=True

#printing the game board..
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


#Taking palyer Input..
def playerInput(board):
    inp=int(input("Enter a number from 1-9:-"))
    if inp >=1 and inp <=9 and board[inp-1] == "-":
        board[inp-1]=currentplayer
    else:
        print("Oops player is already in that spot!..")
    
#Check for win or Tie..
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] !="-":
        winner=board[0]
        return True
    
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner=board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] !="-":
        winner=board[6]
        return True


def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] !="-":
        winner=board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] !="-":
        winner=board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] !="-":
        winner=board[2]
        return True


def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] !="-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    global gamerunning
    if "-" not in board:
        printBoard(board)
        print("It is a TIE !..")
        gamerunning=False


def checkWin():
    global gamerunning
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is {winner}")    
        gamerunning=False
        
# switch player

def switchPlayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer="O"
    else:
        currentplayer="X" 

#computer

def computer(board):
    while currentplayer =="O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

#check for win or tie again..

while gamerunning:
   printBoard(board)
   playerInput(board)
   checkWin()
   checkTie(board)
   switchPlayer()
   computer(board)
   checkWin()
   checkTie(board)





