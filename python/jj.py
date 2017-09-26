import Tkinter
top = Tkinter.Tk()

frame3 = Tkinter.Frame(top)       # select of names
frame3.pack()
scroll = Tkinter.Scrollbar(frame3, orient= "vertical")
select = Tkinter.Listbox(frame3, yscrollcommand=scroll.set, height=6)
select.insert("end",("Neerav","Amogh","Jateen"))
scroll.config (command=select.yview)
scroll.pack(side="right", fill="y")
select.pack(side="left",  fill="both", expand=1)

frame1 = Tkinter.Frame(top)
frame1.pack()

Tkinter.Label(frame1, text="Name").grid(row=0, column=0)
nameVar = Tkinter.StringVar()
name = Tkinter.Entry(frame1, textvariable=nameVar)
name.grid(row=0, column=1)

Tkinter.Label(frame1, text="Phone").grid(row=1, column=0)
phoneVar= Tkinter.StringVar()
phone= Tkinter.Entry(frame1, textvariable=phoneVar)
phone.grid(row=1, column=1)

top.mainloop()
