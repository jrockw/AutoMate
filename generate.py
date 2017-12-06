#!/usr/bin/env python
import sys
sys.dont_write_bytecode = True # Suppress .pyc files

import random
from pysynth import pysynth
from data.dataLoader import *
from models.musicInfo import *
from models.unigramModel import *
from models.bigramModel import *
from models.trigramModel import *
# FIXME Add your team name
TEAM = 'trAIn'
LYRICSDIRS = ['the_beatles']
MUSICDIRS = ['gamecube']
CONVERDIRS = ['Data']
WAVDIR = 'wav/'

###############################################################################
# Helper Functions
###############################################################################

def sentenceTooLong(desiredLength, currentLength):
    """
    Requires: nothing
    Modifies: nothing
    Effects:  returns a bool indicating whether or not this sentence should
              be ended based on its length. This function has been done for
              you.
    """
    STDEV = 1
    val = random.gauss(currentLength, STDEV)
    return val > desiredLength

def printSongLyrics(verseOne, verseTwo, chorus):
    """
    Requires: verseOne, verseTwo, and chorus are lists of lists of strings
    Modifies: nothing
    Effects:  prints the song. This function is done for you.
    """
    verses = [verseOne, chorus, verseTwo, chorus]
    print
    for verse in verses:
        for line in verse:
            print (' '.join(line)).capitalize()
        print

def trainLyricsModels(lyricDirs):
    """
    Requires: lyricDirs is a list of directories in data/lyrics/
    Modifies: nothing
    Effects:  loads data from the folders in the lyricDirs list,
              using the pre-written DataLoader class, then creates an
              instance of each of the NGramModel child classes and trains
              them using the text loaded from the data loader. The list
              should be in tri-, then bi-, then unigramModel order.

              Returns the list of trained models.
    """
    models = [TrigramModel(), BigramModel(), UnigramModel()]
    for ldir in lyricDirs:
        lyrics = loadLyrics(ldir)
        for model in models:
            model.trainModel(lyrics)
    return models


def trainConversationModels(converDirs):
    models = [TrigramModel(), BigramModel(), UnigramModel()]
    for cdir in converDirs:
        conversations = loadConvers(cdir)
        for model in models:
            model.trainModel(conversations)
    return models

###############################################################################
# Core
###############################################################################

def trainMusicModels(musicDirs):
    """
    Requires: lyricDirs is a list of directories in data/midi/
    Modifies: nothing

    Effects:  works exactly as trainLyricsModels, except that
              now the dataLoader calls the DataLoader's loadMusic() function
              and takes a music directory name instead of an artist name.
              Returns a list of trained models in order of tri-, then bi-, then
              unigramModel objects.
    """
    models = [TrigramModel(), BigramModel(), UnigramModel()]
    # call dataLoader.loadMusic for each directory in musicDirs
    for mdir in musicDirs:
        music = loadMusic(mdir)
        for model in models:
            model.trainModel(music)
    return models

    pass

def selectNGramModel(models, sentence):
    """
    Requires: models is a list of NGramModel objects sorted by descending
              priority: tri-, then bi-, then unigrams.
    Modifies: nothing
    Effects:  returns the best possible model that can be used for the
              current sentence based on the n-grams that the models know.
              (Remember that you wrote a function that checks if a model can
              be used to pick a word for a sentence!)
    """
    i = 0
    while i < len(models):
      if models[i].trainingDataHasNGram(sentence): 
        return models[i]
      i = i + 1
    return models[-1]
    pass

def generateLyricalSentence(models, desiredLength):
    """
    Requires: models is a list of trained NGramModel objects sorted by
              descending priority: tri-, then bi-, then unigrams.
              desiredLength is the desired length of the sentence.
    Modifies: nothing
    Effects:  returns a list of strings where each string is a word in the
              generated sentence. The returned list should NOT include
              any of the special starting or ending symbols.

              For more details about generating a sentence using the
              NGramModels, see the spec.
    """
    sentence = ['^::^', '^:::^']
    currentLength = 0
    while True:
        if (sentence[-1] == '$:::$'):
            return sentence[2:-1]
            
        if(sentenceTooLong(desiredLength, currentLength)):
            sentence.append('$:::$')
            return sentence[2:-1]

        

        sentence.append( selectNGramModel(models, sentence).getNextToken(sentence))
        currentLength +=1
    return sentence
    
    

def generateMusicalSentence(models, desiredLength, possiblePitches):
    """
    Requires: possiblePitches is a list of pitches for a musical key
    Modifies: nothing
    Effects:  works exactly like generateLyricalSentence from the core, except
              now we call the NGramModel child class' getNextNote()
              function instead of getNextToken(). Everything else
              should be exactly the same as the core.
    """

    
    sentence = ['^::^', '^:::^']
    currentLength = 0
    while True:

        if (sentence[-1] == '$:::$'):
            return sentence[2:-1]

        if(sentenceTooLong(desiredLength, currentLength)):
            sentence.append('$:::$')
            return sentence[2:-1]


        sentence.append( selectNGramModel(models, sentence).getNextNote(sentence, possiblePitches))
        currentLength +=1
    return sentence


  

def runLyricsGenerator(models):
    """
    Requires: models is a list of a trained nGramModel child class objects
    Modifies: nothing
    Effects:  generates a verse one, a verse two, and a chorus, then
              calls printSongLyrics to print the song out.
    """
    verseOne = []
    verseTwo = []
    chorus = []
    verse1DesiredLength = 12
    verse1DesiredLength = 12
    chorusDesiredLength = 7 #sentences in chorus can be shorter

    for i in range(0,4):
      verseOne.append(generateLyricalSentence(models, verse1DesiredLength))
      verseTwo.append(generateLyricalSentence(models, verse1DesiredLength))
      chorus.append(generateLyricalSentence(models, chorusDesiredLength)) 
      printSongLyrics(verseOne, verseTwo, chorus)

    pass

def runMusicGenerator(models, songName):
    """
    Requires: models is a list of trained models
    Modifies: nothing
    Effects:  runs the music generator as following the details in the spec.
    """
    desiredLength = 50

    possiblePitches = KEY_SIGNATURES[random.choice(KEY_SIGNATURES.keys())]
    tuplesList = tuple(generateMusicalSentence(models, desiredLength, possiblePitches))
    #print tuplesList
    pysynth.make_wav(tuplesList, fn=songName)


###############################################################################
# Reach
###############################################################################

PROMPT = """
(1) Generate song lyrics by The Beatles
(2) Generate a song using data from Nintendo Gamecube
(3) Quit the music generator
> """

def main():
    """
    Requires: Nothing
    Modifies: Nothing
    Effects:  This is your main function, which is done for you. It runs the
              entire generator program for both the reach and the core.

              It prompts the user to choose to generate either lyrics or music.
    """
    # FIXME uncomment these lines when ready
    print('Starting program and loading data...')
    lyricsModels = trainLyricsModels(LYRICSDIRS)
    musicModels = trainMusicModels(MUSICDIRS)
    converModels = trainConversationModels(CONVERDIRS)
    print('Data successfully loaded')
    print('Welcome to the ' + TEAM + ' music generator!')
    while True:
        try:
            userInput = int(raw_input(PROMPT))
            if userInput == 1:
                # FIXME uncomment this line when ready
                runLyricsGenerator(lyricsModels)
                #print("Under construction")
            elif userInput == 2:
                # FIXME uncomment these lines when ready
                songName = raw_input('What would you like to name your song? ')
                runMusicGenerator(musicModels, WAVDIR + songName + '.wav')
                #print("Under construction")
            elif userInput == 3:
                print('Thank you for using the ' + TEAM + ' music generator!')
                sys.exit()
            else:
                print("Invalid option!")
        except ValueError:
            print("Please enter a number")


if __name__ == '__main__':
    main()
    
    # note that if you want to individually test functions from this file,
    # you can comment out main() and call those functions here. Just make
    # sure to call main() in your final submission of the project!
    '''
    #TESTING

    print "Testing runLyricsGenerator"
    lyricsModels = trainLyricsModels(LYRICSDIRS)
    runLyricsGenerator(lyricsModels)

    print "Testing selectNGramModel"
    print 'Test case 1'
    sentence1 = [ 'the', 'quick', 'brown']
    print selectNGramModel(lyricsModels, sentence1)

    print "Test case 2"
    sentence2 = ['yellow', 'submarine'] 
    print selectNGramModel(lyricsModels, sentence2)

    print 'Testing generateLyricalSentence'
    print 'Test case 1'
    print generateLyricalSentence(lyricsModels, 5)

    print 'Test case 2'
    print generateLyricalSentence(lyricsModels, 7)
    '''


