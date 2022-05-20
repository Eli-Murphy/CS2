#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numFibonacciCycles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. FLOAT realPartLL
#  2. FLOAT imagPartLL
#  3. FLOAT realPartUR
#  4. FLOAT imagPartUR
#  5. FLOAT incr
#

def numFibonacciCycles(realPartLL, imagPartLL, realPartUR, imagPartUR, incr):
    
    

    imagArray = []

    cycAmount = []

    fibo = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

    count = 0

    ballocks = round((((realPartUR-realPartLL)/incr)+1),0)
    buttocks = round((((imagPartUR-imagPartLL)/incr)+1),0)


    for i in range(int(ballocks)):
        for j in range(int(buttocks)):
            realNumber = round((realPartLL + (incr*i)), 3)
            imagNumber = round((imagPartLL + (incr*j)), 3)
            imagArray.append([realNumber, imagNumber])

    for imagNumber in imagArray:
        result = mandelfunc(imagNumber)
        cycAmount.append(result)
    for i in cycAmount:
        if i in fibo:
            count = count + 1

    return count

def mandelfunc(imagNumber):
    result = 0
    absHit = False
    cycAmount = 0
    mandelNumber = []
    a = imagNumber[0]
    b = imagNumber[1]
    while True:
        cycAmount += 1
        if result == 0:
            result = imagNumber
        else:
            c = result[0]
            d = result[1]

            e = multiplication(c,d,c,d)
            result = addition(e[0],e[1], a, b)
        if result in mandelNumber:
            break
        elif absoluteVal(result[0],result[1])>4:
            absHit = True
            break
        else:
            mandelNumber.append(result)
    if absHit == False:
        return (cycAmount-1)-mandelNumber.index(result)


def addition(a, b, c, d):

    list = [round((a+c),3), round((b+d),3)]

    return list

def multiplication(a, b, c, d):

    list = [round(((a*c)-(b*d)), 3), round(((a*d)+(b*c)),3)]

    return list

def absoluteVal(a,b):

    return round(math.sqrt(round((a**2),3) + round((b**2),3)),3)    

    
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    realPartLL = float(input().strip())

    imagPartLL = float(input().strip())

    realPartUR = float(input().strip())

    imagPartUR = float(input().strip())

    incr = float(input().strip())

    result = numFibonacciCycles(realPartLL, imagPartLL, realPartUR, imagPartUR, incr)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
