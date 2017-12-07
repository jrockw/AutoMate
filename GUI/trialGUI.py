#!/usr/bin/python
from Tkinter import *
import ttk
#################
TEXTBOX_ACTIVATED = False # flag to indicate 

#################

# This function is called whenever a key is released
def typing(event):
   
    userInput = responseEntry.get("1.0",END) 
    conclusionText.delete("1.0", END)   # delete the text in our conclusion text widget
    conclusionText.insert(END, "What you have typed so far:"+ userInput[:-1] ) 

def clearText(event):
    global TEXTBOX_ACTIVATED
    # removes 'Type here text'
    if(not TEXTBOX_ACTIVATED):
        responseEntry.delete("1.0", END)
        TEXTBOX_ACTIVATED = True
def button1Pressed():
    responseEntry.insert(END, 'INSERT')


##################
root = Tk()
root.title('JackBot')
hello = Label(text="Enter your text here:")
hello.grid(row=1, sticky=W)


box_value = StringVar()
box = ttk.Combobox(root, textvariable=box_value, 
                        state='readonly')
box['value'] = ('French', 'Spanish', 'German', 'Italian')
box.current(0)
box.grid(column=0, row=0)


responseEntry = Text(width=40, height=3)
responseEntry.insert(END, 'Type here')
responseEntry.grid(row=2, sticky=E)
responseEntry.bind('<KeyRelease>', typing) # bind responseEntry to keyboard keys being released, and have it execute the function typing when this occurs
responseEntry.bind('<Button-1>', clearText)

option1 = Button(root, text='Enter', command=lambda: button1Pressed(), default=ACTIVE)    # and on button 
option1.grid(row=4, sticky=NW)

option2 = Button(root, text='Enter', command=lambda:0, default=ACTIVE)    # and on button 
option2.grid(row=4)

option3 = Button(root, text='Enter', command=lambda:0, default=ACTIVE)    # and on button 
option3.grid(row=4, sticky=NE)

conclusionText = Text(width=40, height=5)
conclusionText.insert(END, "What you have typed so far:")
conclusionText.grid(row=5, columnspan=2)





root.mainloop()
