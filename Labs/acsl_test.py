def main():
    msg = "386 358 425 415 347 419 405 402 377 377 390 416"
    key = "h"
    charlist = msg.split(" ")
    strout = ""
    fib = fibo(len(charlist), 3, 7)

    #For adding fib val
    # fib[6] = fib[6] % 26
    # print(fib[6])
    # if ord(key) + fib[6] > 122:
    #     distance = (ord(key) + fib[6]) - 122
    #     key = 97 + distance
    #     print(chr(key))

    #for subtracting fib val
    # if fib[5] >= 26:
    #     fib[5] -= 27
    # if ord(key)- fib[5] < 97:
    #     distance = abs((ord(key) - fib[5]) - 97)
    #     key = 122 - distance
    #     print(chr(key))

    #Decoding
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
    print(strout)

def fibo(n, num1, num2):
    fib = [num1]
    for i in range(0, n-1):
        num1, num2 = num2, num1+num2
        fib.append(num1)
    return fib

if __name__ == "__main__":
    main()