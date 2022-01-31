from random import randint

from numpy import greater, random

alphaConvert = {'A': 0, 'B':1, 'C':2,'D':3,'E':4,"F":5,'G':6,'H':7, 'I':8, "J":9}


def main():
    hidden_board = [["🟦"] * 10 for x in range(10)]
    guess_board = [["🟦"] * 10 for x in range(10)]

    hidden_board = createShips(hidden_board)


    print("Welcome to Battleship!\n")
    while True:
        showBoard(guess_board)
        row, column = getShotLocation()
        if guess_board[row][column] == "💦":
            print("You already guessed that spot!")
        elif hidden_board[row][column] == "💥":
            print("Congradulations! You hit!")
            guess_board[row][column] = "💥"
        else:
            print("Sorry, you missed!")
            guess_board[row][column] = "💦"
        if hitShips(guess_board) == 5:
            print("You hit them all, good job!")
            break


def showBoard(board):
    print("   A  B  C  D  E  F  G  H  I  J")
    print("  ------------------------------")

    rownumb = 1
    for r in board:
        if rownumb == 10:
            space = ""
        else:
            space = " "
        print("%d|%s|" % (rownumb, space + "|".join(r)))
        rownumb += 1
    

def createShips(hiddenBoard):
    for ship in range(5):
        ori = randint(0,3)
        shipRow = randint(1,8)
        shipColumn = randint(1,8)
        if hiddenBoard[shipRow][shipColumn] != "💥":

            if ori == 0:
                hiddenBoard[shipRow][shipColumn] = "💥"
                hiddenBoard[shipRow - 1][shipColumn] = "💥"
            if ori == 1:
                hiddenBoard[shipRow][shipColumn] = "💥"
                hiddenBoard[shipRow][shipColumn + 1] = "💥"
            if ori == 2:
                hiddenBoard[shipRow][shipColumn] = "💥"
                hiddenBoard[shipRow + 1][shipColumn] = "💥"
            if ori == 3:
                hiddenBoard[shipRow][shipColumn] = "💥"
                hiddenBoard[shipRow][shipColumn - 1] = "💥"

            shipRow = randint(1,8)
            shipColumn = randint(1,8)
            ori = randint(0,3)
        else:
            shipRow = randint(1,8)
            shipColumn = randint(1,8)
            ori = randint(0,3)
    showBoard(hiddenBoard)
    return hiddenBoard

def getShotLocation():
    hitcoord = list(input("Please input hit coordinates (ex. A1): "))
    while True:
        if len(hitcoord) == 2 or len(hitcoord) == 3 and hitcoord[0] in "ABCDEFGHIJabcdefghij" and hitcoord[1] in "1234567890":
            column = hitcoord[0].upper()
            if len(hitcoord) == 2:    
                row = hitcoord[1]
            else:
                row = int(str(hitcoord[1]) + str(hitcoord[2]))
            return int(row)-1, alphaConvert[column]

        print("Please input a coordinate (A-J1-10)")
        hitcoord = list(input("Please input hit coordinates (ex. A1): "))
            
    
    
def hitShips(board):
    hits = 0
    for row in board:
        for column in row:
            if column == "💥":
                hits += 1
    return hits

def createShips2(board):
    shipLen = [5,4,3,3,2]
    shipAvalible = 5
    directionposibilities = ["vertical", "horizontal"]
    j = 0
   

    
    for i in range(shipAvalible):
        boatMade = False

        #REGULAR VAR STATMENTS
        direction = random.choice(directionposibilities)   
        col = randint(0,9)
        row = randint(0,9) 

        #DEBUG VAR STATMENTS
        #col = 6
        #row = 3
        #direction = "horizontal"
        

        while boatMade == False:
            
   
            if direction == "vertical":
                buildCount = 0
                if col + int(shipLen[i]) <= 11: #check ship within boundaries BROKEN
                #if row-j > 0:
                    colission = False
                    for i in range(0, int(shipLen[i])):
                        buildCount += 1
                        if board[int(row-i)][int(col)-1] == "💥": 
                            if colission:
                                pass
                            else:
                                colission = True
                    if colission:
                        col = randint(0,9)
                        row = randint(0,9)
                    else:
                       
                        for j in range(buildCount):
                            board[int(row-j)][int(col)-1] = "💥"
                            
                        boatMade = True
                else:
                    col = randint(0,9)
                    row = randint(0,9)
            if direction == "horizontal":
                if col + int(shipLen[i]) <= 10: #check ship within boundaries BROKEN
                    colission = False
                    buildCount = 0
                    for i in range(0, int(shipLen[i])):
                        buildCount += 1
                        if board[int(row)][int(col)+i-1] == "💥":
                            if colission:
                                pass
                            else:
                                colission = True
                    if colission:
                        col = randint(0,9)
                        row = randint(0,9)
                    else:
                       
                        for j in range(buildCount):
                            board[int(row)][int(col)+j-1] = "💥"
                        boatMade = True
                else:
                    col = randint(0,9)
                    row = randint(0,9)
        shipAvalible = shipAvalible - 1
    
    showBoard(board)
    return(board)






if __name__ == '__main__':
    main()