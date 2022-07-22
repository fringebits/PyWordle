
import os
import sys
fpath = os.path.join(os.path.dirname(__file__), '..', 'wordle')
sys.path.append(fpath)

from player import BotPlayer
from game import Game
from state import State

def test_bot():
     game = Game(BotPlayer(), 'trite')
     assert game.play() is True

def test_play():
    # words = [
    #     ['pants', 'yyxxx'],
    #     ['apple', 'ggxxx'],
    #     ['apart', 'ggxxx'],
    # ]
    # game = Game(BotPlayer(words), None)
    # assert game.play() is False # we did not win

    game = Game(BotPlayer(), 'aphid')
    game.play_word('pants')
    game.state.print()
    assert game.state.is_valid_word('apart', True) is False
    assert 'apart' not in game.solver.words


def test_light():
    game = Game(BotPlayer(), 'light')
    game.play_word('tight')
    game.state.print()
    print(game.solver.words)
    assert not game.state.is_valid_word('tight')
    assert not 'tight' in game.solver.words
    #assert False