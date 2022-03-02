from tkinter import *
from tkinter import ttk
from general import avgpts, p3d
from PIL import Image, ImageTk

class Viewport(Canvas):
	def __init__(self, parent, **kwargs):
		super().__init__(parent, **kwargs)
		self.grid(column=0, row=0, sticky=(N, W, E, S))
		"""
		Button Bindings go here
		format:
		self.bind("<button-code>", self.method)
		"""

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

if __name__ ==  "__main__":
	window = Tk()
	window.columnconfigure(0, weight=1)
	window.rowconfigure(0, weight=1)
	window.geometry("500x500")
	
	#widgets[0].place(x=90,y=90, relwidth=1,relheight=1)
	window.mainloop()


