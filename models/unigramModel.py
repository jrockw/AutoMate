import random
from nGramModel import *
import operator
import nltk
from nltk.corpus import brown 


class UnigramModel(NGramModel):

    def __init__(self):
        """
        Requires: nothing
        Modifies: self (this instance of the UnigramModel object)
        Effects:  this is the UnigramModel constructor, which is done
                  for you. It allows UnigramModel to access the data
                  in the NGramModel class by calling the NGramModel
                  constructor.
        """
        super(UnigramModel, self).__init__()

    def trainModel(self, text):
        """
        Requires: text is a list of lists of strings
        Modifies: self.nGramCounts
        Effects:  this function populates the self.nGramCounts dictionary,
                  which is a dictionary of {string: integer} pairs.
                  For further explanation of UnigramModel's version of
                  self.nGramCounts, see the spec.

                  Note: make sure to use the return value of prepData to
                  populate the dictionary, which will allow the special
                  symbols to be included as their own tokens in
                  self.nGramCounts. For more details, see the spec.
        """
        self.nGramCounts = {}
        text = self.prepData(text)
        for a in text:
            for b in a:
                if (b =='^::^' or b =='^:::^'):
                    pass
                elif (b in self.nGramCounts): 
                    self.nGramCounts[b] += 1
                else :
                    self.nGramCounts[b] = 1

        

    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings
        Modifies: nothing
        Effects:  returns True if this n-gram model can be used to choose
                  the next token for the sentence. For explanations of how this
                  is determined for the UnigramModel, see the spec.
        """
        if (len(self.nGramCounts) != 0):
            return True
        return False
        pass

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings, and trainingDataHasNgGram
                  has returned True for this particular language model
        Modifies: nothing
        Effects:  returns the dictionary of candidate next words to be added
                  to the current sentence. For details on which words the
                  UnigramModel sees as candidates, see the spec.
        """
        kList = []
        kList = self.nGramCounts.keys()
        for k in kList:
            if (k.startswith('l') and k[-1].isdigit()) or k[0].isdigit():
                self.nGramCounts.pop(k)
        return self.nGramCounts



    def getThreeChoices(self, sentence):
        poss = []
        allChoices = self.getCandidateDictionary(sentence) #allChoices is a dictionary
        #For testing
        #allChoices = {"a" : 5, "j" : 12, "f" : 8, "u" : 2, "b" : 20, "k" : 10}
        #sorted_allChoices = []
        #sorted_allChoices = sorted(self.getCandidateDictionary(sentence), key=self.getCandidateDictionary.get())
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
        return poss



###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    # Add your test cases here
    text = [ ['the', 'quick', 'brown', 'fox'], ['the', 'lazy', 'dog'] ]
    sentence = [ 'brown' ]
    sentence2 = ['brown', 'the', 'lazy']
    unigramModel = UnigramModel()
    print(unigramModel)

    print 'Testing unigram trainModel'

    print 'Test 1'
    unigramModel.trainModel(text)
    print unigramModel.nGramCounts

    print 'Test 2'
    text.append(sentence)
    unigramModel.trainModel(text)
    print unigramModel.nGramCounts

    print 'Test 3'
    text.append(sentence2)
    unigramModel.trainModel(text)
    print unigramModel.nGramCounts

    print 'Testing getCandidateDictionary'
    print (unigramModel.getCandidateDictionary(sentence))

    print 'Testing unigram trainingDataHasNGram'

    print 'Test 1'
    print 'Test 1 should return True'
    print unigramModel.trainingDataHasNGram(sentence)

    print 'Test 2'
    unigramModel.nGramCounts = {}
    print 'Test 2 should return False'
    print unigramModel.trainingDataHasNGram(sentence)

    unigramModel.trainModel(text)
    
    print 'Test 3'
    sentence4 = ['bob']
    print 'Test 3 should return True'
    print unigramModel.trainingDataHasNGram(sentence4)

    print "\nTesting getNextToken"
    testSentence1 = "Apples are really tasty and apples are really good especially when apples"
    testSentence2 = "I like to run and jog and swim and jog in the weather outside"
    testSentence3 = "Mountains have caves in them and lots of snow in the winter caves caves"
    print "\nTesting Sentence 1"
    for p in range(0,7):
      print unigramModel.getNextToken(testSentence1)

    print "\nTesting Sentence 2"
    for p in range(0,7):
      print unigramModel.getNextToken(testSentence2)

    print "\nTesting Sentence 3"
    for p in range(0,7):
      print unigramModel.getNextToken(testSentence3)


    print "\nTesting getThreeChoices"
    print unigramModel.getThreeChoices(testSentence1)
    #print unigramModel.getCandidateDictionary(testSentence1)



    print brown.words()







    
