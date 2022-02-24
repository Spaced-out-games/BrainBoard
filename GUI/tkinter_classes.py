from tkinter import *
from tkinter import ttk

class Viewport(Canvas):
	def __init__(self, parent, **kwargs):
		super().__init__(parent, **kwargs)
		"""
		Button Bindings go here
		format:
		self.bind("<button-code>", self.method)
		"""
	

class FileOpener(Frame):
	def __init__(self,parent = canvas):
		Frame.__init__(self, parent)
		self.parent = parent
		#Default Class attributes
		self.input = None#Input data, from block A 
		self.output = None#Output data, for block C
		self.input_node = None #Another Block reference
		self.output_node = None #Another Block reference
		"""																		EDITS GO BELOW															"""
		self.block




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
	def __draw__(self):
		"""
		c = self.parent
		c.create_rectangle([(0,0),(20,20)])
		"""

if __name__ ==  "__main__":
	window = Tk()
	canvas = Viewport(window)
