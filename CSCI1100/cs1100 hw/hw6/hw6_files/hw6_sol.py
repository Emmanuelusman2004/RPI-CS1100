# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 20:45:43 2022

@author: Emmanuel Usman
"""

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


def parse(file):
    f = open(file,'r')
    lines = f.readlines()
    f.close()
    justlineswithoutn = []
    for n in lines:
        lineswithoutns = n.split("\n")
        justlineswithoutn.append(lineswithoutns)
    listofstuffwithspaces = []
    for n in justlineswithoutn:
        splitline = n[0].split(" ")
        listofstuffwithspaces.append(splitline)
    unparsedstuff = []
    for line in listofstuffwithspaces:
        unparsedline = []
        for n  in line:
            if n == " " or n == "":
                continue
            else:
                unparsedline.append(n)
        unparsedstuff.append(unparsedline)
    newlines = []
    for line in unparsedstuff:
        lineofwords = []
        for string in line:
            if string.isalpha() == False:
                wordcharacters = []
                for character in string:
                    if character.isalpha():
                        wordcharacters.append(character)
                string = ''.join(wordcharacters)
                string=string.lower()
                lineofwords.append(string)
            else:
                string = string.lower()
                lineofwords.append(string)
        newlines.append(lineofwords)
    newnewlines = []
    for n in newlines:
        lines = []
        for line in n:
            if line == '' or line == ' ':
                continue
            else:
                lines.append(line)
        newnewlines.append(lines)
    return newnewlines

stopfileparsed = parse('stop.txt')
firstfileparsed = parse(firstfile)
secondfileparsed = parse(secondfile)

stopset = set()
for line in stopfileparsed:
    for word in line:
        stopset.add(word)

def removestopwords(parsedlines):
    nostopwordslines = []
    for line in parsedlines:
        newline = []
        for word in line:
            if word in stopset:
                continue
            else:
                newline.append(word)
        nostopwordslines.append(newline)
    return nostopwordslines

nostopwordsfile1 = removestopwords(firstfileparsed)
nostopwordsfile2 = removestopwords(secondfileparsed)

def avgwordlen(file):
    countofwords = 0
    lensofwords = []
    for n in file:
        for word in n:
            countofwords+=1
            x = len(word)
            lensofwords.append(x)
    avgwordlen = sum(lensofwords)/countofwords
    return avgwordlen
avg1 = avgwordlen(nostopwordsfile1)
avg2 = avgwordlen(nostopwordsfile2)

lineofuniquewordsfile1 = set()
count1 = 0
for line in nostopwordsfile1:
    for word in line:
        lineofuniquewordsfile1.add(word)
        count1+=1

uniquewordsratio1 = len(lineofuniquewordsfile1)/count1

lineofuniquewordsfile2 = set()
count2 = 0
for line in nostopwordsfile2:
    for word in line:
        lineofuniquewordsfile2.add(word)
        count2+=1

uniquewordsratio2 = len(lineofuniquewordsfile2)/count2

def wordsoflen(listoflines):
    wordlengths = set()
    for n in  listoflines:
        for word in n:
            x  = len(word)
            wordlengths.add(x)
    wordsofthatlen = []
    for length in wordlengths:
        wordsoflen = []
        for line in listoflines:
            for word in line:
                if len(word) == length:
                    wordsoflen.append(word)
        wordsofthatlen.append(wordsoflen)
    allwords = set()
    for n in wordsofthatlen:
        for word in n:
            allwords.add(word)
    wordsofthatlen2 = []
    for length in wordlengths:
        wordsoflen = []
        for word in allwords:
            if len(word) == length:
                wordsoflen.append(word)
        wordsofthatlen2.append(wordsoflen)
    maxwordlen = max(wordlengths)
    numberofwordsoflengths = []
    for n in range(max(wordlengths)+1):
        x = len(numberofwordsoflengths)
        for words in wordsofthatlen2:
            if len(words[0]) == n:
                numberofwordsoflengths.append(len(words))
        if len(numberofwordsoflengths) == x:
            numberofwordsoflengths.append(0)
    numberofwordsoflengths.pop(0)
    sortedwords = []
    for words in wordsofthatlen2:
        l = words.sort()
        sortedwords.append(l)
    x = 0
    i = 0
    while i < len(numberofwordsoflengths):
        if numberofwordsoflengths[i] == 0:
            print("{0:4}:{1:4}:".format(i+1, numberofwordsoflengths[i]))
        else:
            print("{0:4}:{1:4}:".format(i+1, numberofwordsoflengths[i]),end = "")
            if numberofwordsoflengths[i] != 0:
                if numberofwordsoflengths[i] <=6:
                    string = ''
                    for n in wordsofthatlen2[x]:
                        string+=" " + n
                    print(string)
                    x+=1
                else:
                    string = ''
                    for n in wordsofthatlen2[x][0:3]:
                        string+=" " + n
                    string+=" ..."
                    for n in wordsofthatlen2[x][-3:]:
                        string+=" " + n
                    print(string)
                    x+=1
        i+=1

def wordpairs(lines,maxsep):
    allword = []
    count=0
    for line in lines:
        for word in line:
            allword.append(word)
    tuppy = set()
    for p in range(len(allword)-int(maxsep)):
        for u in range(1,int(maxsep)+1):
            
            if (allword[p+u],allword[p]) not in tuppy:
                tup = (allword[p],allword[p+u])
                tup = tuple(sorted(list(tup)))
                tuppy.add(tup)
            count+=1
            
    for n in range(len(allword)-int(maxsep),len(allword)+1):
        if n == len(allword)-1:
            break
        for u in range(1,int(maxsep)):
            tup =(allword[n],allword[n+u])
            tup = tuple(sorted(list(tup)))
            tuppy.add(tup)
    tuppy = list(tuppy)
    tuppy.sort()
    return tuppy,count
print("")
print("Evaluating document {}".format(firstfile))
print("1. Average word length: {:.2f}".format(avg1))
print("2. Ratio of distinct words to total words: {:.3f}".format(uniquewordsratio1))
print("3. Word sets for document {}:".format(firstfile))
wordsoflen(nostopwordsfile1)
print("4. Word pairs for document {}".format(firstfile))
wordpairs1 = wordpairs(nostopwordsfile1,maxsep)[0]
print("  " + str(len(wordpairs1)) + " distinct pairs")
string = ''
if len(wordpairs1) > 10:
    for tup in wordpairs1[0:5]:
        string+= "  " + tup[0] + " " + tup[1] + "\n"
    string+="  ...\n"
    for tup in wordpairs1[-5:]:
        string+= "  " + tup[0] + " " + tup[1] + "\n"
else:
    for tup in wordpairs1:
        string+= "  " + tup[0] + " " + tup[1] + "\n"
print(string[:-1])
setwordpairs1 = set(wordpairs1)
ratioofwp = len(setwordpairs1)/wordpairs(nostopwordsfile1,maxsep)[1]
print("5. Ratio of distinct word pairs to total: {:.3f}".format(ratioofwp))
print("")
print("Evaluating document {}".format(secondfile))
print("1. Average word length: {:.2f}".format(avg2))
print("2. Ratio of distinct words to total words: {:.3f}".format(uniquewordsratio2))
print("3. Word sets for document {}:".format(secondfile))
wordsoflen(nostopwordsfile2)
print("4. Word pairs for document {}".format(secondfile))
wordpairs2 = wordpairs(nostopwordsfile2,maxsep)[0]
print("  " + str(len(wordpairs2)) + " distinct pairs")
string = ''
if len(wordpairs2) > 10:
    for tup in wordpairs2[0:5]:
        string+= "  " + tup[0] + " " + tup[1] + "\n"
    string+="  ...\n"
    for tup in wordpairs2[-5:]:
        string+= "  " + tup[0] + " " + tup[1] + "\n"
else:
    for tup in wordpairs2:
        string+= "  " + tup[0] + " " + tup[1] + "\n"
print(string[:-1])
setwordpairs2 = set(wordpairs2)
ratioofwp2 = len(wordpairs(nostopwordsfile2,maxsep)[0])/wordpairs(nostopwordsfile2,maxsep)[1]
print("5. Ratio of distinct word pairs to total: {:.3f}".format(ratioofwp2))
print()
print("Summary comparison")
if avg1>avg2:
    print("1. {} on average uses longer words than {}".format(firstfile,secondfile))
else:
    print("1. {} on average uses longer words than {}".format(secondfile,firstfile))


allwordsfile1 = set()
for n in nostopwordsfile1:
    for x in n:
        allwordsfile1.add(x)
allwordsfile2 = set()
for n in nostopwordsfile2:
    for x in n:
        allwordsfile2.add(x)
interofwords = allwordsfile1.intersection(allwordsfile2)
unionwords = allwordsfile1.union(allwordsfile2)
jaccardwords = len(interofwords)/len(unionwords)
print("2. Overall word use similarity: {:.3f}".format(jaccardwords))



setofwordpairsinter = setwordpairs1.intersection(setwordpairs2)
setofwordpairsunion = setwordpairs1.union(setwordpairs2)
jaccardwp = len(setofwordpairsinter)/len(setofwordpairsunion)
print("4. Word pair similarity: {}".format(jaccardwp))

















