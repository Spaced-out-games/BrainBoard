from genericpath import exists
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from jinja2 import is_undefined
from general import create_img
bordercolor = "#888888"
windowcolor = "#aaaaaa"

def f(event = None):
	print("called!")


frames = 0
lastw = 0
lasth = 0
#Tkinter Sub-process:
def task():
	#do some stuff
	global frames,lastw,lasth
	if frames == 0:
		lastw = window.winfo_width()
		lasth = window.winfo_height()
	else:
		if lastw != window.winfo_width() or lasth != window.winfo_height():
			#react
			#app object should not be called, as this results in a recursion error. Need to look into this
			w = app.winfo_width()
			h = app.winfo_height()
			x = w<<5
			print
			y = 0
			app.tc.moveto("FO",x,y)

			pass

	lastw = window.winfo_width()
	lasth = window.winfo_height()
	frames = frames + 1

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
		self.c.create_line(5,5,5,5,fill = "red")

		#toolbar menu
		self.toolbar = Frame(master,padx=0,pady=0,highlightbackground=bordercolor,bg=windowcolor,highlightthickness=2)
		self.toolbar.place(anchor = NW,relx=0.00,rely=0.148,relwidth=0.1,relheight=0.7)

		#Toolbar canvas
		self.tc = Canvas(self.toolbar)
		self.tc.place(anchor = NW,relwidth=1,relheight=1)

		#This code block creates a clickable canvas button, which calls f() when clicked

		self.FO_i = create_img(fp=r"GUI/file_img.png",scale = 0.5)
		self.FO_b = self.tc.create_image((50,50),image = self.FO_i,tags = ['FO'])
		self.tc.move("FO",0,0)
		

		self.tc.tag_bind(self.FO_b, "<Button-1>",self.test)
	def test(self, event):
		print(self.tc.winfo_width())

		

		


if __name__ == "__main__":
	window = Tk()
	#Image initializaton (Needs to be after Tk() is created)
	file = Image.open("GUI/file_img.png")# actual size = 148 × 226(w:h = 0.65487)
	file = file.resize(size = (40, 60))
	file = ImageTk.PhotoImage(file)
	window.geometry("1360x768")
	app = Application(window)
	window.after(1,task)
	window.mainloop()



