import re
import random
import os
import sys
fpath = os.path.dirname(__file__)
sys.path.append(fpath)

from filter import Filter

class IPlayer:
    letters = ['e', 'a', 'r', 'o', 't', 'l', 'i', 's', 'n', 'c']

    def __init__(self):
        self.round = 0
        self.guesses = [] # my guesses
        self.filter = Filter()
        filename = os.path.join(os.path.dirname(__file__), 'five-letter-words.txt')
        f = open(filename, 'r')
        self.words = [line.strip() for line in f]
        f.close()

    def play_word(self, word, score):
        self.guesses.append(word)
        winner = self.filter.update_filter(word, score)
        self.update_words()
        return winner

    def num_words(self):
        return len(self.words)

    def is_first_guess(self):
        return self.num_guesses() == 0

    def num_guesses(self):
        return len(self.guesses)

    def update_words(self):
        self.words = [word for word in self.words if self.filter.is_valid_word(word)]
        return self.words

    def next_guess(self):
        # we really want to SORT throae list of potential words by how many of the 'primary' letters
        # they contain, and then do a random-weighted-selection from that list to return guess

        if self.is_first_guess():
            return self.first_guess()

        # for now, we just return a word at random
        return random.choice(self.words)

    def first_guess(self):
        # return a 'seed word'
        seeds = ['crane', 'chair', 'chain', 'soare', 'roate', 'raise']
        #seeds = ['crane']
        return random.choice(seeds)


class HumanPlayer(IPlayer):
    def __init__(self):
        super(HumanPlayer, self).__init__()

    def next_guess(self):
        if not self.is_first_guess():
            print(f'{len(self.words)}: {self.words}')
        word = input(f'\tINPUT GUESS? [enter for random choice] ')
        if (len(word) < 5):
            word = super(HumanPlayer, self).next_guess()
        return word

class BotPlayer(IPlayer):
    def __init__(self, input = []):
        super(BotPlayer, self).__init__()
        self.input = input

    def next_guess(self):
        if len(self.input) > 0:
            word = self.input[0]
            self.input.pop(0)
        else:
            word = super(BotPlayer, self).next_guess()
        return word

