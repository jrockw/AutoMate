import random
from nGramModel import *
import operator

class BigramModel(NGramModel):

    def __init__(self):
        """
        Requires: nothing
        Modifies: self (this instance of the BigramModel object)
        Effects:  this is the BigramModel constructor, which is done
                  for you. It allows BigramModel to access the data
                  from the NGramModel class by calling the NGramModel
                  constructor.
        """
        super(BigramModel, self).__init__()

    def trainModel(self, text):
        """
        Requires: text is a list of lists of strings
        Modifies: self.nGramCounts, a two-dimensional dictionary. For examples
                  and pictures of the BigramModel's version of
                  self.nGramCounts, see the spec.
        Effects:  this function populates the self.nGramCounts dictionary,
                  which has strings as keys and dictionaries of
                  {string: integer} pairs as values.

                  Note: make sure to use the return value of prepData to
                  populate the dictionary, which will allow the special
                  symbols to be included as their own tokens in
                  self.nGramCounts. For more details, see the spec.
        """
        self.nGramCounts = {}
        text = self.prepData(text)
        for a in text:
            for i in range(0,len(a)-1):

                if (a[i] in self.nGramCounts): 

                    if(a[i+1] in self.nGramCounts[a[i]]):
                        self.nGramCounts[a[i]][a[i+1]] += 1
                    else:
                        self.nGramCounts[a[i]][a[i+1]] = 1

                else :
                    self.nGramCounts[a[i]] = {}
                    self.nGramCounts[a[i]][a[i+1]] = 1

    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings, and len(sentence) >= 1
        Modifies: nothing
        Effects:  returns True if this n-gram model can be used to choose
                  the next token for the sentence. For explanations of how this
                  is determined for the BigramModel, see the spec.
        """
        for i in self.nGramCounts:
          if i == sentence[-1]:
            return True
        return False
        pass

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings, and trainingDataHasNGram
                  has returned True for this particular language model
        Modifies: nothing
        Effects:  returns the dictionary of candidate next words to be added
                  to the current sentence. For details on which words the
                  BigramModel sees as candidates, see the spec.
        """
        D = {}
        if sentence[-1] in self.nGramCounts:
          for i in self.nGramCounts[sentence[-1]]:
                D[i] = self.nGramCounts[sentence[-1]][i]
        #D['.'] = D.pop('$:::$')
        return D
        pass



    def getThreeChoices(self, sentence):
        allChoices = self.getCandidateDictionary(sentence)
        poss = []
        sorted_allChoices = sorted(allChoices.items(), key = operator.itemgetter(1))
        if len(sorted_allChoices) >= 1:
            poss.append(sorted_allChoices[-1][0])
        if len(sorted_allChoices) >= 2:    
            poss.append(sorted_allChoices[-2][0])
        if len(sorted_allChoices) >= 3:
            poss.append(sorted_allChoices[-3][0])
        for i in range(0, len(poss)):
            if poss[i] == '$:::$':
                poss[i] = '.'
        numOptions = len(poss)
        if numOptions < 3:
            for p in range(0, 3 - numOptions):
                poss.append("");
        return poss


        

###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    # Add your test cases here
    text = [ ['the', 'quick', 'brown', 'fox'], ['the', 'lazy', 'dog'] ]
    sentence1 = [ 'quick', 'brown', 'fox']
    sentence2 = [ 'lazy', 'quick']
    sentence3 = ['brown', 'fox']
    sentence4 = ['quick', 'fat']
    bigramModel = BigramModel()
    print(bigramModel)

    print 'Testing bigram trainModel'

    print 'Test 1'
    bigramModel.trainModel(text)
    print bigramModel.nGramCounts

    print 'Test 2'
    text.append(sentence1)
    bigramModel.trainModel(text)
    print bigramModel.nGramCounts

    print 'Test 3'
    text.append(sentence2)
    bigramModel.trainModel(text)
    print bigramModel.nGramCounts


    print bigramModel.trainingDataHasNGram(sentence1)
    sentence3 = ['the']
    print bigramModel.getCandidateDictionary(sentence3)
    song4_lh = [
    ('g2', 8), ('f#2', 8),
    ('e2*', 4), ('a2', 4), ('b2', 4), ('a2', 4),
    ('g2*', 4), ('f#2', 4), ('e2', 4), ('f#2', 4),
    ('g2*', 4), ('a2', 4), ('b2', 4), ('a2', 4),
    ('g2*', 4), ('b2', 4), ('e2', 8), ('f#2', 8), ('g2', 8), ('f#2', 8),
    ('e2*', 4), ('a2', 4), ('b2', 4), ('a2', 4),
    ('g2*', 4), ('f#2', 4), ('e2', 4), ('f#2', 4),
    ('g2*', 4), ('c3', 4), ('d3', 4), ('d3', 4),
    ('b2*', -2),
    ]

    keys_s = ['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']
    bigramMusic = BigramModel()
    print bigramMusic.getNextNote(song4_lh, keys_s)

    print 'Testing bigram trainingDataHasNGram'

    print 'Test 1'
    print 'Test 1 should return True'
    print bigramModel.trainingDataHasNGram(sentence1)

    print 'Test 2'
    print 'Test 2 should return False'
    print bigramModel.trainingDataHasNGram(sentence4)
    
    print 'Test 3'
    print 'Test 3 should return True'
    print bigramModel.trainingDataHasNGram(sentence3)

    print 'Testing getThreeChoices'
    print bigramModel.getThreeChoices(sentence1)












