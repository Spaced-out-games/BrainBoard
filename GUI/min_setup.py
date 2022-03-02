from tkinter import *
from tkinter import ttk
from general import avgpts, p3d
from PIL import Image, ImageTk

class Viewport(Canvas):
	def __init__(self, parent, **kwargs):
		super().__init__(parent, **kwargs)
		self.grid(column=0, row=0, sticky=(N, W, E, S))
		"""
		Button Bindings go here
		format:
		self.bind("<button-code>", self.method)
		"""
	

if __name__ ==  "__main__":
	window = Tk()
	window.columnconfigure(0, weight=1)
	window.rowconfigure(0, weight=1)
	window.geometry("500x500")
	canvas = Viewport(window)
	window.mainloop()


