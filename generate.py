#!/usr/bin/env python
import sys
sys.dont_write_bytecode = True # Suppress .pyc files
import operator
import random
from pysynth import pysynth
from data.dataLoader import *
from models.musicInfo import *
from models.unigramModel import *
from models.bigramModel import *
from models.trigramModel import *
import json
#import ujson
import pickle
from contextlib import closing
import shelve
import cPickle as pickle
import nltk


# FIXME Add your team name
TEAM = 'trAIn'
LYRICSDIRS = ['the_beatles']
MUSICDIRS = ['gamecube']
CONVERDIRS = ['conversations']
WAVDIR = 'wav/'

###############################################################################
# Helper Functions
###############################################################################

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

def selectChoices(models, sentence):
    choices = models[0].getThreeChoices(sentence)
    if len(choices) != 3:
        for i in range(0, 1):
            if len(choices) == 0:
                choices = models[i+1].getThreeChoices(sentence)
            elif len(choices == 1):
                choices[1] = models[i+1].getThreeChoices(sentence)
                choices[2] = models[i+1].getThreeChoices(sentence)
            elif len(choices == 2):
                choices[2] = models[i+1].getThreeChoices(sentence)
    return choices


###############################################################################
# Reach
###############################################################################

PROMPT = """
(1) Generate word suggestions

> """
""
def main():
    models = []
    """
    Requires: Nothing
    Modifies: Nothing
    Effects:  This is your main function, which is done for you. It runs the
              entire generator program for both the reach and the core.

              It prompts the user to choose to generate either lyrics or music.
    """
    # FIXME uncomment these lines when ready
    print('Starting program and loading data...')
    models = trainConversationModels(CONVERDIRS)
    print('Data successfully loaded')
    print('Testing selectChoices...')
    sentence1 = ['I', 'am', 'the']
    sentence2 = ['the', 'xylophone']
    print(selectChoices(models, sentence1))
    print(selectChoices(models, sentence2))
    #print models[2].getThreeChoices(sentence1)
    """
    print ('Storing data...')
    json.dump(models[0].getDict(), open('trigramData.json', 'wb'))
    print('Stored data!')
    print('Getting data...')
    data = json.load(open('trigramData.json'))
    print('Got data!')
    """
    """
    sentence1 = ['baby', 'I', 'love']
    sentence2 = ['whats', 'the']
    sentence3 = ['hello']
    print models[0].getThreeChoices(sentence1)
    print models[2].getThreeChoices(sentence3)
    """



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
    #print 'Hello'
    #models = []
    #models = trainLyricsModels(LYRICSDIRS)
    #models = trainConversationModels(CONVERDIRS)
    """
    print 'yooo'
    with open('models[0].getDict()_dictionary.pickle', 'wb') as handle:
        pickle.dump(models[0].getDict(), handle)
        print 'Done!'

    with open('models[0].getDict()_dictionary.pickle', 'wb') as handle:
        models[0].setDict(pickle.load(handle))
    """






