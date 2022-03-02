import math as m
from tkinter import *
from tkinter import ttk
from ctypes import pointer, POINTER
"""
This file defines the default block class. GUI class elements inherit these values, always. This file is unlikely to be used much
"""
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
		self.button = Button(master = self.frame)
		#make_draggable(self.canvas)
		#w,h = image.width,image.height
		#w,h = int(w * self.scale),int(h * self.scale)
		#image = image.resize((w,h))
		
		#"""
		#Creating an image, and drawing it on frame
		image = Image.open("Untitled-1.png")
		self.img = ImageTk.PhotoImage(image)
		self.canvas.create_image(0,0,image = self.img,anchor = NW,tags = "image")
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