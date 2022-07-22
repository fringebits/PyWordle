import os
import sys
fpath = os.path.dirname(__file__)
sys.path.append(fpath)

from solver import Solver
from state import State
#from .player import IPlayer

def string_to_array(word):
    local = []
    for ch in word:
        local.append(ch)
    return local

def array_to_string(word):
    result = ''.join(map(str, word))
    return result

class Game:
    def __init__(self, player, solution):
        self.player = player
        self.solution = solution
        self.solver = Solver()
        self.state = State()
        self.guesses = []

    def play_word(self, word):
        self.guesses.append(word)

        score = self.ScoreWord(word)

        winner = self.state.UpdateState(word, score)

        self.solver.GetMatchingWords(self.state)

        print(f'{word} -> {score} ({len(self.solver.words)})')

        #state.print()

        return winner

    def play(self):
        winner = False

        while (len(self.guesses) < 6) and not winner and len(self.solver.words) > 0:
            
            # Get the next guess
            word = self.player.GetNextGuess(self.solver, self.state)

            winner = self.play_word(word)

        return winner


        # given a word, produce a score.  the score is 5 chracters, one of [g,y,x] that
    # represent the accuracy of the word relative to the solution.  If solution is 
    # not provided, the user must score the word interactivly.
    def ScoreWord(self, word):
        if self.solution is None:
            score = input(f'\tSCORE {word} [y=yellow, g=green, x=none]: ')
            return score
        else:        
            # in order to test the 'auto-solver' mode, need to write this function.
            score = ['x', 'x', 'x', 'x', 'x']
            local = string_to_array(self.solution)
            word = string_to_array(word)

            # print(local)
            # print(score)
            # print(word)

            for ii in range(0,5):
                if word[ii] == local[ii]:
                    score[ii] = 'g'
                    local[ii] = '.' # mark this as being 'used'

            for ii in range(0,5):
                #print(f'Testing {word[ii]} in {local}')
                if score[ii] != 'g':
                    # find out if letter ii is in the solution at all
                    tmp = ''.join(map(str,local))
                    pos = tmp.find(word[ii])
                    if pos != -1:
                        score[ii] = 'y'
                        local[pos] = '.'
                #print(score)

            result = ''.join(map(str, score))
            return result

