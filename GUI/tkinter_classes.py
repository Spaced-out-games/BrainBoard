from tkinter import *
from tkinter import ttk
from general import avgpts, p3d
from PIL import Image, ImageTk

global_scale = 1
widgets = [] # list of all drag-drop widgets

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



class FileOpener(Frame):
	def __init__(self, parent):
		#super().__init__(self, parent)
		self.parent = parent
		#Default Class attributes
		self.input = None#Input data, from block A 
		self.output = None#Output data, for block C
		self.input_node = None #Another Block reference
		self.output_node = None #Another Block reference
		self.frame = Frame(parent)
		self.frame.place(x=0,y=0)
		self.canvas = Canvas(self.frame)
		self.canvas.grid(column=0, row=0, sticky=(N, W, E, S))
		make_draggable(self.canvas)
		#w,h = image.width,image.height
		#w,h = int(w * self.scale),int(h * self.scale)
		#image = image.resize((w,h))
		"""
		Creating an image, and drawing it on frame
		image = Image.open("Untitled-1.png")
		self.img = ImageTk.PhotoImage(image)
		self.canvas.create_image(0,0,image = self.img,anchor = NW,tags = "image")
		"""
		"""																		EDITS GO BELOW															"""





		"""																		EDITS GO ABOVE															"""

	def __recv__(self):
		if self.input!= None and self.input_node != None:
			self.input = (self.input_node).output
		else:
			pass
	def __send__(self):
		if self.output_node != None and self.output!=None:
			self.output_node.input = self.output
		else:
			pass
	def __proc__(self, **kwargs):
		args = kwargs
		self.recv()
		x = self.input
		#...do some processing in respect to x
		self.output = x
		self.__send__()
		"""																		EDITS GO BELOW															"""





		"""																		EDITS GO ABOVE															"""
if __name__ ==  "__main__":
	window = Tk()
	canvas = Canvas(window)
	b = Block(window)
	window.mainloop()