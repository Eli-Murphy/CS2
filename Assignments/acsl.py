#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findTime' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING cstr as parameter.
#

def findTime(cstr):
    # Write your code here

    h = 0
    m = 0
    s = 0


    ccl = list(cstr)

    if ccl[0] == "R":
        h = h + 1
    elif ccl[0] == "G":
        m = m + 5
    elif ccl[0] == "B":
        s = s + 5
    elif ccl[0] == "Y":
        h = h + 1
        m = m + 5
    elif ccl[0] == "M":
        h = h + 1
        s = s + 5
    elif ccl[0] == "C":
        m = m + 5
        s = s + 5

    if ccl[1] == "R":
        h = h + 1
    elif ccl[1] == "G":
        m = m + 5
    elif ccl[1] == "B":
        s = s + 5
    elif ccl[1] == "Y":
        h = h + 1
        m = m + 5
    elif ccl[1] == "M":
        h = h + 1
        s = s + 5
    elif ccl[1] == "C":
        m = m + 5
        s = s + 5

    if ccl[2] == "R":
        h = h + 2
    elif ccl[2] == "G":
        m = m + 10
    elif ccl[2] == "B":
        s = s + 10
    elif ccl[2] == "Y":
        h = h + 2
        m = m + 10
    elif ccl[2] == "M":
        h = h + 2
        s = s + 10
    elif ccl[2] == "C":
        m = m + 10
        s = s + 10

    if ccl[3] == "R":
        h = h + 3
    elif ccl[3] == "G":
        m = m + 15
    elif ccl[3] == "B":
        s = s + 15
    elif ccl[3] == "Y":
        h = h + 3
        m = m + 15
    elif ccl[3] == "M":
        h = h + 3
        s = s + 15
    elif ccl[3] == "C":
        m = m + 15
        s = s + 15

    if ccl[4] == "R":
        h = h + 5
    elif ccl[4] == "G":
        m = m + 25
    elif ccl[4] == "B":
        s = s + 25
    elif ccl[4] == "Y":
        h = h + 5
        m = m + 25
    elif ccl[4] == "M":
        h = h + 5
        s = s + 25
    elif ccl[4] == "C":
        m = m + 25
        s = s + 25

    if s >= 60:
        s = s -60
        m = m + 1
    if m >= 60:
        m = m -60
        h = h + 1
    if h > 12:
        h = h - 12

    if h < 10:
        h = "0" + str(h)
    if m < 10:
        m = "0" + str(m)
    if s < 10:
        s = "0" + str(s)  



    

    output = str(h) + ":" + str(m) + ":" + str(s)
    return output

if __name__ == '__main__':
    cstr = input("Input: ")
    print(findTime(cstr))

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # cstr = input()

    # result = findTime(cstr)

    # fptr.write(result + '\n')

    # fptr.close()
