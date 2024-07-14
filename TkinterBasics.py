from tkinter import *
root = Tk()   # with this command a basic GUI will be created 

# adding the geometry settings 
root.geometry("1000x1000")
root.minsize(width=400, height=300)
# root.maxsize(width=800,height=700)

# adding the label here
newlabel = Label(text="Hello World!")
newlabel.pack()

'''adding image-but PhotoImage always requires image to be in png format for an image to be in jpg format 
download pillow '''
Photo=PhotoImage(file="C:\\Users\\akshr\\OneDrive\\Desktop\\TaskIcon(1).png")
pnglabel=Label(image=Photo)
pnglabel.pack()

# adding jpg image
from PIL import Image , ImageTk
image1 = Image.open("C:\\Users\\akshr\\OneDrive\\Desktop\\python symbol.jpeg")
photo =ImageTk.PhotoImage(image1)
#jpglabel=Label(image=image1)
photo.pack() 

# Label Attributes 
text = Label(text='''General knowledge is information that has been accumulated over time through 
             various media and sources.It excludes specialized learning that can only be 
             obtained with extensive training and information confined to a single medium. 
             General knowledge is an essential component of crystallized intelligence. 
             It is strongly associated with general intelligence and with openness to experience.''',
             bg="green",fg="white",padx=44,pady=55,font="comicsansms 19 italic",borderwidth=5,relief=RIDGE)
# Options available for relief are SUNKEN , RAISED , GROOVE , RIDGE
# Font can also be given in the tuple format as font = (comicsansms , 19 , italic )

# pack attributes 
text.pack(side=LEFT,anchor=NW,fill=X,padx=34,pady=45) # use ctrl+space to see more options

# GUI Logic here 
root.mainloop()   # remembers the GUI logic 