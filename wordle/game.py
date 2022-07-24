import os
import sys
fpath = os.path.dirname(__file__)
sys.path.append(fpath)

#from state import State
#from player import IPlayer

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
        self.validate_solution();
 
    def num_guesses(self):
        return self.player.num_guesses()

    def is_valid_word(self, word, verbose=False):
        return self.player.filter.is_valid_word(word, verbose)

    def validate_solution(self):
        if not self.solution is None:
            assert self.is_valid_word(self.solution), f'Solution is no longer valid.'
            assert self.solution in self.player.words, f'Solution is not in possible words' 

    def play_word(self, word):

        score = self.ScoreWord(word)

        winner = self.player.play_word(word, score)

        print(f'{word} -> {score} ({self.player.num_words()})')

        self.validate_solution()

        return winner

    def play(self):
        winner = False

        while self.num_guesses() < 6 and not winner and self.player.num_words() > 0:
            
            # Get the next guess
            word = self.player.next_guess()

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

