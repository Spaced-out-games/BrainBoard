from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk


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
		#self.cf = Frame(master,bg="#0000FF",padx=0,pady=0)
		#self.cf.place(anchor = NW,relx=0.05,rely=0.15,relwidth=0.85,relheight=0.7)

		#toolbar menu
		self.toolbar= Frame(master,bg="#00FF00",padx=0,pady=0)
		self.toolbar.place(anchor = NW,relx=0.00,rely=0.15,relwidth=0.5,relheight=0.7)
		
		#fileicon = fileicon.subsample()
		self.buttons = {
			"file":Button(master=self.toolbar,image=images.get("file"), compound=LEFT)
		}
		k = list(self.buttons.keys())
		for i in k:
			c= self.buttons.get(i)
			c.pack(side=LEFT)

		

		


if __name__ == "__main__":
	window = Tk()
	#Image initializaton (Needs to be after Tk() is created)
	images = {
		"file":Image(fp="GUI/file_img.png")
	}
	window.geometry("1360x768")
	app = Application(window)
	window.mainloop()



