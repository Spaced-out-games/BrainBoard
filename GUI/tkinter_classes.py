from tkinter import *
from tkinter import ttk
from general import avgpts, p3d
from PIL import Image, ImageTk


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

class Viewport(Canvas):
	def __init__(self, parent, **kwargs):
		super().__init__(parent, **kwargs)
		self.grid(column=0, row=0, sticky=(N, W, E, S))
		"""
		Button Bindings go here
		format:
		self.bind("<button-code>", self.method)
		"""
	
class FileOpener(Frame):
	"""
	This object contains the functionality required to find and open a file using the on - screen GUI


	"""
	def __init__(self,parent = Canvas, pos = (100,100)):

		Frame.__init__(self, parent)
		self.pos = pos
		self.parent = parent
		#Default Class attributes
		self.input = None#Input data, from block A 
		self.output = None#Output data, for block C
		self.input_node = None #Another Block reference
		self.output_node = None #Another Block reference
		"""																		EDITS GO BELOW															"""
		x,y = pos
		self.canvas = Canvas(self.master)
		self.canvas.grid(column=0, row=0, sticky=(N, W, E, S))
		self.scale = 1.0
		#self.img = ImageTk.PhotoImage(Image.open("Untitled-1.png"))
		#self.canvas.create_image(0,0,image = self.img)
		self.draw()
		"""
		#File shape
		self.canvas.create_line([(x+5,y),(x+5,y+5),(x,y+5),(x,y+30),(x+20,y+30),(x+20,y),(x+5,y),(x,y+5)],tags = ['draggable'])
		#Scribble lines
		self.canvas.create_line([(x+5,y+10),(x+15,y+10)],tags = ['draggable'])
		self.canvas.create_line([(x+5,y+15),(x+15,y+15)],tags = ['draggable'])
		self.canvas.create_line([(x+5,y+20),(x+15,y+20)],tags = ['draggable'])
		self.canvas.create_line([(x+5,y+25),(x+15,y+25)],tags = ['draggable'])
		"""
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
	def draw(self):
		image = Image.open("Untitled-1.png")
		w,h = image.width,image.height
		w,h = int(w * self.scale),int(h * self.scale)
		image = image.resize((w,h))

		self.img = ImageTk.PhotoImage(image)
		self.canvas.create_image(0,0,image = self.img,anchor = NW)
		"""
		c = self.parent
		c.create_rectangle([(0,0),(20,20)])
		"""
	

if __name__ ==  "__main__":
	window = Tk()
	window.columnconfigure(0, weight=1)
	window.rowconfigure(0, weight=1)
	window.geometry("500x500")
	canvas = Viewport(window)
	widgets = []
	widgets.append(FileOpener(canvas))
	widgets[0].place(x=0,y=0, relwidth=1,relheight=1)
	make_draggable(widgets[0])
	print(type(widgets[0]))
	#widgets[0].place(x=90,y=90, relwidth=1,relheight=1)
	window.mainloop()


