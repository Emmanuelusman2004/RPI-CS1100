# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 21:14:55 2022

@author: Emmanuel Usman
"""
def dictionary(file):
    f = open(file,'r')
    d =dict()
    for line in f:
        line = line.strip()
        line = line.split(',')
        d[line[0]] = line[1]
    f.close()
    return d
def keyboard(file):
    file = file.strip("\r")
    f = open(file,'r')
    keyboardsim = dict()
    for line in f:
        line = line.strip()
        line = line.split(" ")
        firstchar = line[0]
        otherchar = line[1:]
        keyboardsim[firstchar[0]] = otherchar
    return keyboardsim
def Sorttuples(listoftuples):
    length = len(listoftuples)
    for i in range(0, length):
         
        for j in range(0, length-i-1):
            if (listoftuples[j][1] > listoftuples[j + 1][1]):
                temp = listoftuples[j]
                listoftuples[j]= listoftuples[j + 1]
                listoftuples[j + 1]= temp
    return listoftuples
    
def filewordreplacer(file,dictionaryfile,keyboardfile):
    f = open(file,'r')
    d = dictionary(dictionaryfile)
    keyboardsim = keyboard(keyboardfile)
    for line in f:
        line = line.strip()
        if line in d:
            print('{:>15} -> FOUND'.format(line))
        else:
#here is where we go through each of the methods
            wordsfound = set()
            lineword = line
#drop
            i = 0
            count = 0
            while i < len(lineword):
                splitword = [x for x in lineword]
                splitword.pop(i)
                splitwordcombined = ''.join(splitword)
                if splitwordcombined in d:
                    count+=1
                    wordsfound.add(splitwordcombined)
#                    print(line+" = " +splitwordcombined + ' found using drop')
                else:
                    splitword = [x for x in lineword]
                i+=1
#insert
            i = 0
            count = 0
            while i < len(lineword)+1:
                splitword = [x for x in lineword]
                alphabet = keyboardsim.keys()
                for value in alphabet:
                    splitword.insert(i,value)
                    splitwordcombined = ''.join(splitword)
                    if splitwordcombined in d:
                        count+=1
                        wordsfound.add(splitwordcombined)
#                        print(line+" = " +splitwordcombined + ' found using insert alphabet')
                    else:
                        splitword = [x for x in lineword]
                i+=1
#swap
            i = 0
            count = 0
            while i < len(lineword):
                indexofchar = i
                indexofnextchar = i+1
                splitword = [x for x in lineword]
                splitword.pop(indexofchar)
                splitword.insert(indexofnextchar,lineword[i])
                splitwordcombined = ''.join(splitword)
#                print(splitwordcombined)
                if splitwordcombined in d:
                    count+=1
                    wordsfound.add(splitwordcombined)
#                    print(line+" = " +splitwordcombined + ' found using swap')
                else:
                    splitword = [x for x in lineword]
                i+=1
                    
#replace with keyboardstuff
            i = 0
            count = 0
            while i < len(lineword):
                splitword = [x for x in lineword]
                characterkey = splitword[i]
                charvalues = keyboardsim.get(characterkey)
#                print(splitword)
#                print(characterkey)
#                print(charvalues)
                for value in charvalues:
                    splitword.pop(i)
                    splitword.insert(i,value)
                    splitwordcombined = ''.join(splitword)
                    if splitwordcombined in d:
                        count+=1
                        wordsfound.add(splitwordcombined)
                    else:
                        splitword = [x for x in lineword]
                i+=1
#            print(line+" = "+ str(wordsfound))
#not found
            if wordsfound == set():
                print('{:>15} -> NOT FOUND'.format(line))
            else:
                wordsfoundnumbers = []
                for word in wordsfound:
                    for key in d:
                        if key == word:
                            wordsfoundnumbers.append((word,d.get(key)))
                wordsfounds = Sorttuples(wordsfoundnumbers)
                stringwordsfound = ''
                for tup in reversed(wordsfounds[-3:]):
                    stringwordsfound+= " " + tup[0]
                print('{0:>15} -> FOUND {1:>2}: {2}'.format(line,len(wordsfound),stringwordsfound))
                            
                
            
dictionaryfile = input("Dictionary file => ").strip()
print(dictionaryfile)
inputfile = input("Input file => ").strip()
print(inputfile)
Keyboardfile = input("Keyboard file => ").strip()
print(Keyboardfile)        

filewordreplacer(inputfile, dictionaryfile,Keyboardfile)