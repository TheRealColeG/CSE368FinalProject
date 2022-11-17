import math
import numpy as np

class User:

    def __init__(self, id, age, gender, occupation, zipcode):
        self.id = id
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.zipcode = zipcode
        self.ratings = list() #Will be filled in later on

class Movie:

    def __init__(self, id, title, releaseDate, genres):
        self.id = id
        self.title = title
        self.releaseDate = releaseDate
        self.genres = genres
        self.ratings = list() #Will be filled in later on
    
    #Use this when creating the object for its genre
    
    def getGenre(entireLine):
        possibleGenres = ["Unknown","Action","Adventure","Animation","Children's","Comedy","Crime","Documentary","Drama","Fantasy","Film-Noir","Horror","Musical","Mystery","Romance","Sci-Fi","Thriller","War","Western"]
        halves = entireLine.split("||")
        fields = halves[1].split("|")
        fields.pop(0)
        genres = []
        for index in range(len(fields)):
            if fields[index].strip() == "1":
                genres.append(possibleGenres[index])
        return genres

class Rating:
    def __init__(self, userID, movieID, rating):
        self.userID = userID
        self.movieID = movieID
        self.rating = rating

def initializeMovies():

    MovieBase = {} #List of Movie objects
    with open("u.item") as file:
        allLines = file.readlines()
        for line in allLines:

            fields = line.split("|")
            id = int(fields[0].strip())
            title = fields[1].strip()
            releaseDate = fields[2].strip()
            genres = Movie.getGenre(line)

            newMovie = Movie(id,title,releaseDate,genres)
            MovieBase[id] = newMovie
            
    return MovieBase

def initializeUsers():

    UserBase = {} #List of User objects
    with open("u.user") as file:
        #May have to .strip() for \n
        allLines = file.readlines()
        for line in allLines:

            fields = line.split("|")
            id = int(fields[0].strip())
            age = int(fields[1].strip())
            gender = fields[2].strip()
            occupation = fields[3].strip()
            zip = fields[4].strip()

            newUser = User(id, age, gender, occupation, zip)
            UserBase[id] = newUser

    return UserBase

def initializeRatings(movieBase, userBase):
    #In reality, no actual ratingBase is needed since the values will be added to the user/movie bases but just in case they are I'm going to make a base for them
    #Let's be real, is anyone strapped for memory in such a low level application such as this?
    RatingBase = []
    with open("u.data") as file:
        allLines = file.readlines()
        for line in allLines:

            fields = line.split()
            userID = int(fields[0].strip())
            movieID = int(fields[1].strip())
            rating = int(fields[2].strip())

            newRating = Rating(userID, movieID, rating)

            movieBase[movieID].ratings.append(newRating)
            userBase[userID].ratings.append(newRating)

            RatingBase.append(newRating)
    
    return RatingBase

def getUsers():
    with open("u.user") as file:
        allLines = file.readlines()
        for line in allLines:
            fields = line.split("|")
            print("ID:",fields[0],"AGE:",fields[1],"GENDER:",fields[2],"OCCUPATION:",fields[3],"ZIP:",fields[4])

if __name__ == "__main__":
    movieBase = initializeMovies()
    for movie in movieBase.keys():
        print(movieBase[movie].genres)
    
    userBase = initializeUsers()
    for user in userBase.keys():
        print(userBase[user].zipcode)

    ratingBase = initializeRatings(movieBase, userBase)
    print(ratingBase)

