from pydoc import visiblename
from tkinter import *
from tkinter import ttk
from general import avgpts, p3d
from PIL import Image, ImageTk
import math as m

global_scale = 1
widgets = {
    "FileOpener": []
}  # list of all drag-drop widgets


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


class Pin(Frame):
    def __init__(self, parent):
        self.canvas = Canvas(parent)


def f():  # placeholder function
    pass



class FileOpener(Frame):
    def __init__(self, parent):
        #super().__init__(self, parent)
        self.parent = parent
        # Default Class attributes
        self.input = None  # Input data, from block A
        self.output = None  # Output data, for block C
        self.input_node = None  # Another Block reference
        self.output_node = None  # Another Block reference
        self.frame = Frame(parent,width=100,height = 1000)
        self.frame.pack()
        self.frame.place(x=0, y=0)
        self.canvas = Canvas(self.frame)
        self.canvas.grid(column=0, row=0, sticky=(N, W, E, S))
        self.canvas.config(width=1000,height = 1000)
        #self.canvas.pack()
        self.button = Button(master=self.frame)
        self.native_image_size = (148,226)
        make_draggable(self.canvas)
        #w,h = image.width,image.height
        #w,h = int(w * self.scale),int(h * self.scale)
        #image = image.resize((w,h))

        # """
        # Creating an image, and drawing it on frame
        #canvas size = (290,205)
        scale = 0.5
        self.image_size = (m.floor(self.native_image_size[0] * scale), m.floor(self.native_image_size[1] * scale))

        image = Image.open("Untitled-1.png")
        image = image.resize(self.image_size)
        self.img = ImageTk.PhotoImage(image)

        self.canvas.create_image(0, 0, image=self.img, anchor=NW, tags="image")
        self.canvas.create_oval(0,0,5,5,outline="#ff0000" )
        # """
        """																		EDITS GO BELOW															"""

        """																		EDITS GO ABOVE															"""

    def __recv__(self):
        if self.input != None and self.input_node != None:
            self.input = (self.input_node).output
        else:
            pass

    def __send__(self):
        if self.output_node != None and self.output != None:
            self.output_node.input = self.output
        else:
            pass

    def __proc__(self, **kwargs):
        self.recv()
        x = self.input
        # ...do some processing in respect to x
        file = open(x)
        # file proccessing done here
        self.output = file
        self.__send__()
        """																		EDITS GO BELOW															"""

        """																		EDITS GO ABOVE															"""
class Application(Frame, Tk):
    def __init__(self, master):
        super().__init__(master)
        #self.canvas = Canvas(master)
        # Menus
        self.menubar = Menu(master)  # maybe master insteas of self
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=f)
        self.filemenu.add_command(label="Open", command=f)
        self.filemenu.add_command(label="Save", command=f)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=master.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        ######
        self.spawn_FO()

        """
		GUI elements go here

		self.attr = tk.xxxxVar()
		self.attr.set(initial value)
		self.entry["xxxxVariable"] = self.attr
		self.entry.bind("<key>",self.method)
		"""

    def spawn_FO(self):
        widget = FileOpener(window)
        widgets["FileOpener"].append(widget)










"""
if __name__ ==  "__main__":
	window = Tk()
	canvas = Canvas(window)
	b = FileOpener(window)
	
	window.mainloop()
"""
if __name__ == "__main__":
    window = Tk()
    window.geometry("1024x768")
    window.columnconfigure(8, weight=8)
    window.rowconfigure(8, weight=1)
    app = Application(window)
    app.config(width = 100,height = 100)
    app.pack()
    #window.config(menu=app.menubar)
    window.mainloop()

    