import os
from os import walk, path
import string
import matplotlib.pyplot as plt

path = "C:\\Users\emurphy24\Documents\GitHub\CS2\Assignments\shakes"            #CHANGE DEPENDING ON MACHINE

def main():

    global path
    if path.exists(path): 
        os.chdir(path)
        dir = path

    #Above section checks to see if this device is Eli's School Laptop or other user

    else:
        dirinput = input("Please input the path to the dir of your shakespeare and breakwords folder (ex: C:\\Users\...\shakes): ")
        os.chdir(dirinput)
        dir = dirinput

    #In case it is not my laptop, it takes an input to the shakespeare directory

    breakwords = dir + "\\breakwords.txt"
    alldict = dict()
    while True:
        #Breakwords: Opens a text file that contains words that are to be ignored (and, or, the, etc.)
        bwtxt = open(breakwords, "r")
        content = bwtxt.read()
        bwlist = content.split("\n")
        bwtxt.close()
        
        #Menu
        print("""MENU OPTIONS:

        Input the number of the option you would like:

        (1): Collect data from specific shakespeare file in directory
        (2): Compile data from all shakepeare files in directory into one dictionary
        (3): Add word to the breakwords text file
        (4): Top results of every text file
        """)
        minput = input("Input: ")
        
        
        if minput == "1":
            usercall = True
            alldict = specFile(bwlist, alldict, dir, usercall) #Call's a function to open a specific file in the directory
            topcall = True
        elif minput == "2":
            alldict = alldicts(bwlist, alldict)                #Call's a function to read all text files and compiles it to a directory
            topcall = True
        elif minput == "3":
            modBreakwords(dir)                                 #Call's a function to modify breakwords
            main()
        elif minput == "4":
            topEach(alldict, bwlist, dir)                      #Call's a function to collect the top results of selected files
            topcall = False
        else:
            print("Please print a number of one of the options!")
            main()
        finaldict = dict(reversed(sorted(alldict.items(), key=lambda x: x[1])))    #Formats dictionary to have it from greatest to smallest value of keys

        if topcall:

            topyn = input("\nWould you like to find the top results? (y/n): ")
            
            if topyn == "n".lower():
                for key in list(finaldict.keys()):                                         #For every key in the dictionary,
                    if finaldict[key] == int(1):                                           #If there is only one instnace of a word, returns correct grammar (time vs. times)
                        print("'" + str(key) + "' was used", finaldict[key], "time.")
                    else:
                        print("'" + str(key) + "' was used", finaldict[key], "times.")
            elif topyn == "y".lower():
                topnumb = int(input("How many top results would you like?: "))
                print(top_n(dict(finaldict), topnumb))
            else:
                print("Please enter either y or n.")

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
        output = str(output) + "\n" + str(topcount) + ". '" + str(key) + "' was used " + str(finaldict[key]) + " times."
        topcount = topcount + 1
        loopbreak = loopbreak - 1
        if loopbreak == 0:
            return str(output)

def alldicts(bwlist, alldict):
    '''
    Collects the amount of times a word was used in every text file in a directory

    :param name 1: bwlist the text file with breakwords for filtering
    :param name 2: alldict the directory being used through out the code
    :param type 1: Document file format
    :param type 2: Directory
    :returns: dictionary of every word counted
    :return type: dictionary
    :raises:
    '''

    for file in os.listdir():
        file = open(file, "r")
        for line in file:
            line = line.strip()
            line = line.lower()
            line = line.translate(line.maketrans("", "", string.punctuation))
            word = line.split(" ")
            for instance in word:
                if instance == " ":
                    alldict["Spaces"] = alldict["Spaces"] + 1
                if instance == "":
                    break
                if instance in bwlist:
                    break
                if instance != " " and instance != "":
                    if instance in alldict:
                        alldict[instance] = alldict[instance] + 1
                    else:
                        alldict[instance] = 1
                
        file.close()
    return alldict

def specFile(bwlist, alldict, dir, usercall):
    """
    Collects the amount of times a word was used in a specific file the user writes.

    :param name 1: bwlist the text file with breakwords for filtering
    :param name 2: alldict the directory being used through out the code
    :param name 3: dir the isolated directory path
    :param name 4: usercall test to see if it was called by the user or called by a function with sufficent data
    :param type 1: Document file format
    :param type 2: Dictionary
    :param type 3: string
    :param type 4: Boolean
    :returns: the count of instances of a word for a specific file
    :return type: dictionary
    """

    if usercall:
        filenames = next(walk(dir), (None, None, []))[2]  # [] if no file
        print("Below are all the files in the shakes directory: \n")
        fnumber = 1
        for x in range(len(filenames)):
            print("(" + str(fnumber) + ")", filenames[x])
            fnumber = fnumber + 1
        choice = input("\nWhat number file do you want to open?: ")
        if choice.isdigit() and int(choice) < fnumber and int(choice) > 0:
            path = dir + "\\" + str(filenames[int(choice)-1])
            file = open(path, "r")
    else:
        path = dir
        file = open(path, "r")
    for line in file:
        line = line.strip()
        line = line.lower()
        line = line.translate(line.maketrans("", "", string.punctuation))
        word = line.split(" ")
        for instance in word:
            if instance == " ":
                alldict["Spaces"] = alldict["Spaces"] + 1
            if instance == "":
                break
            if instance in bwlist:
                break
            if instance != " " and instance != "":
                if instance in alldict:
                    alldict[instance] = alldict[instance] + 1
                else:
                    alldict[instance] = 1
            
    file.close()
    return alldict

def modBreakwords(dir):
    """
    Add's words to the breakwords text file.

    :param name 3: dir the isolated directory path
    :param type 3: string
    :returns: void
    :return type: void
    """
    breakwords = str(dir) + "\\breakwords.txt"
    bwtxt = open(breakwords, "a")
    word = input("What word would you like to add?: ").lower()
    bwtxt.write("\n" + word)

def topEach(alldict, bwlist, dir):
    """
    Collects the top n used words in selected text files.

    :param name 1: bwlist the text file with breakwords for filtering
    :param name 2: alldict the directory being used through out the code
    :param name 3: dir the isolated directory path
    :param type 1: Document file format
    :param type 2: Dictionary
    :param type 3: string
    :returns: the count of instances of a word for a specific file
    :return type: dictionary
    """
    filenames = next(walk(dir), (None, None, []))[2]
    print("Below are all the files in the shakespeare directory: \n")
    fnumber = 1
    for x in range(len(filenames)):
        print("(" + str(fnumber) + ")", filenames[x])
        fnumber = fnumber + 1
    choice = input("\nWhat number file/s do you want to open? (seperate by #,#,#,#): ")
    
    choice = choice.strip()
    choiceslist = choice.split(",")

    try:
        topnumb = int(input("How many top results would you like?: "))
    except:
        print("Please input a number for the top results. ")
        main()
    graphyn = input("Would you like your results to be graphed? (y/n): ").lower()
    if graphyn == "y":
        n = topnumb
        x = input("Title of your X-Axis: ")
        y = input("Title of your Y-Axis: ")
        chart = input("Type of chart (pie, bar, line): ")
    for x in range(len(choiceslist)):
        path = dir + "\\" + str(filenames[int(choiceslist[x])-1])
        title = str(topnumb) + " Results in " + str(path)
        usercall = False
        finaldict = dict(reversed(sorted(specFile(bwlist, alldict, path, usercall).items(), key=lambda x: x[1])))
        topresults = top_n(finaldict, topnumb)
        
        print("\nResults for: " + path + "\n"+ topresults + "\n")
        if graphyn == "y":
            
            print("DEBUG" + path)
            graph = graphDict(finaldict, n, x, y, title, chart)
            graph.show()

def graphDict(finaldict, n, title, chart):
    """
    Graphs a dictionary of instaces of a word being used in a text file

    :param name 1:finaldict the directory being used to be converted into a graph
    :param name 2:n number of x values in graph
    :param name 3:title chart title
    :paran name 4:chart type of chart needed
    :param type 1: dictionary
    :param type 2: integer
    :param type 3: string
    :param type 4: string
    :returns: a chart of the words and their instances
    :return type: custon pyplot module object
    """

    x = "Words"
    y = "Instances"

    try:
        
        #this separates the matching keys and values to its own 
        #variables, making it easier to work with
        
        d = dict(list(finaldict.items())[:n])
        keys = d.keys()     
        values = d.values()
        #print(d)
        
        
        if chart == "line":
            plt.plot(keys, values)
            plt.ylabel(y)
            plt.xlabel(x)
            plt.title(title)
            return plt
        elif chart == "bar":
            plt.bar(keys, values)
            plt.ylabel(y)
            plt.xlabel(x)
            plt.title(title)
            print(type(plt))
            return plt
        elif chart == "pie":
            plt.pie(values, labels = keys, shadow=True, autopct='%1.1f%%',radius=1.3)
            plt.title(title)  
            return plt
        else:
            print("Sorry! Thats not an option.")
    except:
        print("Error, missing data.")
    
if __name__ == '__main__':
    main()