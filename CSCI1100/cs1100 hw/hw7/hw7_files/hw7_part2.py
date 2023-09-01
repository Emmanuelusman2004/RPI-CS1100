# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:55:55 2022

@author: Emmanuel Usman
"""
import json

def getmoviesofyear(minyear,maxyear):
    minyear = int(minyear)
    maxyear = int(maxyear)
    movieswithinyears = []
    for key in movies:
        movieyear = movies[key]['movie_year']
        if movieyear >= minyear and movieyear <= maxyear:
            movieswithinyears.append(key)
    return movieswithinyears

def getcombinedratings(movieswithinyears,w1,w2):
    listofcombratings = []
    for key in movieswithinyears:
        if key in ratings and len(ratings[key]) >= 3:
            imdbrating = movies[key]['rating']
            twitterrating = ratings[key]
            avgtwitterrating = sum(twitterrating)/len(twitterrating)
            combrating = (float(w1) * float(imdbrating) + float(w2) * float(avgtwitterrating)) / (float(w1) + float(w2))
            tuppy = (combrating,key)
            listofcombratings.append(tuppy)
    return listofcombratings

def genre(listofcombratings,genre,date1,date2):
    moviesofgenre = []
    for tup in listofcombratings:
#        print(tup)
        key = tup[1]
#        print(key)
        genreofkey = movies[key]['genre']
#        print(genreofkey)
        genrepp = []
        for string in genreofkey:
            string = string.lower()
            genrepp.append(string)
        if genre in genrepp:
#            print(tup)
            moviesofgenre.append(tup)
    moviesofgenre = sorted(moviesofgenre)
#    print(moviesofgenre)
#    print(moviesofgenre)
#    greatest,least
    if moviesofgenre == []:
        print('No {} movie found in {} through {}'.format(genre.title(),date1,date2))
        print("")
        return None
    return (moviesofgenre[-1],moviesofgenre[0])
    
def getinfoonmovies(tup):
    bestmoviekey = tup[0][1]
    worstmoviekey = tup[1][1]
    bestmoviename = movies[bestmoviekey]['name']
    worstmoviename = movies[worstmoviekey]['name']
    bestmoviedate = movies[bestmoviekey]['movie_year']
    worstmoviedate = movies[worstmoviekey]['movie_year']
    bestmovierating = tup[0][0]
    worstmovierating = tup[1][0]
    print("Best:")
    print('        Released in {}, {} has a rating of {:.2f}\n'.format(bestmoviedate,bestmoviename,bestmovierating))
    print('Worst:')
    print('        Released in {}, {} has a rating of {:.2f}\n'.format(worstmoviedate,worstmoviename,worstmovierating))






minyear = input("Min year => ").strip()
print(minyear)
maxyear = input("Max year => ").strip()
print(maxyear)
wimdb = input("Weight for IMDB => ").strip()
print(wimdb)
wtwitter = input("Weight for Twitter => ").strip()
print(wtwitter)
print("")

movies = json.loads(open("movies.json").read())
ratings = json.loads(open("ratings.json").read())
i = 0
while i != 1:
    genres = input("What genre do you want to see? ").strip()
    print(genres)
    genres = genres.lower()
    if genres == 'stop':
        break
    print("")
    movieswithinyears = getmoviesofyear(minyear, maxyear)
#print(movieswithinyears)
#print("")
    listofcombratings = getcombinedratings(movieswithinyears, wimdb, wtwitter)
#print(listofcombratings)
#print("")
    genremovies = genre(listofcombratings,genres,minyear,maxyear)
    if genremovies == None:
        continue
   #print(genremovies)
    getinfoonmovies(genremovies)
    