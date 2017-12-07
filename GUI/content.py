from Tkinter import *
import os

class Quitter(Frame):                          # subclass our GUI
    def __init__(self, parent=None):           # constructor method
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(side=LEFT)
    def quit(self):
        Frame.quit(self)
     
def fetch():
    print 'Input => "%s"' % ent.get()              # get text
     
root = Tk()
ent = Entry(root)
root.geometry('450x450+500+300')
root.title('JackBot')
ent.insert(0, 'Start typing...')                   # set text
ent.pack(fill=X, pady=50, padx=25)                         # grow horiz

photo = PhotoImage(file="robobot.ppm")
robo = Label(root, image=photo)
robo.image = photo
robo.pack(side=TOP)

ent.focus()                                        # save a click
ent.bind('<Return>', (lambda event: fetch()))      # on enter key
btn = Button(root, text='Enter', command=fetch, default=ACTIVE)    # and on button 
btn.pack(side=RIGHT)
Quitter(root).pack(side=LEFT)
root.mainloop()