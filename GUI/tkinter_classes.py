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
	def __init__(self, parent, x=20,y=20,w = 20,h = 20,d = 20,f = "#00ffff", o = "#00aaaa"):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.d = d
		self.o = o
		self.f = f
		self.block = None
		self.parent = parent
	def __draw__(self):
		x,y = self.x,self.y
		w,h,d = self.w, self.h, self.d
		p = [
			(x,y),
			(x+w,y),
			(x+w,y+h),
			(x,y+h)
		]
		p2 = [
			p3d(x,y,d),
			p3d(x+w,y,d),
			p3d(x+w,y+h,d),
			p3d(x,y+h,d)
		]
		canvas.create_polygon([p[0],p[1],p2[1],p2[0]],fill = self.f, outline = self.o) #Top face
		canvas.create_polygon([p[0],p2[0],p2[3],p[3]],fill = self.f, outline = self.o)# Left Face
		canvas.create_rectangle(p2[0],p2[2], fill = self.f, outline=self.o)



window = Tk() #Create tkinter window element
window.geometry("500x500+0+0")
canvas = Canvas(window)
canvas.pack()
t= DataBlock(canvas)
t.__draw__()

window.mainloop()