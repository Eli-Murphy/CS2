import os

def findFile(c):
    print(c)
    ls = next(os.walk(c))
    # files = ls[2] if len(ls) > 2 else []
    print(ls)
    if len(ls) > 1:
        dirs = ls[1]
        for i in dirs:
            findFile(c+'/'+i)
    return ""

rootDir = r"C:\Users\emurphy24\Desktop"
findFile(rootDir)