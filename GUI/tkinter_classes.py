from ctypes import alignment
from pydoc import visiblename
from tkinter import *
from tkinter import ttk
import tkinter

from general import avgpts, p3d
from PIL import Image, ImageTk
import math as m

global_scale = 1
widgets = {
    "FileOpener": []
}  # list of all drag-drop widgets
'''
Application (Tk) --> contains GUI, Viewport
L   GUI elements
L   Viewport
    L   Widgets (example: FileOpener)
        L   Frame
            L   Canvas
                L   graphics
'''

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
def f():  # placeholder function
    pass
class Application(Tk):
    def __init__(self,master):
        #super().__init__(master)
        self.menubar = Menu(master)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=f)
        self.filemenu.add_command(label="Open", command=f)
        self.filemenu.add_command(label="Save", command=f)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=master.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        





if __name__ == "__main__":
    window = Tk()
    window.geometry("800x450")
    app = Application(window)
    window.configure(menu = app.menubar)
    window.mainloop()

    