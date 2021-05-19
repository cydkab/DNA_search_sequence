# open database and sequence, read it
# calculate the times a small sequence appears on the scv file
# match the dna database to verify if it exists
import csv
import sys
import re

if (len(sys.argv)) < 3:
    print("Usage: python dna.py data.csv sequence.txt")
else:
    sys.argv[1]     # database of DNAs
    sys.argv[2]     # DNA to examine
    with open(sys.argv[1], "r") as file:    # open file of the database
        reader = csv.reader(file)   # read the file of the database
        line_count = 0  # count the lines to ensure only the first is openned and saved in "substrings"
        for row in reader:
            if line_count == 0:
                substrings = row    # allocate the header to a list
                line_count = + 1     # adding one to ensure its only the first line to be read
    counter = [0]*len(substrings)    # create a list of 0's of the size of the header wich has the words cointainned to be searched
    for i in range(1, (len(substrings)), 1):    # loop to read the STR to be seached
        dna = open(sys.argv[2], "r")    # open the sequence to read)
        pattern = "((" + re.escape(substrings[i]) + ")+)"
        group = re.findall(pattern, dna.read())    # group the patterns of the word
        if len(group) == 0:     # In case the group has nothing, just ignore and close the file
            continue
        else:  # In case the group has something, just calculate the longest string occorence in a row
            largest = max([item for tpl in group for item in tpl], key=len)
            count = (len(largest) / (len(substrings[i])))
            counter[i] = int(count)
        dna.close
    line_count = 0
    y = False
    with open(sys.argv[1], "r") as file:    # open file of the database
        reader = csv.reader(file)
        argument_count = 0
        for row in reader:  # iterate the rows
            argument_count = 0
            if line_count == 0:  # skip the first row wich is the header
                line_count = + 1
            else:   # iterate the other rows
                index = 0
                for i in range(len(substrings)):  # iterate through the substrings
                    if index == 0:
                        index = + 1  # i was not getting an int, so an option to turn it to an index
                        # This condition is made to skip the 0 index substring
                    else:
                        row[index] = int(row[index])  # Cast the substring to an int
                        index += 1
                
                for i in range(1, len(substrings), 1):  # loop through the list "row" and counter with the search results
                    if counter[i] == row[i]:
                        argument_count += 1
                        if argument_count == (len(row) - 1):    # excluding the header of the name, it has to have the number
                            # of columns -1 matches to be that person
                            print(row[0])  # print the "header" wich has the name of the person the dna STR matches
                            y = True
        if y == False:
            print("No match")                            
    
