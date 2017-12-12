import random
from nGramModel import *
import operator

class TrigramModel(NGramModel):

    def __init__(self):
        """
        Requires: nothing
        Modifies: self (this instance of the NGramModel object)
        Effects:  this is the TrigramModel constructor, which is done
                  for you. It allows TrigramModel to access the data
                  from the NGramModel class.
        """
        super(TrigramModel, self).__init__()

    def trainModel(self, text):
        """
        Requires: text is a list of lists of strings
        Modifies: self.nGramCounts, a three-dimensional dictionary. For
                  examples and pictures of the TrigramModel's version of
                  self.nGramCounts, see the spec.
        Effects:  this function populates the self.nGramCounts dictionary,
                  which has strings as keys and dictionaries as values,
                  where those inner dictionaries have strings as keys
                  and dictionaries of {string: integer} pairs as values.

                  Note: make sure to use the return value of prepData to
                  populate the dictionary, which will allow the special
                  symbols to be included as their own tokens in
                  self.nGramCounts. For more details, see the spec.
        """
        self.nGramCounts = {}
        text = self.prepData(text)
        for a in text:
            for i in range(0,len(a)-2):

                if (a[i] in self.nGramCounts): 

                    if(a[i+1] in self.nGramCounts[a[i]]):
                        if(a[i+2] in self.nGramCounts[a[i]][a[i+1]]):
                            self.nGramCounts[a[i]][a[i+1]][a[i+2]] += 1
                        else:
                            self.nGramCounts[a[i]][a[i+1]][a[i+2]] = 1
                    else:
                        self.nGramCounts[a[i]][a[i+1]] = {}
                        self.nGramCounts[a[i]][a[i+1]][a[i+2]] = 1

                else :
                    self.nGramCounts[a[i]] = {}
                    self.nGramCounts[a[i]][a[i+1]] = {}
                    self.nGramCounts[a[i]][a[i+1]][a[i+2]] = 1

    def copyModel(self):
        lines = []
        with open('w3.txt') as f:
            #lines = f.readlines()
            for line in lines: 
                line = line.strip() 
                lines.append(line)
                print line 
    pass


    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings, and len(sentence) >= 2
        Modifies: nothing
        Effects:  returns True if this n-gram model can be used to choose
                  the next token for the sentence. For explanations of how this
                  is determined for the TrigramModel, see the spec.
        """
        if sentence[-2] in self.nGramCounts:
            if sentence[-1] in self.nGramCounts[sentence[-2]]:
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
                  TrigramModel sees as candidates, see the spec.
        """
        """
        D = {}
        for i in self.nGramCounts:
<<<<<<< HEAD
          if i == sentence[-2]:
            print 'hey'
            print 'printing ngramcount',  self.nGramCounts[i]
            for j in self.nGramCounts[i]:
              if j == sentence[- 1]:
                D[self.nGramCounts[i]] = self.nGramCounts[i][j]
                print 'yo'
        return D
        """
        D = {}
        if sentence[-2] in self.nGramCounts:
            if sentence[-1] in self.nGramCounts[sentence[-2]]:
              for i in self.nGramCounts[sentence[-2]][sentence[-1]]:
                D[i] = self.nGramCounts[sentence[-2]][sentence[-1]][i]
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
    # Add your tests here
    text = [ ['the', 'quick', 'brown', 'fox'], ['the', 'lazy', 'dog'] ]
    sentence = [ 'the', 'quick', 'brown']
    sentence2 = [ 'the', 'fat', 'bat']
    sentence3 = ['the', 'quick']
    sentence3 = ['quick', 'brown', 'fox']
    '''Testing trainModel'''
    print 'Testing trigram trainModel'
    trigramModel = TrigramModel()
    print(trigramModel)
    
    print 'Test 1'
    trigramModel.trainModel(text)
    print trigramModel.nGramCounts

    print 'Test 2'
    text.append(sentence)
    trigramModel.trainModel(text)
    print trigramModel.nGramCounts

    print 'Test 3'
    text.append(sentence2)
    trigramModel.trainModel(text)
    print trigramModel.nGramCounts

    '''
    Testing trainingDataHasNGram
    '''
    print 'Testing trigram trainingDataHasNGram'

    print 'Test 1'
    print 'Test 1 should return True'
    print trigramModel.trainingDataHasNGram(sentence)

    print 'Test 2'
    print 'Test 2 should return False'
    print trigramModel.trainingDataHasNGram(sentence2)
    
    '''
    Testing getCandidateDictionary
    '''
    print 'testing getCandidateDictionary'
    text2 = [ ['the', 'quick', 'brown', 'fox'], ['the', 'quick', 'brown'], ['the', 'quick', 'green'] ]
    print trigramModel.getCandidateDictionary(sentence3)
    text.append(sentence)
    print 'test complete'
