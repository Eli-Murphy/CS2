import random
from re import T



def main():

    startyn = input("Would you like to start the game? (y/n): ").lower()
    symbol = input("What symbol would you like to represent you? (X, O): ").upper()
    
    if startyn == "y":
        start = "p"
        game(start, symbol)

    elif startyn == "n":
        start = "c"
        game(start, symbol)


def game(start, symbol):
    tttboard = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]

    if symbol == "X":
        csymbol = "O"
    else:
        csymbol = "X"
    
    turn = start
    count = 1
    while True:
        if turn == "p":
            if count == 10:
                print("\nDraw!")
                printttt(tttboard)
                playagain = input("\nWould you like to play again? (y/n): ").lower()
                if playagain == "y":
                    main()
                else:
                    break
            output = playercall(tttboard)
            row = output[0]
            columb = output[1]
            tttboard[row][columb] = symbol
            turn = "c"
            count += 1
            if winDetect(tttboard, symbol):
                print("\nPlayer Wins!")
                printttt(tttboard)
                playagain = input("\nWould you like to play again? (y/n): ").lower()
                if playagain == "y":
                    main()
                else:
                    break
        if turn == "c":
            if count == 10:
                print("\nDraw!")
                printttt(tttboard)
                break
            output = cpucall(tttboard)
            row = output[0]
            columb = output[1]
            tttboard[row][columb] = csymbol
            turn = "p"
            count += 1
            if winDetect(tttboard, csymbol):
                print("\nComputer Wins!")
                printttt(tttboard)
                playagain = input("\nWould you like to play again? (y/n): ").lower()
                if playagain == "y":
                    main()
                else:
                    break
        printttt(tttboard)


    

            
def cpucall(tttboard):
    rnumb = random.randint(0,2)
    cnumb = random.randint(0,2)

    while tttboard[rnumb][cnumb] != " ":
        
        rnumb = random.randint(0,2)
        cnumb = random.randint(0,2)
    output = [rnumb, cnumb]

    return output


def playercall(tttboard):
    while True:
        columb = input("What columb would you like to put your marker in? (1,2,3): ")
        row = input("What row would you like to put your marker in? (1,2,3): ")

        try:
            row = int(row)
            row = row - 1
            columb = int(columb)
            columb = columb - 1
        except:
            print("Please enter 1, 2, or 3 into the questions above. ")
        
        while tttboard[row][columb] != " ":
            print("Sorry, that position is taken!\n")
            columb = input("What columb would you like to put your marker in? (1,2,3): ")
            row = input("What row would you like to put your marker in? (1,2,3): ")
        output = [row, columb]

        return output


def winDetect(tttboard, symbol):
    pos1 = tttboard[0][0]
    pos2 = tttboard[0][1]
    pos3 = tttboard[0][2]
    pos4 = tttboard[1][0]
    pos5 = tttboard[1][1]
    pos6 = tttboard[1][2]
    pos7 = tttboard[2][0]
    pos8 = tttboard[2][1]
    pos9 = tttboard[2][2]

    if pos1 == symbol and pos2 == symbol and pos3 == symbol or pos1 == symbol and pos5 == symbol and pos9 == symbol or pos1 == symbol and pos4 == symbol and pos7 == symbol:
        #All possible combinations 
        return True
    elif pos2 == symbol and pos5 == symbol and pos8 == symbol:
        return True
    elif pos3 == symbol and pos5 == symbol and pos7 == symbol or pos3 == symbol and pos6 == symbol and pos9 == symbol:
        return True
    elif pos4 == symbol and pos5 == symbol and pos6 == symbol or pos7 == symbol and pos8 == symbol and pos9 == symbol:
        return True

def printttt(tttboard):
    pos1 = tttboard[0][0]
    pos2 = tttboard[0][1]
    pos3 = tttboard[0][2]
    pos4 = tttboard[1][0]
    pos5 = tttboard[1][1]
    pos6 = tttboard[1][2]
    pos7 = tttboard[2][0]
    pos8 = tttboard[2][1]
    pos9 = tttboard[2][2]

    print(pos1+ " | "+ pos2+ " | "+ pos3 )
    print('--+---+--')
    print(pos4+ " | "+ pos5+ " | "+ pos6 )
    print('--+---+--')  
    print(pos7+ " | "+ pos8+ " | "+ pos9 )



if __name__ == '__main__':
    main()
