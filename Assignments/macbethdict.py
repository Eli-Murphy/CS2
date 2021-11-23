import string
from operator import itemgetter
import os

def main():
    print("Hello World!")
    macbeth = open(r"C:\Users\emurphy24\Documents\GitHub\CS2\Assignments\macbeth.txt")
    counts = dict()
    for line in macbeth:
        line = line.strip()
        line = line.lower()
        line = line.translate(line.maketrans("", "", string.punctuation))
        word = line.split(" ")
        for instance in word:
            if instance in counts:
                counts[instance] = counts[instance] + 1
            else:
                counts[instance] = 1
    finaldict = dict(reversed(sorted(counts.items(), key=lambda x:x[1])))
    #finaldict = dict(sorted())
    if os.path.exists(r"c:\Users\emurphy24\Documents\GitHub\CS2\Assignments\macbethoutput.txt"):
        os.remove(r"c:\Users\emurphy24\Documents\GitHub\CS2\Assignments\macbethoutput.txt")
        output = open(r"c:\Users\emurphy24\Documents\GitHub\CS2\Assignments\macbethoutput.txt", "w+")
    else:
        output = open(r"c:\Users\emurphy24\Documents\GitHub\CS2\Assignments\macbethoutput.txt", "w+")
    top10ornah = input("top 10 or nah (y/n): ")
    if top10ornah == "n":
        for key in list(finaldict.keys()):
            print(key, ":", finaldict[key])
            result = str(key) + " : " + str(finaldict[key])
            output.write(result)
            output.write("\n")       
    elif top10ornah == "y":
        result = top10(finaldict)



def top10(finaldict):
    result = dict(sorted(finaldict.items(), key = itemgetter(1), reverse = True)[:10])

    

if __name__ == '__main__':
    main()