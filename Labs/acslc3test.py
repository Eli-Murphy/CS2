fibNumber = 13
fiblist = [1,1]
if fibNumber == 1:
    print(1)
while fiblist[-1] != fibNumber:
    nextVal = fiblist[len(fiblist) - 1] + fiblist[len(fiblist) - 2]
    fiblist.append(nextVal)
print(fiblist)