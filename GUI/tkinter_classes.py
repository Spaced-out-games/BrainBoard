import math as m
from tkinter import *
from tkinter import ttk
from xml.dom.minidom import Attr
def avgpts(pts):
	x = []
	y = []
	for i in pts:
		x.append(i[0])
		y.append(i[1])
	return (m.floor(sum(x)/len(x)),m.floor(sum(y)/len(x)))

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
			(x,y+h),
			(x+w,y+h)
		]
		p2 = [
			p3d(x,y,d),
			p3d(x+w,y,d),
			p3d(x,y+h,d),
			p3d(x+w,y+h,d)
			
		]
		canvas.create_polygon([p[0],p[1],p2[1],p2[0]],fill = self.f, outline = self.o) #Top face

		canvas.create_polygon([p[0],p2[0],p2[2],p[2]],fill = self.f, outline = self.o)# Left Face
		m = avgpts([p[0], p2[0], p[2],p2[2]])
		canvas.create_text(m[0],m[1],text = str(d))
		canvas.create_rectangle(p2[0],p2[3], fill = self.f, outline=self.o)



window = Tk() #Create tkinter window element
window.geometry("500x500+0+0")
canvas = Canvas(window)
canvas.pack()
t= DataBlock(canvas)
t.__draw__()

window.mainloop()