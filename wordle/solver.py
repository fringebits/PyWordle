
import random
import re
import os

class Solver:
    letters = ['e', 'a', 'r', 'o', 't', 'l', 'i', 's', 'n', 'c']

    def __init__(self):
        filename = os.path.join(os.path.dirname(__file__), 'five-letter-words.txt')
        f = open(filename, 'r')
        self.words = [line.strip() for line in f]
        f.close()

    def GetMatchingWords(self, state):
        # first, filter word list based on state.required, state.excluded
        words = [word for word in self.words if all(c in word for c in state.required)]
        words = [word for word in words if not any(c in word for c in state.excluded)]    
        # next, filter based on the regex from the state character mask    
        p = re.compile(state.GetRegex())
        self.words = [word for word in words if p.match(word)]
        return self.words

    def GetNextGuess(self, state):
        # we really want to SORT the list of potential words by how many of the 'primary' letters
        # they contain, and then do a random-weighted-selection from that list to return guess

        # for now, we just return a word at random
        return random.choice(self.words)

    def Seed(self):
        # return a 'seed word'
        seeds = ['chair', 'chain', 'soare', 'roate', 'raise']
        return random.choice(seeds)
