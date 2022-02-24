import math as m
from tkinter import *
from tkinter import ttk
from ctypes import pointer, POINTER
"""
This file defines the default block class. GUI class elements inherit these values, always. This file is unlikely to be used much
"""
class Block:
	def __init__(self, parent: Canvas):
		Frame.__init__(self, parent)
		self.parent = parent
		#Default Class attributes
		self.input = None#Input data, from block A 
		self.output = None#Output data, for block C
		self.input_node = None #Another Block reference
		self.output_node = None #Another Block reference
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
	def __draw__(self):
		c = self.parent
