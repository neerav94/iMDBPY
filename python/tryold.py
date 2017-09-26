import Tkinter
win = Tkinter.Tk()
global top
top = []
global name
name = []
global ny
ny = []
global lb
lb = []
global new
new = []
l1 = Tkinter.Label(win,text="Enter the movie name.").pack() #Creating Label
v1 = Tkinter.StringVar() 
e1 = Tkinter.Entry(win,textvariable=v1)
e1.pack()
def call():
   ny = ["amogh","nerav","jateen"]
   name = v1.get()
   print name
   #lb.insert("end",("amogh","1pi13is016"))
   #lb.insert("end",("jateen","1pi13is044"))
   #lb.insert("end",("neerav","1pi13is065"))
   #lb.pack()

   win.destroy()
   top = Tkinter.Tk()
   lb=Tkinter.Listbox(top, height = 10,width = 20)
   for item in ny:
      lb.insert("end",item)
   lb.pack()
   l2 = Tkinter.Label(top,text="Enter the id.")
   l2.pack()
   v2 = Tkinter.IntVar()
   e2 = Tkinter.Entry(top,textvariable=v2)
   e2.pack()
   b2=Tkinter.Button(top,text="two",command=call1).pack()
def call1() :
   print "New window"
   #top.destroy()
   new = Tkinter.Tk()
   b3=Tkinter.Button(new,text="TJBSCJK")
   b3.pack()
b1 = Tkinter.Button(win,text="Next",command=call)
b1.pack()
win.mainloop()
