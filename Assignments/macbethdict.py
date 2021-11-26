#Library Imports
import string

def main():

    #School LTP
    #textfile = open(r"C:\Users\emurphy24\Documents\GitHub\CS2\Assignments\macbeth.txt")

    #Personal LPT
    #stextfile = open(r"C:\Users\elija\Documents\GitHub\CS2\Assignments\macbeth.txt")
    try:
        textfile = open(input("Please input the path to the file (include C:/): "))
    except OSError:
        print("Please input a path that exists. ")
        main()
    capyn = input("\nSet all words to lowercase? (y/n): ")                    #Checks if user wants to set all words to lowercase

    counts = dict()
    for line in textfile:                                                     #For each line in the text file...
        line = line.strip()                                                   #This line through 8 down (14-22 unless changed) formats for sorting
        line = line.strip("\n")
        if capyn == "n":
            line = line.lower()
        elif capyn != "y" or capyn != "n":
            print("Please input either y or n.")
            break 
        line = line.translate(line.maketrans("", "", string.punctuation))     #Removes all punctuation for word splitting
        word = line.split(" ")                                                #Defines the word at each space
        for instance in word:                                                 #For the instance of that word...
            if instance == "":
                break
            if instance in counts:                                            #If that word already has a key
                counts[instance] = counts[instance] + 1                       #Add one count to it's already created key
            else:                                                             #If that word dosent have a key,
                counts[instance] = 1                                          #Create one and give it a value
    finaldict = dict(reversed(sorted(counts.items(), key=lambda x: x[1])))    #Formats dictionary to have it from greatest to smallest value of keys
    topyn = (input("Top? (y/n): ")).lower()                                   #Checks to see if user wants only top results
    if topyn == "y":    
        topnumb = int(input("How many top?: "))                               #If they want top results, how many top results?
        print(top_n(dict(finaldict), topnumb))                                #Calls function to print top 10
    elif topyn == "n":   
        for key in list(finaldict.keys()):                                    #For every key in the dictionary,
            if finaldict[key] == int(1):                                      #If there is only one instnace of a word, returns correct grammar (time vs. times)
                print("'" + str(key) + "' was used", finaldict[key], "time.")
            else:
                print("'" + str(key) + "' was used", finaldict[key], "times.")
    else:
        print("Sorry, please input y or n")



def top_n(finaldict, topnumb):

    '''
    Finds the top used words in the text file

    :param name 1: finaldict the directory being used
    :param name 2: topnumb the amount of keys returned
    :param type 1: dictionary
    :param type 2: integer
    :returns: the formatted top keys in the given directory
    :return type: string
    :raises:
    '''

    loopbreak = topnumb
    topcount = 1
    output = ""
    for key in list(finaldict.keys()):
        output = str(output) + "\n" + str(topcount) + ". '" + str(key) + "' was used " + str(finaldict[key]) + " stimes."
        topcount = topcount + 1
        loopbreak = loopbreak - 1
        if loopbreak == 0:
            return str(output + "\n")

if __name__ == '__main__':
    main()