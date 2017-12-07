#!/usr/bin/python
from Tkinter import *
import ttk
#################
TEXTBOX_ACTIVATED = False # flag to indicate 
buttons = []

#################

# This function is called whenever a key is released

def initializeResponseEntry():
    responseEntry = Text(width=40, height=3)
    responseEntry.insert(END, 'Type here')
    responseEntry.grid(row=2, sticky=E)
    responseEntry.bind('<KeyRelease>', typing) 
    responseEntry.bind('<Button-1>', clearText)
    return responseEntry

def initializeLangBox():
    box_value = StringVar()
    box = ttk.Combobox(root, textvariable=box_value, 
                            state='readonly')
    box['value'] = ('French', 'Spanish', 'German', 'Italian')
    box.current(0)
    box.grid(column=0, row=0, sticky = EW)

def initializeButtons():
    option1 = Button(root, text='Enter', command=lambda: buttonPressed(option1), default=ACTIVE)    # and on button 
    option1.grid(row=4, sticky=NW)

    option2 = Button(root, text='Enter', command=lambda: buttonPressed(option2), default=ACTIVE)    # and on button 
    option2.grid(row=4)

    option3 = Button(root, text='Enter', command=lambda: buttonPressed(option3), default=ACTIVE)    # and on button 
    option3.grid(row=4, sticky=NE)

    buttons = [option1, option2, option3]
    return buttons

def setButtonTexts(suggestions):
    global buttons
    for i in range(0,3):
        buttons[i]["text"] = suggestions[i]

def buttonPressed(button):
    responseEntry.insert(END, button["text"])
    pass
def getSuggestions(lastTwoWords):
    lastTwoWords.append('Third word')
    return lastTwoWords

def typing(event):
    userInput = responseEntry.get("1.0",END)
    wordArray = userInput.split() 

    if(len(wordArray)>1 and userInput[-2] == ' '):
        englishSuggestion = 
        setButtonTexts(getSuggestions(wordArray[-2:]))
        conclusionText.delete("1.0", END)
        conclusionText.insert(END, userInput.split()[-2:] ) 
        #conclusionText.insert(END, "User typed space" ) 
        #conclusionText.delete("1.0", END)   # delete the text in our conclusion text widget
        #conclusionText.insert(END, "What you have typed so far:"+ userInput[:-1] ) 

def clearText(event):
    global TEXTBOX_ACTIVATED
    # removes 'Type here text'
    if(not TEXTBOX_ACTIVATED):
        responseEntry.delete("1.0", END)
        TEXTBOX_ACTIVATED = True


##################
root = Tk()
root.title('JackBot')
hello = Label(text="Enter your text here:")
hello.grid(row=1, sticky=W)



LangBox = initializeLangBox()
responseEntry = initializeResponseEntry()
buttons = initializeButtons()


conclusionText = Text(width=40, height=5)
conclusionText.insert(END, "What you have typed so far:")
conclusionText.grid(row=5, columnspan=2)



root.mainloop()
