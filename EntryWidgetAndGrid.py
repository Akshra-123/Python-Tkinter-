from tkinter import *

root =Tk()
root.geometry("600x600")

# Adding grid
user=Label(root,text="Username:")
user.grid()

password=Label(root,text="Password:")
password.grid(row=1)


# Types of Text Variable - BooleanVar , DoubleVar , IntVar , StringVar
# Adding Entry Widget
UserEntry=Entry(root,textvariable=StringVar())
PassEntry=Entry(root,textvariable=StringVar())

UserEntry.grid(row=0,column=1)
PassEntry.grid(row=1,column=1)

# Submit Button

def getVals():
    print(UserEntry.get())
    print(PassEntry.get())
    
switch = Button(text="Submit",command=getVals)
switch.grid()

root.mainloop()
