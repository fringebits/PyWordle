
import os
import sys
fpath = os.path.join(os.path.dirname(__file__), '..', 'wordle')
sys.path.append(fpath)

from player import BotPlayer

def test_score():
    player = BotPlayer('trite')
    assert player.ScoreWord('chair') == 'xxxyy'
    assert player.ScoreWord('piers') == 'xyyyx'