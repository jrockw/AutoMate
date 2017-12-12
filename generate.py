#!/usr/bin/env python
import sys
sys.dont_write_bytecode = True # Suppress .pyc files
import operator
from data.dataLoader import *
from models.musicInfo import *
from models.unigramModel import *
from models.bigramModel import *
from models.trigramModel import *



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
# Reach
###############################################################################

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


PROMPT = """
(1) Generate word suggestions

> """
""
def main():
    models = []
    print('Starting program and loading data...')
    models = trainConversationModels(CONVERDIRS)
    print('Data successfully loaded')
    print('Testing selectChoices...')
    sentence1 = ['are', 'you', 'today']
    sentence2 = ['the', 'xylophone']
    print(selectChoices(models, sentence1))
    print(selectChoices(models, sentence2))
    
if __name__ == '__main__':
    main()
    
    






