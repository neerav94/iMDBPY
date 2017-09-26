import Tkinter
from imdb import IMDb
win = Tkinter.Tk()
ia = IMDb()
l1 = Tkinter.Label(win,text="Enter the movie name.").pack() #Creating Label
v1 = Tkinter.StringVar() 
e1 = Tkinter.Entry(win,textvariable=v1)
e1.pack()
global movie
movie = []
global lb
lb = []
global top
top = []
def call():
   name = v1.get()
   for movie in ia.search_movie(name):
      lb.insert("end",(movie.movieID, movie['title'], movie['year']))
   lb.pack()
   #print name
   #for movie in ia.search_movie(name):
      #lb.insert("end",(movie.movieID, movie['title'], movie['year']))
      #print movie.movieID, movie['title'], movie['year']
   #win.destroy()
   #top = Tkinter.Tk()
   
def call1(): 
   global v2
   id_movie = v2.get()
   #id_movie = 3322420

   inter = ia.get_movie(id_movie)
   print inter
   
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
   print "plot  :", inter['plot']
b1=Tkinter.Button(win,text="Next",command=call)
b1.pack()
lb = Tkinter.Listbox(win, height = 30,width = 40)
l2 = Tkinter.Label(win,text="Enter the id.")
l2.pack()
#   global v2
v2=Tkinter.IntVar()
e2 = Tkinter.Entry(top,textvariable=v2)
e2.pack()
b2 = Tkinter.Button(top,text="Print",command=call1)
b2.pack()   

win.mainloop()
