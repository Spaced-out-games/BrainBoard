from tkinter import *
from tkinter import ttk,PhotoImage
import tkinter
from PIL import Image, ImageTk

images = {
	"file": None
}

from matplotlib import container
def f():
	print("called!")
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
		#Toolbar

		self.toolbar = Frame(master,bg="#FF0000", height = 100,padx=0,pady=0)
		self.toolbar.place(anchor = NW,relx=0,rely=0,relwidth = 0.9,relheight = 0.15)

		#Canvas frame
		self.cf = Frame(master,bg="#0000FF",padx=0,pady=0)
		self.cf.place(anchor = NW,relx=0.05,rely=0.15,relwidth=0.85,relheight=0.7)

		#toolbar menu
		self.toolbar= Frame(master,bg="#00FF00",padx=0,pady=0)
		self.toolbar.place(anchor = NW,relx=0.00,rely=0.15,relwidth=0.05,relheight=0.7)

		b1 = Button(
			self.toolbar,
			compound=LEFT,
			text = "LSTM layer",
			command = f,
		)
		b1.pack(side=LEFT, padx = 0,pady = 0)

		

		



if __name__ == "__main__":
    window = Tk()
    window.geometry("1360x768")
    app = Application(window)
    window.mainloop()



