from tkinter import *
root=Tk()
root.title("Canvas Widget")
width=800
height=400
root.geometry(f"{width}x{height}")
canvas_widget=Canvas(root,width=width,height=height)
canvas_widget.pack()
canvas_widget.create_line(0,0,400,400)
canvas_widget.create_line(200,300,0,350)
canvas_widget.create_rectangle(3,5,700,300)
canvas_widget.create_oval(344,233,200,400)


root.mainloop()