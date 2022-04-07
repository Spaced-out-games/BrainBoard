from ast import Is
from tkinter import *
from tkinter import ttk,filedialog,Widget,dnd
import tkinter
from turtle import bgcolor
from PIL import Image,ImageTk
from jinja2 import is_undefined
from pygments import highlight
from general import create_img, keylist
from pprint import pprint as pprint
from functools import lru_cache
#parent widget space to canvas position = widgetpos + relative pos
viewport = None
data = {
	"currentline": None,
	"focus": None,
	"viewport": None,
	"start": (None, None),
	"wpos": (None, None),
	"wparent": None,
}

get_mouse = lambda event: (event.x, event.y),

def add_tuple(*args):
	xt = 0
	yt = 0
	for t in args:
		x = t[0]
		y = t[1]
		xt += x
		yt += y
	return (xt,yt)


get_parent= lambda widget: Widget.nametowidget(widget, name = widget.winfo_parent())


pallete = {
"bordercolor": "#888888",
"windowcolor": "#aaaaaa",
"windowcolorBG": "#777777"
#other colors are for types
}
f = lambda: None
frames = 0
num_widgets = 0

window = Tk()
window.geometry("1360x768")
def get_canvas_position(widget):
	global viewport, data
	x = 0
	y = 0
	if isinstance(widget,Pin):
		x = 50
		y = 50
	while widget is not viewport:
		x = x + widget.winfo_rootx()
		y = y + widget.winfo_rooty()
		widget = get_parent(widget)
	return (x,y)

def destroy_widget(widgetInstance):
	widgetInstance.destroy(widgetInstance)
def make_draggable(widget):
	widget.bind("<Button-1>", on_drag_start)
	widget.bind("<B1-Motion>", on_drag_motion)
def on_drag_start(event):
	widget = event.widget
	widget._drag_start_x = event.x
	widget._drag_start_y = event.y
	print("pickup")
def on_drag_motion(event):
	print("drop")
	widget = event.widget
	x = widget.winfo_x() - widget._drag_start_x + event.x
	y = widget.winfo_y() - widget._drag_start_y + event.y
	widget.place(x=x, y=y)

def on_drag_start_pin(event):
	w = event.widget
	global data
	p = get_parent(w)
	mouse = (event.x,event.y)
	print(mouse)
	#pinloc
	#set up some focus variables
	#(data['viewport'].winfo_rootx(),data['viewport'].winfo_rooty())
	data['start'] = mouse
	data['focus'] = w
	data['wpos'] = (p.winfo_rootx(),p.winfo_rooty())
	data['wparent'] = p
	
	start = add_tuple(data['start'], data['wpos'])
	line = data['viewport'].create_line(start,start)

	data['currentline'] = line



def on_drag_motion_pin(event):
	w = event.widget
	global data
	p = get_parent(w)
	#print(data('start'))
	start = add_tuple(data['start'], data['wpos'])
	mouse = (event.x,event.y)
	print(mouse)
	end = add_tuple(mouse, data['wpos'])

	data['viewport'].delete(data['currentline'])

	start = (
		start[0] - data['viewport'].winfo_rootx(),
		start[1] - data['viewport'].winfo_rooty()
	)
	end = (
		end[0] - data['viewport'].winfo_rootx(),
		end[1] - data['viewport'].winfo_rooty()
	)

	line = data['viewport'].create_line(start,end)

	data['currentline'] = line

def on_drag_end_pin(event):
	pass

class TransparentImageButton(Tk):
	def __init__(self, master, fp= "GUI/file_img.png", function = None,relx = 0, rely = 0, anchor = NW, width = 100, height = 100,scale = 0.1):
		self.fp = fp# image filapath
		c = master['bg']
		if c == None:
			c = 'white'
		self.function = function
		self.img = create_img(fp = fp, scale = scale)
		self.frame = Frame(
			master,
			padx = 5,
			pady = 5,
			highlightbackground=c,
			bg = c,
			highlightthickness=0
		)
		self.frame.place(anchor = anchor,relx=relx,rely=rely,relwidth=0.9,relheight=0.15)
		self.canvas = Canvas(
			self.frame,
			bg = c,
			highlightbackground=c,
			)

		self.canvas.place(anchor = CENTER,relx=0.5,rely=0.5,relwidth=1,relheight=1)
		self.image = self.canvas.create_image((10,5),image = self.img,anchor = NW)
		self.canvas.tag_bind(self.image, "<Button-1>",self.function)

'''ALL CLASSES BELOW THIS'''
class Reroute(Tk):
	def __init__(self, **args):
		wp = args['WidgetParams']
		pp = args["PackParams"]
		self.f = Frame(
			master = wp['master'],
			padx = 0,
			pady = 0,
			highlightbackground=None,
			bg= "green",
			highlightthickness=4
		)
		self.f.place(
			anchor = pp['anchor'],
			x = pp['x'],
			y = pp['y'],
			width = 50,
			height = 20,
		)
		self.f.focus_set()

		self.c = Canvas(
			master = self.f,
			bg = "red",
			highlightthickness=0
			)
		self.c.place(anchor = NW,x=0,y=0,relwidth =1,relheight = 1)
		settings = (
			{
				"Widget": Pin,
				"WidgetParams":{
					"master": self.c,
					"width": 25,
					"height": 25,
					"bg": None
				},
				"PackParams":{
					"anchor": NW,
					"x": 0,
					"y": 0
				},
				"AdditionalParams":{
					"direction": 'out' #Default
				}
			}
		)
		self.IsSelected = False
		self.input = Pin(**settings)
		
		self.f.bind("<Button-1>",self.select)
		self.f.bind("<B1-Motion>",self.move)
		self.f.bind("<ButtonRelease-1>",self.drop)
		

		self.f.bind("<BackSpace>",self.trydel)
	def select(self, event):
		self.IsSelected = True
		self.HasMoved = False
		p = get_canvas_position(self.f)
		p1 = (self.f.winfo_rootx(),self.f.winfo_rootx())
		print(p)
		print(p1)
		on_drag_start(event)
	def move(self, event):
		self.HasMoved = True
		on_drag_motion(event)
		#move code here
	def drop(self, event):
		"""If widget has been clicked but not dragged, widget remains selected. Otherwise, it is deselected on drop"""
		if self.IsSelected and self.HasMoved:
			self.IsSelected = False
	def trydel(self, event):
		if self.IsSelected:
			self.f.destroy()



class Pin(Tk):
	def __init__(self, **args):
		#Note: kwargs has no depth
		wp = args['WidgetParams']
		self.img = create_img(fp = "GUI/pin-open.png", scale = 0.04)
		self.fp = "test"
		pp = args["PackParams"]
		self.f = Frame(
			master = wp['master'],
			padx = 0,
			pady = 0,
			highlightbackground=None,
			bg = 'green',
			highlightthickness=4#0 later
		)

		self.f.place(
			anchor = pp['anchor'],
			x = pp['x'],
			y = pp['y'],
			width=15,
			height=15
		)
		
		self.c = Canvas(
			master = self.f,
			bg = "black",
			highlightthickness=0
		)


		self.c.place(anchor = NW,x=0,y=0,width=11,height=11)
		
		self.image = self.c.create_image((0,0),image = self.img,anchor = NW)

		#when canvas is clicked
		self.c.tag_bind(self.image,"<Button-1>", on_drag_start_pin)
		self.c.tag_bind(self.image,"<B1-Motion>", on_drag_motion_pin)
		self.c.tag_bind(self.image,"<ButtonRelease-1>",on_drag_end_pin)



class FileOpener(Tk):
	def __init__(self, **args):
		#Note: kwargs has no depth
		wp = args['WidgetParams']
		self.img = create_img(fp = "GUI/file_img.png", scale = 0.25)
		self.fp = "test"
		pp = args["PackParams"]
		self.f = Frame(
			master = wp['master'],
			padx = 0,
			pady = 0,
			highlightbackground=pallete['bordercolor'],
			bg = pallete['windowcolor'],
			highlightthickness=2,
		)
		self.f.place(
			anchor = pp['anchor'],
			x = pp['x'],
			y = pp['y'],
			width = 100,
			height=150
		)
		self.c = Canvas(
			master = self.f,
			bg = None,
			width = 64,#36,
			height = 64#55
		)
		self.c.place(anchor = CENTER,relx=0.5,rely=0.35)
		self.image = self.c.create_image((20,30),image = self.img,anchor = CENTER)
		self.filebutton = Button(master = self.f,text="Open File",command = self.dialog)
		self.filebutton.place(anchor = CENTER, relx=0.5,rely = 0.9)

		self.l = Label(master = self.f, text = self.fp,bg = pallete['windowcolor'])
		self.l.place(anchor = CENTER, relx=0.5,rely = 0.7)
		#self.c.tag_bind(self.image,"<Button-1>", on_drag_start)
		#self.c.tag_bind(self.image,"<B1-Motion>", on_drag_motion)
		self.f.bind("<Button-1>", on_drag_start)
		self.f.bind("<B1-Motion>", on_drag_motion)

	def dialog(self):
		d = filedialog.askopenfilename()
		print(d)
		self.fp = d
		self.l['text'] = d
		self.l.update()

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

		self.Topbar = Frame(master, height = 100,padx=0,pady=0,highlightbackground=pallete['bordercolor'],bg=pallete['windowcolor'],highlightthickness=2)
		self.Topbar.place(anchor = NW,relx=0,rely=0,relwidth = 0.9,relheight = 0.15)

		#Canvas frame
		self.cf = Frame(master,padx=0,pady=0,highlightbackground=pallete['bordercolor'],bg=pallete['windowcolor'],highlightthickness=2)
		self.cf.place(anchor = NW,relx=0.049,rely=0.148,relwidth=0.851,relheight=0.699)
		self.c = Canvas(master = self.cf,bg = "#FFFFFF")
		self.c.custom_mem = {}
		self.c.place(anchor = NW,relwidth=1,relheight=1)
		#toolbar menu
		self.toolbar = Frame(master,padx=0,pady=0,highlightbackground=pallete['bordercolor'],bg=pallete['windowcolor'],highlightthickness=2)
		self.toolbar.place(anchor = NW,relx=0.00,rely=0.148,relwidth=0.05,relheight=0.7)
		self.FOButton = TransparentImageButton(self.toolbar,relx = 0.5,anchor = N,function = self.create_FO,scale = 0.2)
		#self.PinButton = TransparentImageButton(self.toolbar,relx = 0.5,rely = 0.15,anchor = N,function = self.create_pin,fp = "GUI/pin-open.png",scale=0.1)#create_pin needs changed to create_FO
		#TransparentImageButton(self.toolbar,relx = 0.5,anchor = N,function = self.create_FO)
		self.widgets = []
		global viewport, data
		viewport = self.c
		data['viewport'] = viewport







		self.create_reroute(event = None)
		#"""
		#"""
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
				"bg": pallete['windowcolor']
			},
			"PackParams":{
				"anchor": NW,
				"relx": 0,
				"rely": 0
			},
			"PackType": None #optional
		}
		#-----------------------------------------------------------
		#if arguments are empty, default settings are assumed
		if kwargs == {}:
			kwargs = default
		#-----------------------------------------------------------
		#need: stock widget --> needs only widget parameters, custom --> pass all parameters
		IsCustom = not hasattr(kwargs["Widget"],"pack")
		if IsCustom:#Is a custom widget
			w = kwargs["Widget"](**kwargs)
		else:#is a Tkinter default widget
			w = kwargs["Widget"](**kwargs["WidgetParams"])
			if "PackType" in kwargs.keys():
				if kwargs['PackType'] == 'pack':#type = pack
					w.pack(**kwargs['PackParams'])
				elif kwargs['PackType'] == 'place':#type = place
					w.place(**kwargs['PackParams'])
				else:#type is None or invalid
					print("Invalid PackType: this may be the cause of an issue")
					w.place(**kwargs['PackParams'])
			else:#PackType does not exist
				w.place(**kwargs['PackParams'])
				









		self.widgets.append(w)
		return w
	def create_FO(self,event):
		settings = {# a peek at the default argument structure
			"Widget": FileOpener,
			"WidgetParams": {
				"master": self.c,
				"width": 100,
				"height": 100,
				"bg": None
			},
			"PackParams":{
				"anchor": NW,
				"x": 0,
				"y": 0,
				"relx": 0,
				"rely": 0
			}
		}
		w = self.add_widget(**settings)
	def create_pin(self, event):
		settings = (
			{
				"Widget": Pin,
				"WidgetParams":{
					"master": self.c,
					"width": 25,
					"height": 25,
					"bg": None
				},
				"PackParams":{
					"anchor": NW,
					"x": 80,
					"y": 80
				},
				"AdditionalParams":{
					"direction": 'out' #Default
				}
			}
		)
		w = self.add_widget(**settings)
	def create_reroute(self, event):
		settings = (
			{
				"Widget": Reroute,
				"WidgetParams":{
					"master": self.c,
					"width": 25,
					"height": 25,
					"bg": None
				},
				"PackParams":{
					"anchor": NW,
					"x": 80,
					"y": 80
				},
			}
		)
		w = self.add_widget(**settings)
		

		

		


if __name__ == "__main__":
	#Image initializaton (Needs to be after Tk() is created)
	window.geometry("1360x768")
	app = Application(window)
	window.after(1,task)
	window.mainloop()