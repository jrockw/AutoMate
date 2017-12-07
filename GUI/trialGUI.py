#!/usr/bin/python
from Tkinter import *
import ttk
from googletrans import Translator
from time import sleep
from ALL_LANGUAGES import *

#################
TEXTBOX_ACTIVATED = False # flag to indicate 
buttons = []
suggestions = ['Enter', 'Enter', 'Enter']
translatedSuggestion = ['Enter', 'Enter', 'Enter']
NATIVE_LANGUAGE = 'English'
translator = Translator()



#################

# This function is called whenever a key is released

def initializeResponseEntry():
    responseEntry = Text(width=40, height=3)
    responseEntry.insert(END, 'Type here')
    responseEntry.grid(row=2, sticky=E)
    responseEntry.bind('<KeyRelease>', typing) 
    responseEntry.bind('<Button-1>', clearText)
    return responseEntry

'''
def initializeLangBox():
    box = ttk.Combobox(root, textvariable=NATIVE_LANGUAGE, 
                            state='active')
    box['value'] = ('English','French', 'Spanish', 'German', 'Italian')
    box.current(0)
    print box.get()
    box.current(1)
    print box.get()
    box.grid(column=0, row=0, sticky = EW)
    box.bind('<<ComboboxSelected>>', selectNativeLanguage(box.get()))
'''   
def initializeLangBox():
    options = ALL_LANGUAGES
    var = StringVar()
    var.set('English')
    box = OptionMenu(root, var, *options, command = updateLangValue)           
    box.grid(column=0, row=0, sticky = W)


def updateLangValue(value):
    global NATIVE_LANGUAGE
    NATIVE_LANGUAGE = value 
    print 'updateLangValue to '+ NATIVE_LANGUAGE

    pass


def initializeButtons():
    option1 = Button(root, text='Enter', command=lambda: buttonPressed(0), default=ACTIVE)    # and on button 
    option1.grid(row=4, sticky=NW)

    option2 = Button(root, text='Enter', command=lambda: buttonPressed(1), default=ACTIVE)    # and on button 
    option2.grid(row=4)

    option3 = Button(root, text='Enter', command=lambda: buttonPressed(2), default=ACTIVE)    # and on button 
    option3.grid(row=4, sticky=NE)

    buttons = [option1, option2, option3]
    return buttons


def setButtonTexts(translatedSuggestions):

    global buttons
    for i in range(3):
        buttons[i]["text"] = translatedSuggestions[i]

def buttonPressed(buttonNumber):
    global suggestions
    print NATIVE_LANGUAGE
    responseEntry.insert(END, suggestions[buttonNumber])
    pass
def getSuggestions(lastTwoWords):
    
    return ['How', 'are', 'you']

def translate(englishSuggestions):
    print englishSuggestions
    global translator
    global NATIVE_LANGUAGE
    print ' Native language is:'+ NATIVE_LANGUAGE
    nativeLanguageSuggestions = []
    for englishWord in englishSuggestions:
        nativeWord = translator.translate(englishWord, dest = NATIVE_LANGUAGE)
        nativeLanguageSuggestions.append(nativeWord.text)
        print englishWord + ':' + nativeWord.text
    print nativeLanguageSuggestions
    return nativeLanguageSuggestions

def typing(event):

    global suggestions
    global translatedSuggestions

    userInput = responseEntry.get("1.0",END)
    wordArray = userInput.split() 


    if(len(wordArray)>1 and userInput[-2] == ' '):
        suggestions = getSuggestions(wordArray)
        translatedSuggestions = translate(suggestions)
        setButtonTexts(translatedSuggestions)
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
hello.grid(row=1, sticky=EW)



LangBox = initializeLangBox()
responseEntry = initializeResponseEntry()
buttons = initializeButtons()


conclusionText = Text(width=40, height=5)
conclusionText.insert(END, "What you have typed so far:")
conclusionText.grid(row=5, columnspan=2)

root.mainloop()

