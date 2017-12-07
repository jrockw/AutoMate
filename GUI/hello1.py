from Tkinter import * 
import os
class Dialog(Toplevel):

	def __init__(self, parent, title = None):

		Toplevel.__init__(self, parent)
		self.transient(parent)

		if title:
			self.title(title)

		self.parent = parent

		self.result = None

		body = Frame(self)
		self.initial_focus = self.body(body)
		body.pack(padx=5, pady=5)

		self.buttonbox()

		self.grab_set()

		if not self.initial_focus:
			self.initial_focus = self

		self.protocol("WM_DELETE_WINDOW", self.cancel)

		self.geometry("+%d+%d" % (parent.winfo_rootx()+50, parent.winfo_rooty()+50))

		self.initial_focus.focus_set()

		self.wait_window(self)
	def body(self, master):

		pass
	def buttonbox(self):

		box = Frame(self)

		w = Button(box, text="Enter", width=10, command=self.ok, default=ACTIVE)
		w.pack(side=LEFT, padx=5, pady=5)
		w = Button(box, text="Exit", width=10, command=self.cancel)
		w.pack(side=LEFT, padx=5, pady=5)

		self.bind("<return>", self.ok)
		self.bind("<Escape>", self.cancel)

		box.pack()

	def ok(self, event=None):

		if not self.validate():
			self.initial_focus.focus_set()
			return

		self.withdraw()
		self.update_idletasks()
		self.apply()
		self.cancel()

	def cancel(self, event=None):
		self.parent.focus_set()
		self.destroy()

	def validate(self):
		return 1

	def appy(self):
		pass

class MyDialog(Dialog):

	def body(self, master):

		Label(master, text="Type here:").grid(row=0)

		self.e = Entry(master)

		self.e.grid(row=0, column=1)
		return self.e

	def apply(self):
		sentence = int(self.e.get())
		print sentence

root = Tk()
d = MyDialog(root)
root.wait_window(d.top)
