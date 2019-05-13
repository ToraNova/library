#!/usr/bin/python3

from tkinter import Tk
from tkinter import Frame, Toplevel
from tkinter import Button, Label


class MainWindow(Frame):
	
	colorList = ['red','green','blue']

	def __init__(self,master):
		Frame.__init__(self,master)
		master.title("gooi sample")
		self.master = master
		self.buildElements()
		self.pack()
		self.cturn = 0
		
		self.master.after('1000',self.colorSwitch,self.colorList[self.cturn])

	def buildElements(self):
		frame0 = Frame(self)
		frame0.pack()
		label0 = Label(frame0,text="Hello Ting",height=3,width=30,fg='red',bg='white')
		label0.pack(fill='x',side='top')

		frame1 = Frame(frame0)
		frame1.pack(fill='x',side='top')
		
		self.label10 = Label(frame1,text="Hi",height=3,fg='red',bg='white')
		self.label11 = Label(frame1,text="Hi",height=3,fg='blue',bg='white')
		self.label12 = Label(frame1,text="Hi",height=3,fg='green',bg='white')

		self.label10.pack(fill='x',side='left',expand=True)
		self.label12.pack(fill='x',side='left',expand=True)
		self.label11.pack(fill='x',side='left',expand=True)

		button0 = Button(frame0, text="SubWindow",fg="blue",bg="white")
		button0.pack(fill='both',side='top')
		button0["command"] = self.formWindow

		button1 = Button(frame0, text="Exit",fg="red",bg="white")
		button1.pack(fill='both',side='top')
		button1["command"] = self.exit

	def formWindow(self):
		subwindow = SubWindow(self)

	def exit(self):
		self.master.destroy()
		exit(0)

	def colorSwitch(self,color):
		self.label10['fg'] = color
		self.label11['fg'] = color
		self.label12['fg'] = color
		self.cturn += 1
		if(self.cturn >= len(self.colorList)):
			self.cturn = 0

		self.master.after('1000',self.colorSwitch,self.colorList[self.cturn])
		

class SubWindow(Toplevel):
	def __init__(self,master):
		Toplevel.__init__(self,master)
		self.wm_title("gooi subsample")
		self.buildElements()
		
	def buildElements(self):
		frame0 = Frame(self)
		frame0.pack()
		label0 = Label(frame0,text="This is a sub window",height=3,width=30,fg='red',bg='white')
		label0.pack(fill='x',side='top')
		

if __name__ == "__main__":
	root = Tk()
	root.title("gooi sample")
	main_window = MainWindow(root)
	try:
		root.mainloop()
	except Exception as e:
		print(e)
	
