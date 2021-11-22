import string

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
    finaldict = dict( sorted(counts.values(), key=lambda x: x[0].lower()) )
    for key in list(finaldict.keys()):
        print(key, " ", finaldict[key])

if __name__ == '__main__':
    main()