import math as m
from tkinter import *
from tkinter import ttk
from ctypes import pointer, POINTER
"""
This file defines the default block class. GUI class elements inherit these values, always. This file is unlikely to be used much
"""
def f(): #placeholder function
	pass
class Application(Frame):
	def __init__(self, master):
		super().__init__(master)
		self.pack()
		self.menubar = Menu(master)#maybe master insteas of self
		self.filebar = Menu(self.menubar, tearoff = 0)
		self.filebar.add_command(label="New", command=f)
		self.filebar.add_command(label="Open", command=f)
		self.filebar.add_command(label="Save", command=f)
		self.filebar.add_separator()
		self.filebar.add_command(label="Exit", command=master.quit)
		self.menubar.add_cascade(label="File", menu=self.filebar)
		"""
		GUI elements go here

		self.attr = tk.xxxxVar()
		self.attr.set(initial value)
		self.entry["xxxxVariable"] = self.attr
		self.entry.bind("<key>",self.method)
		"""
class FileOpener(Frame):
	def __init__(self, parent):
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
		self.button = Button(master = self.frame)
		#make_draggable(self.canvas)
		#w,h = image.width,image.height
		#w,h = int(w * self.scale),int(h * self.scale)
		#image = image.resize((w,h))
		
		#"""
		#Creating an image, and drawing it on frame
		
		#"""
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
		self.recv()
		x = self.input
		#...do some processing in respect to x
		file = open(x)
		#file proccessing done here
		self.output = file
		self.__send__()
		"""																		EDITS GO BELOW															"""





		"""																		EDITS GO ABOVE													"""









if __name__ == "__main__":
	window = Tk()
	window.geometry("1960x1080")
	app = Application(window)
	window.config(menu = app)
	window.mainloop()
