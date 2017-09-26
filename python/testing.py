#!/usr/bin/python
import MySQLdb as mdb
import Tkinter
import sys
from imdb import IMDb
win = Tkinter.Tk()
win.title("PYMDb")
ia = IMDb()

global root
root=[]
global Call
Call=[]
Movie=[]
global row
row=[]
global top
top=[]
global v4
v4=Tkinter.IntVar()
# Open database connection
db = mdb.connect("localhost","amogh","2014","PYMDb" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

#movie function
def Movie():
 global var
 global v1
 global root
 root=[]
 var=v1.get()
 #var=input("enter movie name  ")
 if(cursor.execute ("""select * from Movie where Title=%s""",var)):
# fetch all of the rows from the query
  top = Tkinter.Tk()
  top.title("PYMDb")
  frame1 = Tkinter.Frame(top)
  frame1.pack()
  frame2 = Tkinter.Frame(top)
  frame2.pack()
  frame3 = Tkinter.Frame(top)
  frame3.pack( )
  frame4 = Tkinter.Frame(top)
  frame4.pack( side = "bottom" )
  
  data = cursor.fetchall ()
# print the rows
  for row in data :
   l4 = Tkinter.Label(frame1,text="Title :")
   l4.grid(row=0,column=0)
   l4 = Tkinter.Label(frame1,text=row[1])
   l4.grid(row=0,column=1)
  
   l5 = Tkinter.Label(frame1,text="Movie_id :")
   l5.grid(row=1,column=0)
   l5 = Tkinter.Label(frame1,text=row[0])
   l5.grid(row=1,column=1)

   l6 = Tkinter.Label(frame1,text="Genre :")
   l6.grid(row=2,column=0)
   l6 = Tkinter.Label(frame1,text=row[2])
   l6.grid(row=2,column=1)

   l7 = Tkinter.Label(frame1,text="Director :")
   l7.grid(row=3,column=0)
   l7 = Tkinter.Label(frame1,text=row[3])
   l7.grid(row=3,column=1)

   l8 = Tkinter.Label(frame1,text="Writer :")
   l8.grid(row=4,column=0)
   l8 = Tkinter.Label(frame1,text=row[4])
   l8.grid(row=4,column=1)

   l9 = Tkinter.Label(frame1,text="Runtime :")
   l9.grid(row=5,column=0)
   l9 = Tkinter.Label(frame1,text=row[6])
   l9.grid(row=5,column=1)

   l10 = Tkinter.Label(frame1,text="Country :")
   l10.grid(row=7,column=0)
   l10 = Tkinter.Label(frame1,text=row[7])
   l10.grid(row=7,column=1)

   l11 = Tkinter.Label(frame1,text="Language :")
   l11.grid(row=8,column=0)
   l11 = Tkinter.Label(frame1,text=row[8])
   l11.grid(row=8,column=1)
   
   l12 = Tkinter.Label(frame1,text="Rating :")
   l12.grid(row=9,column=0)
   l12 = Tkinter.Label(frame1,text=row[9])
   l12.grid(row=9,column=1)
   
   sb2 = Tkinter.Scrollbar(frame2)
   sb2.pack( side = "right", fill="y" )
   text1 = Tkinter.Text(frame2,yscrollcommand = sb2.set,height=5)
   l13 = Tkinter.Label(frame2,text="Cast :").pack()
   text1.insert('insert',row[5])
   text1.pack()
   sb2.config( command = text1.yview )

   sb1 = Tkinter.Scrollbar(frame3)
   sb1.pack( side = "right", fill="y" )
   text2 = Tkinter.Text(frame3,yscrollcommand = sb1.set)
   l14 = Tkinter.Label(frame3,text="Plot :").pack()
   text2.insert('insert',row[10])
   text2.pack()
   sb1.config( command = text2.yview )

   l15 = Tkinter.Label(frame4,text="Thank You! ")
   l15.pack()

 else :
   global v4
   root = Tkinter.Tk()
   root.title("PYMDb")
   l16 = Tkinter.Label(root,text="Record Not Found In The Database.")
   l16.grid(row=0,column=0)
   
#SQL query to INSERT a record into the table.
   l17 = Tkinter.Label(root,text="Online Results..")
   l17.grid(row=3,column=0)
   #root1=Tkinter.Tk()
   #print "\nSearching Online...Please Wait! "
   lb18 = Tkinter.Listbox(root, height = 30,width = 40)
   for movie in ia.search_movie(var):
	#print movie.movieID, movie['title']
	lb18.insert("end",(movie.movieID, movie['title'], movie['year']))
   lb18.grid(row=4,column=0)
   #root.destroy()
   l20 = Tkinter.Label(win,text="Enter the Movie id :").pack() #Creating Label
   #v = Tkinter.StringVar() 
   e4 = Tkinter.Entry(win,textvariable=v4)
   e4.pack() 
   b4=Tkinter.Button(win,text="Next",command=mov)
   b4.pack()
   
def mov():
   top = Tkinter.Tk()
   top.title("PYMDb")
   frame1 = Tkinter.Frame(top)
   frame1.pack()
   frame2 = Tkinter.Frame(top)
   frame2.pack()
   frame3 = Tkinter.Frame(top)
   frame3.pack( )
   frame4 = Tkinter.Frame(top)
   frame4.pack( side = "bottom" )

   #num = v4.get()
   #print num
   id_movie = v4.get()
   #id_movie=raw_input("\n enter the id of the movie you want to have data of-- ")
   inter = ia.get_movie(id_movie)
   title_m=genre_m=director_m=writer_m=cast_m=runtimes_m=countries_m=languages_m=rating_m=plot_m=" "
   root.destroy()
   
   title_m=str(inter['title']) 
   l4 = Tkinter.Label(frame1,text="Title :")
   l4.grid(row=0,column=0)
   l4 = Tkinter.Label(frame1,text=title_m)
   l4.grid(row=0,column=1)

   #print "Title--",title_m
   for genre in inter['genre']:
    genre_m=genre_m+str(genre)
    genre_m=genre_m+"," 
   l5 = Tkinter.Label(frame1,text="Genre :")
   l5.grid(row=1,column=0)
   l5 = Tkinter.Label(frame1,text=genre_m)
   l5.grid(row=1,column=1)
   #print "Genre--",genre_m
   for director in inter['director']:
     director_m=director_m+str(director_m)
     director_m=director_m+","
   l7 = Tkinter.Label(frame1,text="Director :")
   l7.grid(row=3,column=0)
   l7 = Tkinter.Label(frame1,text=director_m)
   l7.grid(row=3,column=1)
   
   for writer in inter['writer']:
     writer_m=writer_m+str(writer)
     writer_m=writer_m+","
   l8 = Tkinter.Label(frame1,text="Writer :")
   l8.grid(row=4,column=0)
   l8 = Tkinter.Label(frame1,text=writer_m)
   l8.grid(row=4,column=1)

   #print "Director--",director_m
   for cast in inter['cast']:
    cast_m=cast_m+str(cast)
    cast_m=cast_m+","
   sb2 = Tkinter.Scrollbar(frame2)
   sb2.pack( side = "right", fill="y" )
   text1 = Tkinter.Text(frame2,yscrollcommand = sb2.set,height=5)
   l13 = Tkinter.Label(frame2,text="Cast :").pack()
   text1.insert('insert',cast_m)
   text1.pack()
   sb2.config( command = text1.yview )
   #print "Cast--",cast_m
   for runtimes in inter['runtimes']:
    runtimes_m=runtimes_m+str(runtimes)
    runtimes_m=runtimes_m+","
   l9 = Tkinter.Label(frame1,text="Runtime :")
   l9.grid(row=5,column=0)
   l9 = Tkinter.Label(frame1,text=runtimes_m)
   l9.grid(row=5,column=1)

   #print "Runtime--",runtimes_m
   for countries in inter['countries']:
    countries_m=countries_m+str(countries)
    countries_m=countries_m+","  
   l10 = Tkinter.Label(frame1,text="Country :")
   l10.grid(row=7,column=0)
   l10 = Tkinter.Label(frame1,text=countries_m)
   l10.grid(row=7,column=1)

   #print "Countries--",countries_m
   for languages in inter['languages']:
     languages_m=languages_m+str(languages)
     languages_m=languages_m+","
   
   l11 = Tkinter.Label(frame1,text="Language :")
   l11.grid(row=8,column=0)
   l11 = Tkinter.Label(frame1,text=languages_m)
   l11.grid(row=8,column=1)
   #print "Languages--",languages_m  
   rating_m=inter['rating']
   l12 = Tkinter.Label(frame1,text="Rating :")
   l12.grid(row=9,column=0)
   l12 = Tkinter.Label(frame1,text=rating_m)
   l12.grid(row=9,column=1)
   #print "Rating--",rating_m
   for plot in inter['plot']:
    plot_m=plot_m+str(plot)
   sb1 = Tkinter.Scrollbar(frame3)
   sb1.pack( side = "right", fill="y" )
   text2 = Tkinter.Text(frame3,yscrollcommand = sb1.set)
   l14 = Tkinter.Label(frame3,text="Plot :").pack()
   text2.insert('insert',plot_m)
   text2.pack()
   sb1.config( command = text2.yview )

   #print "Plot--",plot_m
   l15 = Tkinter.Label(frame4,text="Populating...")
   l15.pack()
   #print "\nPopulating"
   cursor.execute("""INSERT INTO Movie(Movie_id,Title,Genre,Director,Writer,Cast,Runtime,Country,Language,Rating,Plot)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""" ,(id_movie,title_m,genre_m,director_m,writer_m,cast_m,runtimes_m,countries_m,languages_m,rating_m,plot_m))

   l15 = Tkinter.Label(frame4,text="Done! ")
   l15.pack()
   #print "Done!!"
   db.commit()
# disconnect from server 
   db.close()
'''def ca():
 temp = v4.get()
 print temp'''
def Tv_Show():
 
 global var
 global v2
 global root
 root=[]
 var=v2.get()
 #var=input("enter movie name  ")
 if(cursor.execute ("""select * from Tv_Show where Title=%s""",var)):
# fetch all of the rows from the query
  top = Tkinter.Tk()
  top.title("PYMDb")
  frame1 = Tkinter.Frame(top)
  frame1.pack()
  frame2 = Tkinter.Frame(top)
  frame2.pack()
  frame3 = Tkinter.Frame(top)
  frame3.pack( )
  frame4 = Tkinter.Frame(top)
  frame4.pack( side = "bottom" )
  
  data = cursor.fetchall ()
# print the rows
  for row in data :
   l4 = Tkinter.Label(frame1,text="Title :")
   l4.grid(row=0,column=0)
   l4 = Tkinter.Label(frame1,text=row[1])
   l4.grid(row=0,column=1)
  
   l5 = Tkinter.Label(frame1,text="Show_id :")
   l5.grid(row=1,column=0)
   l5 = Tkinter.Label(frame1,text=row[0])
   l5.grid(row=1,column=1)

   l6 = Tkinter.Label(frame1,text="Genre :")
   l6.grid(row=2,column=0)
   l6 = Tkinter.Label(frame1,text=row[2])
   l6.grid(row=2,column=1)

   l7 = Tkinter.Label(frame1,text="Director :")
   l7.grid(row=3,column=0)
   l7 = Tkinter.Label(frame1,text=row[3])
   l7.grid(row=3,column=1)

   l8 = Tkinter.Label(frame1,text="Writer :")
   l8.grid(row=4,column=0)
   l8 = Tkinter.Label(frame1,text=row[4])
   l8.grid(row=4,column=1)

   l9 = Tkinter.Label(frame1,text="Runtime :")
   l9.grid(row=5,column=0)
   l9 = Tkinter.Label(frame1,text=row[6])
   l9.grid(row=5,column=1)

   l10 = Tkinter.Label(frame1,text="Country :")
   l10.grid(row=7,column=0)
   l10 = Tkinter.Label(frame1,text=row[7])
   l10.grid(row=7,column=1)

   l11 = Tkinter.Label(frame1,text="Language :")
   l11.grid(row=8,column=0)
   l11 = Tkinter.Label(frame1,text=row[8])
   l11.grid(row=8,column=1)
   
   l12 = Tkinter.Label(frame1,text="Rating :")
   l12.grid(row=9,column=0)
   l12 = Tkinter.Label(frame1,text=row[9])
   l12.grid(row=9,column=1)
   
   sb2 = Tkinter.Scrollbar(frame2)
   sb2.pack( side = "right", fill="y" )
   text1 = Tkinter.Text(frame2,yscrollcommand = sb2.set,height=5)
   l13 = Tkinter.Label(frame2,text="Cast :").pack()
   text1.insert('insert',row[5])
   text1.pack()
   sb2.config( command = text1.yview )

   sb1 = Tkinter.Scrollbar(frame3)
   sb1.pack( side = "right", fill="y" )
   text2 = Tkinter.Text(frame3,yscrollcommand = sb1.set)
   l14 = Tkinter.Label(frame3,text="Plot :").pack()
   text2.insert('insert',row[10])
   text2.pack()
   sb1.config( command = text2.yview )

   l15 = Tkinter.Label(frame4,text="Thank You! ")
   l15.pack()
 

 else :
   global v4
   root = Tkinter.Tk()
   root.title("PYMDb")
   l16 = Tkinter.Label(root,text="Record Not Found In The Database.")
   l16.grid(row=0,column=0)
   
#SQL query to INSERT a record into the table.
   l17 = Tkinter.Label(root,text="Online Results..")
   l17.grid(row=3,column=0)
   #root1=Tkinter.Tk()
   #print "\nSearching Online...Please Wait! "
   lb18 = Tkinter.Listbox(root, height = 30,width = 40)
   for movie in ia.search_movie(var):
	#print movie.movieID, movie['title']
	lb18.insert("end",(movie.movieID, movie['title'], movie['year']))
   lb18.grid(row=4,column=0)
   #root.destroy()

   
#SQL query to INSERT a record into the table.
   l20 = Tkinter.Label(win,text="Enter the TV SHOW id :").pack() #Creating Label
   #v = Tkinter.StringVar() 
   e4 = Tkinter.Entry(win,textvariable=v4)
   e4.pack() 
   b4=Tkinter.Button(win,text="Next",command=tv)
   b4.pack()
def tv():
   top = Tkinter.Tk()
   top.title("PYMDb")
   frame1 = Tkinter.Frame(top)
   frame1.pack()
   frame2 = Tkinter.Frame(top)
   frame2.pack()
   frame3 = Tkinter.Frame(top)
   frame3.pack( )
   frame4 = Tkinter.Frame(top)
   frame4.pack( )
   frame5 = Tkinter.Frame(top)
   frame5.pack( )
   frame6 = Tkinter.Frame(top)
   frame6.pack( side = "bottom" )	

   id_movie = v4.get()
   #id_movie=raw_input("\n enter the id of the Tv Show / Episode you want to have data of-- ")
   inter = ia.get_movie(id_movie)
   title_m=genre_m=director_m=writer_m=cast_m=runtimes_m=countries_m=languages_m=rating_m=plot_m=" "
  
   root.destroy()
   
   title_m=str(inter['title']) 
   l4 = Tkinter.Label(frame1,text="Title :")
   l4.grid(row=0,column=0)
   l4 = Tkinter.Label(frame1,text=title_m)
   l4.grid(row=0,column=1)

   #print "Title--",title_m
   for genre in inter['genre']:
     genre_m=genre_m+str(genre)
     genre_m=genre_m+"," 
   l5 = Tkinter.Label(frame1,text="Genre :")
   l5.grid(row=1,column=0)
   l5 = Tkinter.Label(frame1,text=genre_m)
   l5.grid(row=1,column=1)
   #print "Genre--",genre_m
   for director in inter['director']:
     director_m=director_m+str(director)
     director_m=director_m+","
   sb2 = Tkinter.Scrollbar(frame2)
   sb2.pack( side = "right", fill="y" )
   text4 = Tkinter.Text(frame2,yscrollcommand = sb2.set,height=5)
   l14 = Tkinter.Label(frame2,text="Director :").pack(side = "left")
   text4.insert('insert',director_m)
   text4.pack(side = "left")
   sb2.config( command = text4.yview )

   for writer in inter['writer']:
     writer_m=writer_m+str(writer)
     writer_m=writer_m+","
   sb3 = Tkinter.Scrollbar(frame3)
   sb2.pack( side = "right", fill="y" )
   text5 = Tkinter.Text(frame3,yscrollcommand = sb3.set,height=5)
   l14 = Tkinter.Label(frame3,text="Writer :").pack(side = "left")
   text5.insert('insert',writer_m)
   text5.pack(side = "left")
   sb3.config( command = text5.yview )

   for cast in inter['cast']:
    cast_m=cast_m+str(cast)
    cast_m=cast_m+","
   sb4 = Tkinter.Scrollbar(frame4)
   sb4.pack( side = "right", fill="y" )
   text1 = Tkinter.Text(frame4,yscrollcommand = sb4.set,height=5)
   l13 = Tkinter.Label(frame4,text="Cast :").pack(side = "left")
   text1.insert('insert',cast_m)
   text1.pack(side = "left")
   sb4.config( command = text1.yview )
   #print "Cast--",cast_m
   
   for runtimes in inter['runtimes']:
    runtimes_m=runtimes_m+str(runtimes)
    runtimes_m=runtimes_m+","
   l9 = Tkinter.Label(frame1,text="Runtime :")
   l9.grid(row=5,column=0)
   l9 = Tkinter.Label(frame1,text=runtimes_m)
   l9.grid(row=5,column=1)

   for countries in inter['countries']:
    countries_m=countries_m+str(countries)
    countries_m=countries_m+","  
   l10 = Tkinter.Label(frame1,text="Country :")
   l10.grid(row=7,column=0)
   l10 = Tkinter.Label(frame1,text=countries_m)
   l10.grid(row=7,column=1)

   #print "Countries--",countries_m
   for languages in inter['languages']:
     languages_m=languages_m+str(languages)
     languages_m=languages_m+","
   l11 = Tkinter.Label(frame1,text="Language :")
   l11.grid(row=8,column=0)
   l11 = Tkinter.Label(frame1,text=languages_m)
   l11.grid(row=8,column=1)
   #print "Languages--",languages_m  
   
   rating_m=inter['rating']
   l12 = Tkinter.Label(frame1,text="Rating :")
   l12.grid(row=9,column=0)
   l12 = Tkinter.Label(frame1,text=rating_m)
   l12.grid(row=9,column=1)
   #print "Rating--",rating_m
   for plot in inter['plot']:
    plot_m=plot_m+str(plot)
   sb5 = Tkinter.Scrollbar(frame5)
   sb5.pack( side = "right", fill="y" )
   text2 = Tkinter.Text(frame5,yscrollcommand = sb5.set,height=10)
   l14 = Tkinter.Label(frame5,text="Plot :").pack(side = "left")
   text2.insert('insert',plot_m)
   text2.pack(side = "left")
   sb5.config( command = text2.yview )

   #print "Plot--",plot_m
   l15 = Tkinter.Label(frame6,text="Populating...")
   l15.pack()
   #print "\nPopulating"
   cursor.execute("""INSERT INTO Tv_Show(Show_id,Title,Genre,Director,Writer,Cast,Runtime,Country,Language,Rating,Plot)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""" ,(id_movie,title_m,genre_m,director_m,writer_m,cast_m,runtimes_m,countries_m,languages_m,rating_m,plot_m))

   l15 = Tkinter.Label(frame6,text="Done! ")
   l15.pack()
   
   db.commit()
# disconnect from server 
   db.close()
 
def Person():
 
 global var
 global root
 root=[]
 global v3
 var=v3.get()
 #print var
 #var=input("enter movie name  ")
 if(cursor.execute ("""select * from Person where Name=%s""",var)):
  # fetch all of the rows from the query
  top = Tkinter.Tk()
  top.title("PYMDb")
  frame1 = Tkinter.Frame(top)
  frame1.pack()
  frame2 = Tkinter.Frame(top)
  frame2.pack()
  frame3 = Tkinter.Frame(top)
  frame3.pack(side = "bottom" )
  
  data = cursor.fetchall ()
  # print the rows
  for row in data :
   l4 = Tkinter.Label(frame1,text="Name :")
   l4.grid(row=0,column=0)
   l4 = Tkinter.Label(frame1,text=row[1])
   l4.grid(row=0,column=1)
  
   l5 = Tkinter.Label(frame1,text="Person_id :")
   l5.grid(row=1,column=0)
   l5 = Tkinter.Label(frame1,text=row[0])
   l5.grid(row=1,column=1)

   l6 = Tkinter.Label(frame1,text="Birth Date :")
   l6.grid(row=2,column=0)
   l6 = Tkinter.Label(frame1,text=row[2])
   l6.grid(row=2,column=1)

   l7 = Tkinter.Label(frame1,text="Birth Place :")
   l7.grid(row=3,column=0)
   l7 = Tkinter.Label(frame1,text=row[3])
   l7.grid(row=3,column=1)

      
   sb2 = Tkinter.Scrollbar(frame2)
   sb2.pack( side = "right", fill="y" )
   text1 = Tkinter.Text(frame2,yscrollcommand = sb2.set,height=8)
   l13 = Tkinter.Label(frame2,text="Biography :").pack()
   text1.insert('insert',row[4])
   text1.pack()
   sb2.config( command = text1.yview )

   l15 = Tkinter.Label(frame3,text="Thank You! ")
   l15.pack()
# print the rows

 else :
   root = Tkinter.Tk()
   root.title("PYMDb")
   l16 = Tkinter.Label(root,text="Record Not Found In The Database.")
   l16.grid(row=0,column=0)
   l17 = Tkinter.Label(root,text="Online Results..")
   l17.grid(row=3,column=0)	
   lb18 = Tkinter.Listbox(root, height = 30,width = 40)
   for celeb in ia.search_person(var):
      lb18.insert("end",(celeb,"  ",celeb.personID))
   lb18.grid(row=4,column=0)
   l20 = Tkinter.Label(win,text="Enter the TV SHOW id :").pack() #Creating Label
   #v = Tkinter.StringVar() 
   e4 = Tkinter.Entry(win,textvariable=v4)
   e4.pack() 
   b4=Tkinter.Button(win,text="Next",command=pers)
   b4.pack()
   #root.destroy()
def pers():
   name_p=dob_p=bn_p=bio_p=""
   #var=v3.get()
   #print var
   top = Tkinter.Tk()
   top.title("PYMDb")
   frame1 = Tkinter.Frame(top)
   frame1.pack()
   frame2 = Tkinter.Frame(top)
   frame2.pack()
   frame3 = Tkinter.Frame(top)
   frame3.pack(side = "bottom" )
   id_person = v4.get()
   root.destroy
   #id_person=raw_input("enter id--")
   inter=ia.get_person(id_person)
   #print "Name  :",inter['name']
   name_p=str(inter['name'])
   l4 = Tkinter.Label(frame1,text="Name :")
   l4.grid(row=0,column=0)
   l4 = Tkinter.Label(frame1,text=name_p)
   l4.grid(row=0,column=1)
  
   #print "Year of Birth  :",inter['birth date']
   
   dob_p=str(inter['birth date'])
   l6 = Tkinter.Label(frame1,text="Birth Date :")
   l6.grid(row=2,column=0)
   l6 = Tkinter.Label(frame1,text=dob_p)
   l6.grid(row=2,column=1)

   #print "birth place :", inter['birth notes']
   bn_p=str(inter['birth notes'])
   l7 = Tkinter.Label(frame1,text="Birth Place :")
   l7.grid(row=3,column=0)
   l7 = Tkinter.Label(frame1,text=bn_p)
   l7.grid(row=3,column=1)

   #print "Biography  :",inter['mini biography']
   bio_p=str(inter['mini biography'])
   sb2 = Tkinter.Scrollbar(frame2)
   sb2.pack( side = "right", fill="y" )
   text1 = Tkinter.Text(frame2,yscrollcommand = sb2.set,height=8)
   l13 = Tkinter.Label(frame2,text="Biography :").pack()
   text1.insert('insert',bio_p)
   text1.pack()
   sb2.config( command = text1.yview )
   
   l15 = Tkinter.Label(frame3,text="Populating...")
   l15.pack()
   #print "\nPopulating"
   cursor.execute("""INSERT INTO Person(Person_id,Name,Birth_Date,Birth_Note,Biography)VALUES(%s,%s,%s,%s,%s);""" ,(id_person,name_p,dob_p,bn_p,bio_p))

   l15 = Tkinter.Label(frame3,text="Done! ")
   l15.pack()
   
   db.commit()
# disconnect from server 
   db.close()

def Call1() :
 global v1
 #top=Tkinter.Tk()
 l1 = Tkinter.Label(win,text="Enter the movie name.").pack() #Creating Label
 v1 = Tkinter.StringVar() 
 e1 = Tkinter.Entry(win,textvariable=v1)
 e1.pack() 
 b1=Tkinter.Button(win,text="Next",command=Movie)
 b1.pack()

def Call2() :
 global v2
 #top=Tkinter.Tk()
 l2 = Tkinter.Label(win,text="Enter the TV Show name :").pack() #Creating Label
 v2 = Tkinter.StringVar() 
 e2 = Tkinter.Entry(win,textvariable=v2)
 e2.pack() 
 b2=Tkinter.Button(win,text="Next",command=Tv_Show)
 b2.pack()
 
def Call3() :
 global v3
 #top=Tkinter.Tk()
 l3 = Tkinter.Label(win,text="Enter the person's name :").pack() #Creating Label
 v3 = Tkinter.StringVar() 
 e3 = Tkinter.Entry(win,textvariable=v3)
 e3.pack() 
 b3=Tkinter.Button(win,text="Next",command=Person)
 b3.pack()
 
CheckVar1 = Tkinter.IntVar()
CheckVar2 = Tkinter.IntVar()
CheckVar3 = Tkinter.IntVar()
c1 = Tkinter.Radiobutton(win,text = "Movie",variable=CheckVar1,command=Call1)
c2 = Tkinter.Radiobutton(top,text = "TV Show",variable=CheckVar2,command=Call2)
c3 = Tkinter.Radiobutton(top,text = "Person",variable=CheckVar3,command=Call3)
c1.pack()
c2.pack()
c3.pack()
win.mainloop()
