import re
import random
import os
import sys
fpath = os.path.dirname(__file__)
sys.path.append(fpath)

from filter import Filter

class IPlayer:
    letters = ['e', 'a', 'r', 'o', 't', 'l', 'i', 's', 'n', 'c']
    ranks = {
        'a':43.3,
        'b':10.56,
        'c':23.13,
        'd':17.25,
        'e':56.88,
        'f':9.24,
        'g':12.59,
        'h':15.31,
        'i':38.45,
        'j':1.0,
        'k':5.61,
        'l':27.98,
        'm':15.36,
        'n':33.92,
        'o':36.51,
        'p':16.14,
        'q':1.0,
        'r':38.64,
        's':29.23,
        't':35.43,
        'u':18.51,
        'v':5.13,
        'w':6.57,
        'x':1.48,
        'y':9.06,
        'z':1.39,
        '.':0.0
    }

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

    def first_guess(self):
        # return a 'seed word'
        seeds = ['crane', 'chair', 'chain', 'soare', 'roate', 'raise']
        #seeds = ['crane']
        return random.choice(seeds)

    def next_guess(self):
        if self.is_first_guess():
            word = self.first_guess()
        else:
            ranks = self.rank_words()
            word = list(ranks.keys())[-1]
        return word

    def rank_word(self, word):
        rank = 0.0
        for ii in range(0,5):
            if len(self.filter.mask[ii]) > 1:
                rank += IPlayer.ranks[word[ii]]
            if (ii > 0) and (word[ii] in word[0:ii]):
                # duplicate letter, no value add for this information
                rank -= (IPlayer.ranks[word[ii]] * 0.9)
        return rank

    def rank_words(self):
        table = dict()
        for word in self.words:
            rank = self.rank_word(word)
            table[word] = rank

        result = {k: v for k, v in sorted(table.items(), key=lambda item: item[1])}
        return result


class HumanPlayer(IPlayer):
    def __init__(self):
        super(HumanPlayer, self).__init__()

    def next_guess(self):
        # if not self.is_first_guess():
        #     print(f'{len(self.words)}: {self.words}')
        result = self.rank_words()
        for k in list(result.keys())[-10:]:
             print(f'{k} {result[k]}')

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
        elif self.is_first_guess():
            word = self.first_guess()
        else:
            ranks = self.rank_words()
            word = list(ranks.keys())[-1]
        return word
