#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMatch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING word
#  2. STRING guesses
#

def getBest(result):
    value = 0
    result = list(result)
    for i in range(len(result)):
        if result[i] == "G":
            value += 2
        if result[i] == "Y":
            value += 1
    return(value)
    
def sortAlgo(guessWordleStr):
    for i in range(len(guessWordleStr)):
        if guessWordleStr[i] == "-----":
            del guessWordleStr[i]
            i = i-1
    
    

def findMatch(word, guess):
    wordle_pattern = []
    wordL = list(word)
    guessL = list(guess)
    for i, letter in enumerate(guessL):
        if wordL[i] == guessL[i]:
            wordle_pattern.append("G")
        elif letter in wordL:
            wordle_pattern.append("Y")
        else:
            wordle_pattern.append("-")
    return "".join(wordle_pattern)

def main(guesslist, word):
    guessWordleStr = {}
    guessValue = {}
    for i in range(len(guesslist)):
        guessWordleStr[guesslist[i]] = findMatch(word, guesslist[i])
    for j in range(len(guessWordleStr)):
        guessValue[guesslist[j]] = getBest(guessWordleStr[guesslist[j]])
    #print(guessValue)
    sorteddict = {k: v for k, v in sorted(guessValue.items(), key=lambda item: item[1])}
    print(sorteddict)
    sortedkeys = list(sorteddict.keys())
    print(sortedkeys.sort())
    return " ".join(sortedkeys[-6:])





if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #word = input()

    word = "apple"
    guesses = "apple teste vagin sweat orang copes perio cummy"

    #guesses = input()

    guesslist = guesses.split()

    result = main(guesslist, word)
    print(result)
    #fptr.write(result + '\n')


    #fptr.close()
