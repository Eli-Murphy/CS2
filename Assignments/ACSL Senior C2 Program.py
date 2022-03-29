#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fibCypher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. CHARACTER option
#  2. INTEGER num1
#  3. INTEGER num2
#  4. CHARACTER key
#  5. STRING msg
#

def fibCypher(option, num1, num2, key, msg):
    if option == "E":
        n = len(msg)
        fib = fibo(n, num1, num2)
        msg = list(msg)
        strout = ""
        for i in range(len(msg)):
            if (i%2) == 0:
                # while fib[i] >= 26:
                #     fib[i] -= 26
                fib[i] = fib[i] % 26
                if ord(key) + fib[i] > 122:
                    distance = (ord(key) + fib[i]) - 122
                    nkey = 97 + distance - 1
                    char_enc = ord(msg[i]) + 3 * nkey 
                else:
                    char_enc = ord(msg[i]) + 3 * (ord(key) + fib[i])
                strout = strout + str(char_enc) + " "
            
            
            
            else:
                # while fib[i] >= 26:
                #     fib[i] -= 26
                fib[i] = fib[i] % 26
                if ord(key)- fib[i] < 97:
                    distance = abs((ord(key) - fib[i]) - 97)
                    nkey = 122 - distance + 1
                    char_enc = ord(msg[i]) + 3 * nkey
                else:
                    char_enc = ord(msg[i]) + 3 * (ord(key) - fib[i])
                strout = strout + str(char_enc) + " "
        return strout
    elif option == "D":
        charlist = msg.split(" ")
        strout = ""
        while("" in charlist):
            charlist.remove("")
        fib = fibo(len(charlist), num1, num2)
        for i in range(len(charlist)):
            fib[i] = fib[i] % 26
            if (i%2) == 0:
                
                if ord(key) + fib[i] > 122:
                    distance = (ord(key) + fib[i]) - 122
                    nkey = 97 + distance - 1
                    char = int(charlist[i]) - 3*(nkey) 
                else:
                    char = int(charlist[i]) - 3*(ord(key)+fib[i])

                strout = strout + chr(char)
            else:
                if ord(key)- fib[i] < 97:
                    distance = abs((ord(key) - fib[i]) - 97)
                    nkey = 122 - distance + 1
                    char = int(charlist[i]) - 3*(nkey)
                else:
                    char = int(charlist[i]) - 3*(ord(key)-fib[i])


                strout = strout + chr(char)
    return strout

    
def fibo(n, num1, num2):
    fib = [num1]
    for i in range(0, n-1):
        num1, num2 = num2, num1+num2
        fib.append(num1)
    return fib
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    option = input()[0]

    num1 = int(input().strip())

    num2 = int(input().strip())

    key = input()[0]

    msg = input()


    result = fibCypher(option, num1, num2, key, msg)
    print(result)