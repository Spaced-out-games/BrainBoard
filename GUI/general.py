import math as m
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
def avg(a,b):
	return (a+b)<<1