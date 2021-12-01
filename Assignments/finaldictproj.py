#Library Imports
import string
import os
import matplotlib.pyplot as plt

def main():

    try:
        #pathinput = input("Please input the path to the file (dir/folder/file.txt): ")
        pathinput = r"C:\Users\emurphy24\Documents\GitHub\CS2\Assignments\macbeth.txt"
        drive, path = os.path.splitdrive(pathinput)                          #Splits input into drive and path, path is redundant
        
        if pathinput.lower() and not pathinput.endswith(".txt"):             #Verifies input is indeed a text file
            print("Sorry, file must have a .txt extension.\n")
            main()
        elif drive == "":                                                    #Verifies input has a drive selected
            print("Please verify that you have inputted a drive (ex. C:\\)\n")
            main()
        else:
            textfile = open(pathinput)
    except OSError:
        print("OSError: Inputted path is not a path or the file/directory does not exists. Please input a valid path.\n")
        main()


    capyn = input("\nSet all words to lowercase? (y/n): ")                    #Checks if user wants to set all words to lowercase
    counts = dict()

    for line in textfile:
        line = line.strip()
        line = line.lower()
        line = line.translate(line.maketrans("", "", string.punctuation))
        word = line.split(" ")
        for instance in word:
            if instance == "":
                break
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
        #print(key, ":", finaldict[key])
        result = str(key) + " : " + str(finaldict[key])
        output.write(result)
        output.write("\n")       
    for line in textfile:                                                     #For each line in the text file...
        line = line.strip()                                                   #This line through 8 down (27-34 unless changed) formats for sorting
        line = line.strip("\n")
        if capyn == "y":
            line = line.lower()
        elif capyn != "y" and capyn != "n":
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
    topyn = (input("\nTop? (y/n): ")).lower()                                 #Checks to see if user wants only top results
    if topyn == "y":    
        topnumb = int(input("\nHow many top?: "))                             #If they want top results, how many top results?
        result = top_n(dict(finaldict), topnumb)                                #Calls function to print top instances
        print(result)
    elif topyn == "n":   
        for key in list(finaldict.keys()):                                    #For every key in the dictionary,
            if finaldict[key] == int(1):                                      #If there is only one instnace of a word, returns correct grammar (time vs. times)
                print("'" + str(key) + "' was used", finaldict[key], "time.")
            else:
                print("'" + str(key) + "' was used", finaldict[key], "times.")
    graphyn = (input("\nGraph? (y/n): ")).lower()
    if graphyn == 'y':
        topnumb = int(input("\nHow many top?: "))
        plt = graphing(finaldict, topnumb)
        plt.show()
    else:
        print("\nSorry, please input y or n.")



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

def graphing(finaldict, n):
    try:
        
        #this separates the matching keys and values to its own 
        #variables, making it easier to work with
        
        d = dict(list(finaldict.items())[:n])
        keys = d.keys()     
        values = d.values()
        #print(d)
        
        x = input("\nWhat is your X-Axis?: ")
        y = input("What is your Y-Axis?: ")
        title = input("What is the title of the graph?")
    
        chart = input("Which chart would you like to use? (line, bar, or pie): ")
        if chart == "line":
            plt.plot(keys, values)
            plt.ylabel(x)
            plt.xlabel(y)
            plt.title(title)
            return plt
        elif chart == "bar":
            plt.bar(keys, values)
            plt.ylabel(x)
            plt.xlabel(y)
            plt.title(title)
            return plt
        elif chart == "pie":
            plt.pie(values, labels = keys, shadow=True, autopct='%1.1f%%',radius=1.3)
            plt.title(title)  
            #To be honest, im not sure what all these mean, but I do know that this 
            #customizes the pie chart.
            return plt
        else:
            print("Sorry! Thats not an option.")
    except:
        print("Error, missing data.")
        

if __name__ == '__main__':
    main()