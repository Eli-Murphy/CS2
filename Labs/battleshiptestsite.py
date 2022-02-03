

def placeShips(board):
    shipSize = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2} #size of each ship
    shipList = [['Carrier', 1], ['Battleship', 1], ['Cruiser', 1], ['Submarine', 1], ['Destroyer', 1]]
    
    
    

    for x in shipList: #place ships
        r = 0

        while x[1] > 0: #check there's ships available
            r += 1
            type = x[0]
            ship_size = shipSize[x[0]]
            if placeShip(board, ship_size, type):
                x[1] -= 1
            else:
                print("Can't put boat here.")


def placeShip(board, ship_size, type):
    print("Where would you like to put your", str(type) + ", the", str(ship_size), "long boat? (A1)")
    pos = input("Input here: ")
    row, column = locationFormat(pos)
    angle = input("Place it up, down, left, or right? (u,d,l,r): ").upper()
    if angle == "U":
        colission = False
        buildCount = 0
        if 0 <= (row+1 + int(-1 * ship_size)) <= 9:
            for i in range(ship_size):
                buildCount += 1
                if board[int(row-i)][int(column)] == "⬛": 
                    colission = True
                    pass
        else:
            colission = True
        
        if colission is False:
            for k in range(buildCount):
                board[int(row-k)][int(column)] = "⬛"
            showBoard(board)
    
    if angle == "D":
        colission = False
        buildCount = 0
        if row + int(ship_size) <= 9: #WORKS
            for i in range(ship_size):
                buildCount += 1
                if board[int(row+i)][int(column)] == "⬛": 
                    colission = True
                    pass
        else:
            colission = True
        if colission is False:
            for k in range(buildCount):
                board[int(row+k)][int(column)] = "⬛"
            showBoard(board)
    
    if angle == "R":
        colission = False
        buildCount = 0
        if 0 <= (column-1 + int(ship_size)) <= 9: #WORKS
            for i in range(ship_size):
                buildCount += 1
                if board[int(row)][int(column)+i] == "⬛": 
                    colission = True
                    pass
    
        else:
            colission = True
        if colission is False:
            for k in range(buildCount):
                board[int(row)][int(column)+k] = "⬛"
            showBoard(board)

    if angle == "L":
        colission = False
        buildCount = 0
        if column - int(ship_size) <= 9:
            for i in range(ship_size):
                buildCount += 1
                if board[int(row)][int(column)-i] == "⬛": 
                    colission = True
                    pass
    
        else:
            colission = True
        if colission is False:
            for k in range(buildCount):
                board[int(row)][int(column)-k] = "⬛"
            showBoard(board)
    if colission:
        return False
    else:
        return True

    
def locationFormat(hitcoord):
    alphaConvert = {'A': 0, 'B':1, 'C':2,'D':3,'E':4,"F":5,'G':6,'H':7, 'I':8, "J":9}
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

board = [["🟦"] * 10 for x in range(10)]


placeShips(board)