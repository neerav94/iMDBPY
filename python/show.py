#!/usr/bin/python
import MySQLdb as mdb
import Tkinter
import sys
from imdb import IMDb
win = Tkinter.Tk()
ia = IMDb()
global call
Movie=[]
Tv_Show=[]
Person=[]
global row
row=[]
# Open database connection
db = mdb.connect("localhost","amogh","2014","PYMDb" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
def Movie():
 var=raw_input("enter movie name  ")
 if(cursor.execute ("""select * from Movie where Title=%s""",var)):
# fetch all of the rows from the query
  data = cursor.fetchall ()
# print the rows
  for row in data :
   print "Title--",row[1] 
   print "Movie_id--",row[0]
   print "Genre--",row[2] 
   print "Director--",row[3]
   print "Writer--",row[4]
   print "Cast--",row[5]
   print "Runtime--",row[6]
   print "Country--",row[7]
   print "Language--",row[8]
   print "Rating--",row[9]
   print "Plot--",row[10]
   print "\n Thank you! " 
 else :
   print "Record Not Found In The Database.\n"	

#SQL query to INSERT a record into the table.
   print "\nSearching Online...Please Wait! "
   for movie in ia.search_movie(var):
	print movie.movieID, movie['title']
	
   id_movie=raw_input("\n enter the id of the movie you want to have data of-- ")
   inter = ia.get_movie(id_movie)
   title_m=genre_m=director_m=writer_m=cast_m=runtimes_m=countries_m=languages_m=rating_m=plot_m=" "


   title_m=str(inter['title']) 
   print "Title--",title_m
   for genre in inter['genre']:
    genre_m=genre_m+str(genre)
    genre_m=genre_m+"," 
   print "Genre--",genre_m
   for director in inter['director']:
     director_m=director_m+str(director)
     director_m=director_m+","
   print "Director--",director_m
   for writer in inter['writer']:
     writer_m=writer_m+str(writer)
     writer_m=writer_m+","
   print "Writer--",writer_m
   for cast in inter['cast']:
    cast_m=cast_m+str(cast)
    cast_m=cast_m+","
   print "Cast--",cast_m
   for runtimes in inter['runtimes']:
    runtimes_m=runtimes_m+str(runtimes)
    runtimes_m=runtimes_m+","
   print "Runtime--",runtimes_m
   for countries in inter['countries']:
    countries_m=countries_m+str(countries)
    countries_m=countries_m+","  
   print "Countries--",countries_m
   for languages in inter['languages']:
     languages_m=languages_m+str(languages)
     languages_m=languages_m+","
   print "Languages--",languages_m  
   rating_m=inter['rating']
   print "Rating--",rating_m
   for plot in inter['plot']:
    plot_m=plot_m+str(plot)
   print "Plot--",plot_m
   print "\nPopulating"
   cursor.execute("""INSERT INTO Movie(Movie_id,Title,Genre,Director,Writer,Cast,Runtime,Country,Language,Rating,Plot)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""" ,(id_movie,title_m,genre_m,director_m,writer_m,cast_m,runtimes_m,countries_m,languages_m,rating_m,plot_m))

   
   print "Done!!"
   db.commit()
# disconnect from server 
   db.close()

def Tv_Show():
 var=raw_input("enter name of the Tv Show or Episode Name-- ")
 if(cursor.execute ("""select * from Tv_Show where Title=%s""",var)):
# fetch all of the rows from the query
  data = cursor.fetchall ()
# print the rows
  for row in data :
   print "Title--",row[1] 
   print "Show_id--",row[0]
   print "Genre--",row[2] 
   print "Director--",row[3]
   print "Writer--",row[4]
   print "Cast--",row[5]
   print "Runtime--",row[6]
   print "Country--",row[7]
   print "Language--",row[8]
   print "Rating--",row[9]
   print "Plot--",row[10]
   print "\n Thank you! " 
 else :
   print "Record Not Found In The Database.\n"	

#SQL query to INSERT a record into the table.
   print "\nSearching Online...Please Wait! "
   for movie in ia.search_movie(var):
	print movie.movieID, movie['title']
	
   id_movie=raw_input("\n enter the id of the Tv Show / Episode you want to have data of-- ")
   inter = ia.get_movie(id_movie)
   title_m=genre_m=director_m=writer_m=cast_m=runtimes_m=countries_m=languages_m=rating_m=plot_m=" "


   title_m=str(inter['title']) 
   print "Title--",title_m
   
   for genre in inter['genre']:
     genre_m=genre_m+str(genre)
     genre_m=genre_m+"," 
   print "Genre--",genre_m
   
   for director in inter['director']:
     director_m=director_m+str(director)
     director_m=director_m+","
   print "Director--",director_m
   for cast in inter['cast']:
    cast_m=cast_m+str(cast)
    cast_m=cast_m+","
   print "Cast--",cast_m
   for runtimes in inter['runtimes']:
    runtimes_m=runtimes_m+str(runtimes)
    runtimes_m=runtimes_m+","
   print "Runtime--",runtimes_m
   for countries in inter['countries']:
    countries_m=countries_m+str(countries)
    countries_m=countries_m+","  
   print "Countries--",countries_m
   for languages in inter['languages']:
     languages_m=languages_m+str(languages)
     languages_m=languages_m+","
   print "Languages--",languages_m  
   rating_m=inter['rating']
   print "Rating--",rating_m
   for plot in inter['plot']:
    plot_m=plot_m+str(plot)
   print "Plot--",plot_m
   print "\nPopulating"
   cursor.execute("""INSERT INTO Tv_Show(Show_id,Title,Genre,Director,Writer,Cast,Runtime,Country,Language,Rating,Plot)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""" ,(id_movie,title_m,genre_m,director_m,writer_m,cast_m,runtimes_m,countries_m,languages_m,rating_m,plot_m))

   
   print "Done!!"
   db.commit()
  #disconnect from server 
   db.close()
 
def Person():
 name_p=dob_p=bn_p=bio_p=""
 var=raw_input("enter name of the Person/Director/Actor/Actress etc-- ")
 if(cursor.execute ("""select * from Person where Name=%s""",var)):
# fetch all of the rows from the query
  dataa = cursor.fetchall ()
# print the rows
  for row in dataa :
   print "Name--",row[1] 
   print "Person_id--",row[0]
   print "Birth Date--",row[2] 
   print "Birth Note--",row[3]
   print "Biography--",row[4]
   print "\n Thank you! " 
 else :
   print "Record Not Found In The Database.\n"	

#SQL query to INSERT a record into the table.
   print "\nSearching Online...Please Wait! "
   #name=raw_input("name of the person required to be searched --")
   for celeb in ia.search_person(var):
	print celeb," ",celeb.personID
   id_person=raw_input("enter id--")
   inter=ia.get_person(id_person)
   print "Name  :",inter['name']
   name_p=str(inter['name'])
   print "Year of Birth  :",inter['birth date']
   dob_p=str(inter['birth date'])
   print "birth place :", inter['birth notes']
   bn_p=str(inter['birth notes'])
   print "Biography  :",inter['mini biography']
   bio_p=str(inter['mini biography'])
   print "\n Populating"
   cursor.execute("""INSERT INTO Person(Person_id,Name,Birth_Date,Birth_Note,Biography)VALUES(%s,%s,%s,%s,%s);""" ,(id_person,name_p,dob_p,bn_p,bio_p))
   print "Done!"
   db.commit()
  #disconnect from server 
   db.close()
b1=Tkinter.Button(win,text="Next",command=Person)
b1.pack()
win.mainloop()
