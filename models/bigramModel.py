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
        """
        numOptions = len(poss)
        if numOptions < 3:
            for p in range(0, 3 - numOptions):
                poss.append("");
        """
        return poss


        

###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    # Add your test cases here
    print 'Testing getThreeChoices'
    print bigramModel.getThreeChoices(sentence1)












