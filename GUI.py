#!/usr/bin/python
from Tkinter import *
from ScrolledText import ScrolledText
import ttk
from googletrans import Translator
from time import sleep
from ALL_LANGUAGES import *
from generate import *

#################
'''
Global variables are declared here.
'''
TEXTBOX_ACTIVATED = False # flag to indicate whether user has clicked text box for first time
buttons = [] # list to hold button objects
suggestions = ['Enter', 'Enter', 'Enter'] # list to hold the suggestions in English
translatedSuggestion = ['Enter', 'Enter', 'Enter'] #list to hold translated suggestions
NATIVE_LANGUAGE = 'English' # holds native language as selected by user
translator = Translator() # translator object created using googletrans API



#################

'''
This function creates the text box to receive user input.
The  text box is sensitive to keyboard input and 
'''
def initializeResponseEntry():
    responseEntry = ScrolledText(width=40, height=6, relief=GROOVE)
    responseEntry.insert(END, 'Type here')
    responseEntry.grid(row=2, sticky=EW, padx=50)
    responseEntry.bind('<KeyRelease>', typing)
    responseEntry.bind('<BackSpace>', blankButtons()) 
    responseEntry.bind('<Button-1>', clearText)
    return responseEntry


'''
This function initializes the language selection menu
'''

def initializeLangBox():
    options = ALL_LANGUAGES
    var = StringVar()
    var.set('English')
    box = OptionMenu(root, var, *options, command = updateLangValue)           
    box.grid(column=0, row=0)


'''
This function changes the value of NATIVE_LANGUAGE
'''
def updateLangValue(value):
    global NATIVE_LANGUAGE
    NATIVE_LANGUAGE = value
    setButtonTexts()

    pass
'''
Creates a list of buttons and stores them in buttons[]
'''

def initializeButtons():
    option1 = Button(root, text='Enter', command=lambda: buttonPressed(0))    # and on button 
    option1.grid(row=4, sticky=NW, padx=50)

    option2 = Button(root, text='Enter', command=lambda: buttonPressed(1))    # and on button 
    option2.grid(row=4)

    option3 = Button(root, text='Enter', command=lambda: buttonPressed(2))    # and on button 
    option3.grid(row=4, sticky=NE, padx=50)

    buttons = [option1, option2, option3]
    return buttons

'''
Updates the text on the buttons with the translated suggestions
'''
def setButtonTexts():

    global translatedSuggestions
    global suggestions
    global buttons

    translatedSuggestions = translate(suggestions)
    for i in range(3):
        if (translatedSuggestions[i] == ''):
            buttons[i]["text"] = ''
        else:
            buttons[i]["text"] = "("+ str(i+1) +")  " + translatedSuggestions[i]

def blankButtons():
    global buttons
    for button in buttons:
        button["text"] = '      '
    pass

'''
Inserts the English equivalent of the button pressed into the text entry
'''

def buttonPressed(buttonNumber):
    global suggestions
    responseEntry.insert(END, suggestions[buttonNumber] + ' ')
    typing(1)
    pass
'''
Passes the list of words the user has typed so far and expects suggestions from the getThreeChoices() function
'''
def getSuggestions(wordList):
    #print '1:Getting suggestions...'
    try:
        s = selectChoices(models, wordList)
        if(len(s) != 3):
            #print 'Didnt get three suggestions'
            s = ['','','']

    except:
        #print 'exception called'
        return['','','']

    #print 'wordList', wordList
    #print "suggestion are:", s
    return s

'''
Takes the list of english suggestions and returns the translated suggestions
'''
def translate(englishSuggestions):
    global translator
    global NATIVE_LANGUAGE
    nativeLanguageSuggestions = []
    for englishWord in englishSuggestions:
        nativeWord = translator.translate(englishWord, dest = NATIVE_LANGUAGE)
        nativeLanguageSuggestions.append(nativeWord.text)
    return nativeLanguageSuggestions

'''
This function is triggered whenever the user types or presses a button.
'''
def typing(event):
    global suggestions
    global translatedSuggestions

    userInput = responseEntry.get("1.0",END)
    #print '------------'
    #print 'userInput', userInput
    wordArray = userInput.split() 

    if(len(userInput) == 1 or (len(userInput)>1 and userInput[-2] == ' ') ):
        suggestions = getSuggestions(wordArray)
        #print '2: Got suggestions...'
        setButtonTexts()
    
    # this case is executed when the user types 1,2, or 3. The corresponding button text is inserted    
    elif(len(userInput)>1 and userInput[-2].isdigit() and int(userInput[-2]) < 4):

            button = int(userInput[-2]) - 1
            responseEntry.delete(INSERT+"-1c")
            buttonPressed(button)

    else: 
        blankButtons()

'''
Clears the starting message when user first activates the text entry box     
'''
def clearText(event):
    global TEXTBOX_ACTIVATED
    # removes 'Type here text'
    if(not TEXTBOX_ACTIVATED):
        responseEntry.delete("1.0", END)
        TEXTBOX_ACTIVATED = True
        typing(1)


##################
'''
All the GUI functions are called here.
'''
print 'Loading data...'
models = trainConversationModels(CONVERDIRS)
print('Data successfully loaded')
print ('Please use the GUI!')
root = Tk()
root.title('JackBot')
root.geometry("400x200+150+150")
lightGreen = '#%02x%02x%02x' % (255, 173, 164)
root.configure(background=lightGreen)
root.tk_setPalette(background=lightGreen)
langLabel = Label(text = "Enter native language:")
langLabel.grid(column=0, row=0, sticky=W)
hello = Label(text="Enter your text here:")
hello.grid(row=1, sticky=W)
langSelect = Label(text="Select language:")
langSelect.grid(row=0, sticky=W)



LangBox = initializeLangBox()
responseEntry = initializeResponseEntry()
buttons = initializeButtons()


root.mainloop()
################
