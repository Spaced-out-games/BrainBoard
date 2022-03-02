from tkinter import *
from tkinter import ttk
from general import avgpts, p3d
from PIL import Image, ImageTk

def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)

main = Tk()

frame = Frame(main, bd=4, bg="grey")
frame.place(x=10, y=10)
make_draggable(frame)
canvas = Canvas(frame)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.create_rectangle(0,0,20,20)

#image =  ImageTk.PhotoImage(file = "Untitled-1.png")
#Label(main, image=image).pack()
main.mainloop()