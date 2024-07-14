from tkinter import *
root = Tk()
root.geometry("400x600")
root.title("Events in Tkinter")

Event=Button(root,text="CLick me")
Event.pack()

# Binding Events

def Function(event):
    print(f"Event is triggered and handled at {event.x} , {event.y}")
    
Event.bind('<Button-1>',Function)
Event.bind('<Double-1>',quit)
root.mainloop()