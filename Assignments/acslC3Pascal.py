from threading import local


def countUniqueValues(fibNumber):
    fibnumbers = fibonacciSeq(fibNumber)
    print(fibnumbers)

    pascTri = getPascTri(len(fibnumbers))
    print(pascTri)

    getNumbers(pascTri, fibnumbers)


def fibonacciSeq(fibNumber):
    fiblist = [1, 1]
    if fibNumber == 1:
        return [1]
    while fiblist[-1] != fibNumber:
        nextVal = fiblist[len(fiblist) - 1] + fiblist[len(fiblist) - 2]
        fiblist.append(nextVal)
    return fiblist
        
def getPascTri(fibNumber):
    pascTri = []
    for i in range(fibNumber):
        locallist = []
        for j in range(i+1):
            if j == 0 or j==i:
                locallist.append(1)
            else: 
                locallist.append(pascTri[i-1][j-1]+pascTri[i-1][j])
        pascTri.append(locallist)
    return pascTri

def getNumbers(pascTri, fibnumbers):
    for i in range(len(fibnumbers)):
        iterType = ((i+1)//2) + ((i+1)%2)
        fibsum = []
        row = 0
        item = 0
        for j in range(iterType):
            fibsum.append(pascTri[row][item])
            row = row + 1
            if j != 1:
                

        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    fibNumber = int(input().strip())

    result = countUniqueValues(fibNumber)

    #fptr.write(str(result) + '\n')

    #fptr.close()