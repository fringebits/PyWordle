
import os
import sys
fpath = os.path.join(os.path.dirname(__file__), '..', 'wordle')
sys.path.append(fpath)

from player import BotPlayer
from game import Game

class ValidateScore:
    def __init__(self, solution, pairs):
        self.game = Game(BotPlayer(), solution)
        self.pairs = pairs

        assert self.game.ScoreWord(solution) == 'ggggg'
        for pair in self.pairs:
            score = self.game.ScoreWord(pair[0])
            assert  score == pair[1], f'{pair[0]} score={score}, expected {pair[1]}'

def test_score():
    ValidateScore('trite', [
        ['chair', 'xxxyy'],
        ['piers', 'xyyyx'],
        ['write', 'xgggg']
    ])

    ValidateScore('angry', [
        ['pants', 'xyyxx'],
        ['brawn', 'xyyxy'],
        ['loran', 'xxyyy'],
        ['anger', 'gggxy']
    ])