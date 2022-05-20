from threading import local
import numpy as np
import math as mt


def countUniqueValues(fibNumber):
    fibnumbers = fibonacciSeq(fibNumber)
    #print(fibnumbers)

    pascTri = getPascTri(len(fibnumbers))
    #print(pascTri)

    output = getNumbers(pascTri, fibnumbers)

    newout = checkOcc(output, len(output))  

    #print(len(newout))

    return len(newout)  


def checkOcc(output, n):
    newout = []
    mp = dict()
    for i in range(n):
        if output[i] in mp.keys():
            mp[output[i]] += 1
        else:
            mp[output[i]] = 1

    for j in mp:
        if mp[j] == 1:
            newout.append(j)
    return newout



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
    startrow = [0]
    iterDepth = []
    output = []
    for i in range(len(fibnumbers)):
        
        iterType = ((i+1)//2) + ((i+1)%2)
        startrow.append(iterType)
        iterDepth.append(iterType)
        

        fibsum = []
        row = 0
    startrow.pop()
    #print(startrow)
    for j in range(len(fibnumbers)):
        sumInstance = []
        item = iterDepth[j]-1
        for k in range(iterDepth[j]):
            sumInstance.append(pascTri[startrow[j]][item])
            output.append(pascTri[startrow[j]][item])
            item = item-1
            startrow[j] = startrow[j]+1
        #print("sum:", sumInstance)
    return output
                

        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    fibNumber = int(input().strip())

    result = countUniqueValues(fibNumber)

    #fptr.write(str(result) + '\n')

    #fptr.close()