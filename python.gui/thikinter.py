import tkinter
from tkinter import*
from tkinter import messagebox
root=tkinter.Tk()
root.title("mahesh")

#label
label=tkinter.Label(root,text="hiii").pack()
#button
b=Button(root,text="login",bg="red",fg="blue").pack()

#radio
r=Radiobutton(root,text="nani",value=1).pack()


#message
def Button1():
    messagebox.showinfo("status","please")
b=Button(root,text="py",command=Button1)
b.pack()
root.mainloop()
