def main():
    print("Hello World!")
    macbeth = open(r"C:\Users\emurphy24\Documents\GitHub\CS2\Assignments\macbeth.txt", "r")
    counts = dict()
    for line in macbeth:
        line = line.strip()
        line = line.lower()
        word = line.split(" ")
        for word in line:
            if word in counts:
                counts[word] = counts[word] + 1
            else:
                counts[word] = 1
    finaldict = dict( sorted(counts.items(), key=lambda x: x[0].lower()) )
    for key in list(finaldict.keys()):
       print(key, " ", finaldict[key])

if __name__ == '__main__':
    main()