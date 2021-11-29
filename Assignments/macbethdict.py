import string
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
            if instance == " ":
                counts["Spaces"] = counts["Spaces"] + 1
            if instance == "\\n":
                counts["\\n"] = counts["\n"] + 1
            if instance != " ":
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

    for key in list(finaldict.keys()):
        print(key, ":", finaldict[key])
        result = str(key) + " : " + str(finaldict[key])
        output.write(result)
        output.write("\n")       

    

if __name__ == '__main__':
    main()