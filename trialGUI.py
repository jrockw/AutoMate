#!/usr/bin/python
from Tkinter import *
import ttk
from googletrans import Translator
from time import sleep
from ALL_LANGUAGES import *
from generate import *

#################
TEXTBOX_ACTIVATED = False # flag to indicate 
buttons = []
suggestions = ['Enter', 'Enter', 'Enter']
translatedSuggestion = ['Enter', 'Enter', 'Enter']
NATIVE_LANGUAGE = 'English'
translator = Translator()



#################

'''
This function creates the text box to receive user input.
The  text box is sensitive to keyboard input and 
'''
def initializeResponseEntry():
    responseEntry = Text(width=40, height=3)
    responseEntry.insert(END, 'Type here')
    responseEntry.grid(row=2, sticky=EW)
    responseEntry.bind('<KeyRelease>', typing)
    responseEntry.bind('<BackSpace>', blankButtons()) 
    responseEntry.bind('<Button-1>', clearText)
    return responseEntry


'''
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
    setButtonTexts()

    pass


def initializeButtons():
    option1 = Button(root, text='Enter', command=lambda: buttonPressed(0))    # and on button 
    option1.grid(row=4, sticky=NW)

    option2 = Button(root, text='Enter', command=lambda: buttonPressed(1))    # and on button 
    option2.grid(row=4)

    option3 = Button(root, text='Enter', command=lambda: buttonPressed(2))    # and on button 
    option3.grid(row=4, sticky=NE)

    buttons = [option1, option2, option3]
    return buttons


def setButtonTexts():

    global translatedSuggestions
    global suggestions
    global buttons

    translatedSuggestions = translate(suggestions)
    for i in range(3):
        buttons[i]["text"] = "("+ str(i+1) +")" + translatedSuggestions[i]

def blankButtons():
    global buttons
    for button in buttons:
        button["text"] = '      '
    pass

def buttonPressed(buttonNumber):
    global suggestions
    responseEntry.insert(END, suggestions[buttonNumber] + ' ')
    typing
    pass

def getSuggestions(wordList):
    s = models[0].getThreeChoices(wordList)
    print 'wordList', wordList
    print "suggestion are:", s
    return s
def translate(englishSuggestions):
    print englishSuggestions
    global translator
    global NATIVE_LANGUAGE
    nativeLanguageSuggestions = []
    for englishWord in englishSuggestions:
        nativeWord = translator.translate(englishWord, dest = NATIVE_LANGUAGE)
        nativeLanguageSuggestions.append(nativeWord.text)
    return nativeLanguageSuggestions

def typing(event):

    global suggestions
    global translatedSuggestions

    userInput = responseEntry.get("1.0",END)
    wordArray = userInput.split() 


    if(len(wordArray)>1 and userInput[-2] == ' '):
        suggestions = getSuggestions(wordArray)
        setButtonTexts()
        conclusionText.delete("1.0", END)
        conclusionText.insert(END, userInput.split()[-2:] ) 
        
    elif(len(userInput)>1 and userInput[-2].isdigit() and int(userInput[-2]) < 4):
            button = int(userInput[-2]) - 1
            responseEntry.delete(INSERT+"-1c")
            buttonPressed(button)

    else: 
        blankButtons()


def clearText(event):
    global TEXTBOX_ACTIVATED
    # removes 'Type here text'
    if(not TEXTBOX_ACTIVATED):
        responseEntry.delete("1.0", END)
        TEXTBOX_ACTIVATED = True


##################
print 'Loading data...'
models = trainConversationModels(CONVERDIRS)
print('Data successfully loaded')
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

