from ctypes import alignment
from pydoc import visiblename
from tkinter import *
from tkinter import ttk
import tkinter
from turtle import bgcolor
from general import create_img

from general import avgpts, p3d
from PIL import Image, ImageTk
import math as m
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

class TransparentImageButton(Tk):
    def __init__(self, master, fp= "GUI/file_img.png", SpawnWidget = Frame, function = None,relx = 0, rely = 0, anchor = NW, width = 100, height = 100):
        self.fp = fp# image filapath
        c = master['bg']
        if c == None:
            c = 'white'
        self.spawnwidget = SpawnWidget# Widget to spawn on button click
        self.function = function
        self.img = create_img(fp = fp, scale = 0.3)
        self.frame = Frame(
            master,
            padx = 5,
            pady = 5,
            highlightbackground=c,
            bg = c,
            highlightthickness=0,
        )
        self.frame.place(anchor = anchor,relx=relx,rely=rely,width=width,height=height)
        self.canvas = Canvas(
            self.frame,
            bg = c,
            highlightbackground=c
            )
        self.canvas.place(anchor = NW,relx=0,rely=0,relwidth=1,relheight=1)
        self.image = self.canvas.create_image((45,45),image = self.img,anchor = CENTER)
        self.canvas.tag_bind(self.image, "<Button-1>",self.function)