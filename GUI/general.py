import math as m
from PIL import Image, ImageTk
from tkinter import PhotoImage
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
		Args:
			x,y,z (ints): x,y,z position in pseudo-isometric space
			depth_scaling(bool): Whether or not to account for depth scaling
	"""
	if depth_scaling:
		d = z / m.sqrt(2) #depth scale by root 2. 
	else:
		d=z
	return (x+d,y+d)
def avg(a,b):
	"""Average of two numbers

	Args:
		a (int of float): number 1
		b (int or float): number 2

	Returns:
		float: Average of A and B
	"""

	return (a+b) / 2
def create_img(fp, scale = 1):
	"""Creates an image, and scales it

	Args:
		fp (str): Image file path
		scale (int, optional): Image scale factor. Defaults to 1.

	Returns:
		_type_: _description_
	"""
	PhIm = PhotoImage(file=fp)
	#PhIm = PhIm.zoom(x=2,y=2)
	s = int(1/scale)
	PhIm = PhIm.subsample(s,s)
	

	return PhIm
def keylist(d: dict):
	"""Returns all of the keys of a dictionary, in a list

	Args:
		d (dict): A dictionary

	Returns:
		list(str): A list of keys
	"""
	return list(d.keys())
