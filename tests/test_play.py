
import os
import sys
fpath = os.path.join(os.path.dirname(__file__), '..', 'wordle')
sys.path.append(fpath)

from player import BotPlayer
from game import Game

