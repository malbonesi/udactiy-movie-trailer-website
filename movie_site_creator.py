import mopic
import fresh_tomatoes

movies = []

f = open('./movies.txt', 'r')

#Populate movies list from txt file
for line in f:
    movies.append(mopic.Movie(*line.split(',')))

f.close()

#Create template and open from browser
fresh_tomatoes.open_movies_page(movies)
