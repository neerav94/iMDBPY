from imdb import IMDb
ia = IMDb()
name = input("Name of the movie you want to search? ")
for movie in ia.search_movie(name):
	
	print movie.movieID, movie['title'], movie['year']
id_movie=input(" \n enter the id of the movie you want to have data of  ")

inter = ia.get_movie(id_movie)

print "Year  : ", inter['year']

print "Genre : ",inter['genre']

print "Director : "
for dir in inter['director']:
	print "    ",dir

print "Producer : "

for pro in inter['producer']:
	print "    ",pro

print "Casting Director : "
for ca in inter['casting director']:
	print "    ",ca

print "rating  :", inter['rating']


#print " Plot : "
#for pl in inter['original music']:
#	print "   " , inter['pl']

	
