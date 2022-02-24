import math as m
from tkinter import *
from tkinter import ttk
from xml.dom.minidom import Attr


def p3d(x,y,z,depth_scaling = True):
	"""
	2D w/depth to 2D screen space. Basically (x,y) + (z/√2,z/√2)
	"""
	if depth_scaling:
		d = z / m.sqrt(2) #depth scale by root 2. 
	else:
		d=z
	return (x+d,y+d)


class Sketchpad(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

class DataBlock(Frame):
	def __init__(self, parent, w = 20,h = 20,d = 20,**kwargs):
		self.w = w
		self.h = h
		self.d = d
		"""
		Add attributes during initialization
		k = kwargs.keys()
		for i in k:
			self.__setattr__(i, kwargs.get(i))
		"""


window = Tk() #Create tkinter window element
window.geometry("500x500+0+0")

t= DataBlock(window, p = 100)
print(t.p)

window.mainloop()