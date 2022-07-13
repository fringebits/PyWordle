
#from . import State
import numpy
import re
import os

class Solver:

    def __init__(self):
        filename = os.path.join(os.path.dirname(__file__), 'five-letter-words.txt')
        f = open(filename, 'r')
        self.words = [line.strip() for line in f]
        f.close()

    def GetMatchingWords(self, state):
        # first, filter word list based on state.required, state.excluded
        words = [word for word in self.words if all(c in word for c in state.required)]
        words = [word for word in words if not any(c in word for c in state.excluded)]        
        p = re.compile(state.GetRegex())
        words = [word for word in words if p.match(word)]
        return words

    def Seed(self):
        # return a 'seed word'
        return 'chair'
