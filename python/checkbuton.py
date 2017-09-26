import Tkinter
import tkMessageBox
top = Tkinter.Tk()
def call():
    B1=Tkinter.Button(top,text="t").pack()
    top.destroy()
CheckVar1 = Tkinter.IntVar()
CheckVar2 = Tkinter.IntVar()
c1 = Tkinter.Checkbutton(top,text = "Movie",variable=CheckVar1,command=call)
c2 = Tkinter.Checkbutton(top,text = "TV",variable=CheckVar2,onvalue=1,offvalue=0)
c1.pack()
c2.pack()

top.mainloop()
