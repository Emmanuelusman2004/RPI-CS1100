# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 14:01:09 2022

@author: Emmanuel Usman
"""
def stripwhitespacefromalllines(listwithspaces):
    #make list separate stuff by line without \n
    listofplainlinesnon = []
    for line in listwithspaces:
        l = line.replace("\n","")
        listofplainlinesnon.append(l)
    #turn the list of lines into a list of words
    justwordlist = []
    for line in listofplainlinesnon:
        x = line.split(" ")
        justwordlist.append(x)
    #remove any empty list spaces
    justdemwords = []
    for listofwords in justwordlist:
        lineofjustdemwords = []
        justdemwords.append(lineofjustdemwords)
        for word in listofwords:
            if word == "":
                continue
            else:
                lineofjustdemwords.append(word)
    return justdemwords
    
def removenoncharacters(listoflines2):
    listofnewlines = []
    for line in listoflines2:
        lineofwords = []
        for word in line:
            if word.isalpha() == False:
                wordcharacters = []
                for character in word:
                    if character.isalpha():
                        wordcharacters.append(character)
                string = ''.join(wordcharacters)
                string=string.lower()
                lineofwords.append(string)
            else:
                word = word.lower()
                lineofwords.append(word)
        listofnewlines.append(lineofwords)
    correctedlines = []
    for line in listofnewlines:
        if line == []:
            continue
        else:
            correctedlines.append(line)
    correctedeverything = []
    for line in correctedlines:
        correctedlinewithoutempty = []
        for word in line:
            if word == "" or word == " ":
                    continue
            else:
                correctedlinewithoutempty.append(word)
        correctedeverything.append(correctedlinewithoutempty)                  
    return correctedeverything


def parsefile(filename):
    f = open(filename, 'r')
    #get a list of all lines
    unparsedcontents = f.readlines()
    f.close()
    #strip the characters
    just_words_of_file_in_listoflines = stripwhitespacefromalllines(unparsedcontents)
    #remove all non-cahracters
    if filename != "stop.txt":
        just_real_words_in_listoflines = removenoncharacters(just_words_of_file_in_listoflines)
    #print(just_real_words_in_listoflines)
    if filename != "stop.txt":
        return just_real_words_in_listoflines
    else:
        return just_words_of_file_in_listoflines
def avgwordlen(listoflists):
    wordlengths = []
    count = 0
    for line in listoflists:
        for word in line:
            x = len(word)
            if word == "cant":
                x+=1
            wordlengths.append(x)
            count+=1
    avgwordlen = sum(wordlengths)/count
    return avgwordlen
#inputs
firstfile = input("Enter the first file to analyze and compare ==> ")
print(firstfile)
firstfile = firstfile.strip()
secondfile = input("Enter the second file to analyze and compare ==> ")
print(secondfile)
secondfile= secondfile.strip()
maxsep = input("Enter the maximum separation between words in a pair ==> ")
maxsep = maxsep.strip()
print(maxsep)
#parse files
firstfileparsed = parsefile(firstfile)

secondfileparsed = parsefile(secondfile)

#get stop words
stopfilelines = parsefile("stop.txt")
#stopfilelines = removenoncharacters(stopfilelines)

allstopwords = []
for word in stopfilelines:
    for wordd in word:
        allstopwords.append(wordd)
#TESTfirstfileparsed = [['hey','its','emmanuel','a','about','again'],['wouldnt','cannot','am','pokemongo']]

#remove stop words from docs
firstfile_listofnostopwordlines = []
for line in firstfileparsed:
    linewithnostopwords = []
    for word in line:
        if word in allstopwords:
            continue
        else:
            linewithnostopwords.append(word)
    firstfile_listofnostopwordlines.append(linewithnostopwords)
    
#TESTprint(firstfile_listofnostopwordlines)
secondfile_listofnostopwordlines = []
for line in secondfileparsed:
    linewithnostopwords = []
    for word in line:
        if word in allstopwords:
            continue
        else:
            linewithnostopwords.append(word)
    secondfile_listofnostopwordlines.append(linewithnostopwords)

#getting avg word lengths
avgwordfile1 = avgwordlen(firstfile_listofnostopwordlines)

avgwordfile2 = avgwordlen(secondfile_listofnostopwordlines)

#stopwords as a set
allstopwordset = set(allstopwords)

#ratio of distinct words and total words

lineofuniquewrdsfile1 = set()
count1 = 0
for line in firstfile_listofnostopwordlines:
    for word in line:
        lineofuniquewrdsfile1.add(word)
        count1+=1

uniquewordsratio1 = len(lineofuniquewrdsfile1)/count1

lineofuniquewrdsfile2 = set()
count2 = 0
for line in secondfile_listofnostopwordlines:
    for word in line:
        lineofuniquewrdsfile2.add(word)
        count2+=1

uniquewordsratio2 = len(lineofuniquewrdsfile2)/count2

#wordlength thingy

def wordsoflen(listoflines):
    #get all types of word length in the file
    wordlengths = set()
    wordoflen = []
    #retrieve wordlens
    for line in listoflines:
        for word in line:
            x = len(word)
            wordlengths.add(x)
    #make a list of lists with words with the same length
    for num in wordlengths:
        lineofwordlen = []
        for line in listoflines:
            for word in line:
                if len(word) == num:
                    lineofwordlen.append(word)
        wordoflen.append(lineofwordlen)
    listofwordlengths = []
    for numbers in wordlengths:
        listofwordlengths.append(numbers)
    #make a list with number of words with same length
    countofwordssamelength = []
    for listofwordswithsamelength in wordoflen:
        countofwords = 0
        for samelenwords in listofwordswithsamelength:
            countofwords+=1
        countofwordssamelength.append(countofwords)

    i = 0
    while i < len(listofwordlengths):
        print("{0:4}:{1:4}: ".format(i+1, countofwordssamelength[i]), end = "")
        if len(wordoflen[i]) > 6:
            print(wordoflen[i][0]+" " +wordoflen[i][1]+" "+wordoflen[i][2]+" ... " +wordoflen[i][-3]+" "+wordoflen[i][-2]+" "+wordoflen[i][-1])
        elif len(wordoflen[i]) <= 6:
            print(wordoflen[i][0:7][0],sep = " ")
        i+=1

#wordpairs thing

def wordpairs(listoflistsss,max_sep):
    allwordsinfile = []
    for line in listoflistsss:
        for word in line:
            allwordsinfile.append(word)
    wordpairs = []
    for word in allwordsinfile:
        i = 0
        while i < int(max_sep):
            tup = (word,allwordsinfile[i+1])
            wordpairs.append(tup)
            i+=1
        print(wordpairs)
wordpairs(secondfile_listofnostopwordlines,maxsep)

#body of output
print("")
print("Evaluating document {}".format(firstfile))
print("1. Average word length: {:.2f}".format(avgwordfile1))
print("2. Ratio of distinct words to total words: {:.3f}".format(uniquewordsratio1))
print("3. Word sets for document {}:".format(firstfile))
wordsoflen(firstfile_listofnostopwordlines)
print("4. Word pairs for document {}".format(firstfile))
print("5. Ratio of distinct word pairs to total: ") #ADDDDD
print("")
print("Evaluating document {}".format(secondfile))
print("1. Average word length: {:.2f}".format(avgwordfile2))
print("2. Ratio of distinct words to total words: {:.3f}".format(uniquewordsratio2))
print("3. Word sets for document {}:".format(secondfile))
wordsoflen(secondfile_listofnostopwordlines)
print("4. Word pairs for document {}".format(secondfile))
print("5. Ratio of distinct word pairs to total: ") #ADDDDD

    
    