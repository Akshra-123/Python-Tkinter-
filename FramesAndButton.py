from tkinter import *
root = Tk()
root.geometry("800x900")

# Frames 
f1=Frame(root,bg="black",borderwidth=5,relief=SUNKEN)
f1.pack(side=LEFT,anchor=NW)
l=Label(f1,text="Adding Frames")
l.pack(pady=300,padx=5)

f2=Frame(root,bg="Grey",borderwidth=4,relief=SUNKEN)
f2.pack(side=TOP)
l2=Label(f2,text="Welcome to our GUI",font=("comicsansms",13,"bold"))
l2.pack()


def Hello():
    print("Hello World!")
    
def Name():
    print("My name is Akshra")

def Course():
    print("BTech")

def Specialisations():
    print("Machine Learning")
    

# Buttons
b1=Button(f1,fg="Green",text="Hello",command=Hello)
b1.pack(pady=3)

b2=Button(f1,text="Name",command=Name)
b2.pack(pady=3)

b3=Button(f1,text="Course",command=Course)
b3.pack(pady=3)

b4=Button(f1,text="Specialisation",command=Specialisations)
b4.pack(pady=3)


root.mainloop()