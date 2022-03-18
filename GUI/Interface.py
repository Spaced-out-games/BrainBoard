from ast import arguments
from genericpath import exists
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from jinja2 import is_undefined
from tkinter_classes import make_draggable
from classes import FileOpener
from general import create_img, keylist
from pprint import pprint as pprint
bordercolor = "#888888"
windowcolor = "#aaaaaa"

def f(event = None):
	print("called!")
class TransparentImageButton(Tk):
    def __init__(self, master, fp= "GUI/file_img.png", function = None,relx = 0, rely = 0, anchor = NW, width = 100, height = 100):
        self.fp = fp# image filapath
        c = master['bg']
        if c == None:
            c = 'white'
        self.function = function
        self.img = create_img(fp = fp, scale = 0.3)
        self.frame = Frame(
            master,
            padx = 5,
            pady = 5,
            highlightbackground=c,
            bg = c,
            highlightthickness=0,
        )
        self.frame.place(anchor = anchor,relx=relx,rely=rely,width=width,height=height)
        self.canvas = Canvas(
            self.frame,
            bg = c,
            highlightbackground=c
            )
        self.canvas.place(anchor = NW,relx=0,rely=0,relwidth=1,relheight=1)
        self.image = self.canvas.create_image((45,45),image = self.img,anchor = CENTER)
        self.canvas.tag_bind(self.image, "<Button-1>",self.function)

frames = 0
def task():
	global frames
	frames+=1

	#schedule next call
	window.after(1, task)
class Application(Tk):
	def __init__(self,master):
		#Menu Bar
		self.menubar = Menu(master)
		self.menubar = Menu(master)
		self.filemenu = Menu(self.menubar, tearoff=0)
		self.filemenu.add_command(label="New", command=f)
		self.filemenu.add_command(label="Open", command=f)
		self.filemenu.add_command(label="Save", command=f)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Exit", command=master.quit)
		self.menubar.add_cascade(label="File", menu=self.filemenu)
		#GUI
		#Top Toolbar

		self.Topbar = Frame(master, height = 100,padx=0,pady=0,highlightbackground=bordercolor,bg=windowcolor,highlightthickness=2)
		self.Topbar.place(anchor = NW,relx=0,rely=0,relwidth = 0.9,relheight = 0.15)

		#Canvas frame
		self.cf = Frame(master,padx=0,pady=0,highlightbackground=bordercolor,bg=windowcolor,highlightthickness=2)
		self.cf.place(anchor = NW,relx=0.099,rely=0.148,relwidth=0.801,relheight=0.699)
		self.c = Canvas(master = self.cf,bg = "#FFFFFF")
		self.c.place(anchor = NW,relwidth=1,relheight=1)
		#toolbar menu
		self.toolbar = Frame(master,padx=0,pady=0,highlightbackground=bordercolor,bg=windowcolor,highlightthickness=2)
		self.toolbar.place(anchor = NW,relx=0.00,rely=0.148,relwidth=0.1,relheight=0.7)
		self.FOButton = TransparentImageButton(self.toolbar,relx = 0.5,anchor = N,function = None)
		self.widgets = []
	def add_widget(self, **kwargs):
		"""
		Expected keyword argument structure:
		{
			"Widget": WidgetInstance
			"WidgetParams":{}
			"PackParams":{} --> dictionary containing the parameters for packing widget
		}
		"""
		default = {# a peek at the default argument structure
			"Widget": Frame,
			"WidgetParams": {
				"master": self.c,
				"width": 100,
				"height": 100,
				"bg": windowcolor
			},
			"PackParams":{
				"anchor": NW,
				"relx": 0,
				"rely": 0
			}
		}
		#-----------------------------------------------------------
		#if arguments are empty, default settings are assumed
		if kwargs == {}:
			kwargs = default
		#-----------------------------------------------------------
		w = kwargs['Widget'](**kwargs.get("WidgetParams"))
		if not w.winfo_ismapped():
			w.place(**kwargs.get("PackParams"))
		self.widgets.append(w)
		return w.winfo_ismapped()

		#w.place(kwargs['PackParams'])
		

		

		


if __name__ == "__main__":
	window = Tk()
	#Image initializaton (Needs to be after Tk() is created)
	window.geometry("1360x768")
	app = Application(window)
	window.after(1,task)
	window.mainloop()



