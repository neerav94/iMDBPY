import Tkinter
import tkMessageBox
from imdb import IMDb
win = Tkinter.Tk()
ia = IMDb()
global new
global movie
movie = []
global lb
lb = []
global top
top = []
global call1
call1=[]
global call2
call2=[]
global call3
call3=[]
global call4
call4=[]
global call5
call5=[]
global call6
call6=[]
global call7
call7=[]
global call8
call8=[]
global call9
call9=[]
global call10
call10=[]
global call11
call11=[]
new = Tkinter.Tk()
l1 = Tkinter.Label(win,text="Enter the movie name.").pack() #Creating Label
v1 = Tkinter.StringVar() 
e1 = Tkinter.Entry(win,textvariable=v1)
e1.pack()

def call2() :
   global id_movie
   inter1 = ia.get_movie(id_movie)
   l3 = Tkinter.Label(new,text= "Title : ").grid(row=0,column=0)
   l31 = Tkinter.Label(new,text= inter1[ 'title' ]).grid(row=0,column=2)
def call3() :
   inter2 = ia.get_movie(id_movie)
   l4 = Tkinter.Label(new,text="Genre : ").grid(row=1,column=0)
   lb41 = Tkinter.Listbox(new)
   for gen in inter2['genre']:
      lb41.insert("end",gen)
   lb41.grid(row=1,column=2)
def call4() :
   global id_movie
   inter3 = ia.get_movie(id_movie)
   l5 = Tkinter.Label(new,text= "Director : ").grid(row=2,column=0)
   lb51 = Tkinter.Listbox(new)
   for dir in inter3['director']:
      lb51.insert("end",dir)
   lb51.grid(row=2,column=2)   
def call5() :
   global id_movie
   inter4 = ia.get_movie(id_movie)
   l6 = Tkinter.Label(new,text= "Writer : ").grid(row=3,column=0)
   lb61 = Tkinter.Listbox(new)
   for wri in inter4['writer']:
      lb61.insert("end",wri)
   lb61.grid(row=3,column=2)
def call6() :
   global id_movie
   inter5 = ia.get_movie(id_movie)
   l7 = Tkinter.Label(new,text= "Cast : ").grid(row=4,column=0)
   lb71 = Tkinter.Listbox(new)
   for cas in inter5['cast']:
      lb71.insert("end",cas)
   lb71.grid(row=4,column=2)
def call7() :
   global id_movie
   inter6 = ia.get_movie(id_movie)
   l8 = Tkinter.Label(new,text= "Runtime : ").grid(row=5,column=0)
   lb81 = Tkinter.Listbox(new)
   for run in inter6['runtimes']:
      lb81.insert("end",run)
   lb81.grid(row=5,column=2)
def call8() :
   global id_movie
   inter7 = ia.get_movie(id_movie)
   l9 = Tkinter.Label(new,text= "Country : ").grid(row=6,column=0)
   lb91 = Tkinter.Listbox(new)
   for count in inter7['countries']:
      lb91.insert("end",count)
   lb91.grid(row=6,column=2)
def call9() :
   global id_movie
   inter8 = ia.get_movie(id_movie)
   l10 = Tkinter.Label(new,text= "Language : ").grid(row=7,column=0)
   lb101 = Tkinter.Listbox(new)
   for lan in inter8['languages']:
      lb101.insert("end",lan)
   lb101.grid(row=7,column=2)
def call10() :
   global id_movie
   inter9 = ia.get_movie(id_movie)
   l11 = Tkinter.Label(new,text= "Rating : ").grid(row=8,column=0)
   lb111 = Tkinter.Listbox(new)
   for rat in inter9['rating']:
      lb111.insert("end",rat)
   lb111.grid(row=8,column=2)

def call():
   name = v1.get()
   for movie in ia.search_movie(name):
      lb.insert("end",(movie.movieID, movie['title'], movie['year']))
   lb.pack()
      
def call1(): 
   global v2
   global id_movie
   id_movie = v2.get()
   win.destroy()
   inter = ia.get_movie(id_movie)
   top = Tkinter.Tk()
   CheckVar1 = Tkinter.IntVar()
   CheckVar2 = Tkinter.IntVar()
   CheckVar3 = Tkinter.IntVar()
   CheckVar4 = Tkinter.IntVar()
   CheckVar5 = Tkinter.IntVar()
   CheckVar6 = Tkinter.IntVar()
   CheckVar7 = Tkinter.IntVar()
   CheckVar8 = Tkinter.IntVar()
   CheckVar9 = Tkinter.IntVar()
   c1 = Tkinter.Checkbutton(top,text = "Title",variable=CheckVar1,command=call2)
   c2 = Tkinter.Checkbutton(top,text = "Genre",variable=CheckVar2,command=call3)
   c3 = Tkinter.Checkbutton(top,text = "Director",variable=CheckVar3,command=call4)
   c4 = Tkinter.Checkbutton(top,text = "Writer",variable=CheckVar4,command=call5)
   c5 = Tkinter.Checkbutton(top,text = "Cast",variable=CheckVar5,command=call6)
   c6 = Tkinter.Checkbutton(top,text = "Runtime",variable=CheckVar6,command=call7)
   c7 = Tkinter.Checkbutton(top,text = "Country",variable=CheckVar7,command=call8)
   c8 = Tkinter.Checkbutton(top,text = "Language",variable=CheckVar8,command=call9)
   c9 = Tkinter.Checkbutton(top,text = "Rating",variable=CheckVar9,command=call10)
   c1.pack()
   c2.pack()
   c3.pack()
   c4.pack()
   c5.pack()
   c6.pack()
   c7.pack()
   c8.pack()
   c9.pack()

   '''inter = ia.get_movie(id_movie)
      
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
   print "plot  :", inter['plot']'''

b1=Tkinter.Button(win,text="Next",command=call)
b1.pack()
lb = Tkinter.Listbox(win, height = 30,width = 40)
l2 = Tkinter.Label(win,text="Enter the id.")
l2.pack()
v2=Tkinter.IntVar()
e2 = Tkinter.Entry(top,textvariable=v2)
e2.pack()
b2 = Tkinter.Button(top,text="Print",command=call1)
b2.pack()   

win.mainloop()
