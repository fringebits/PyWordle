
from wordle.player import HumanPlayer, BotPlayer
from wordle.game import Game

import argparse
import os
import logging
from logging.handlers import RotatingFileHandler

logFile = 'solver.log'
logLevel = logging.DEBUG
isDebug = True

handler = RotatingFileHandler(logFile, mode='a', backupCount=5)
if os.path.isfile(logFile):
    handler.doRollover()
logging.basicConfig(filename=logFile, level=logging.DEBUG)


# test case
# --seed raise --solution wedge --autoplay

def main():
    logging.debug("PiFrame main")

    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="Debug mode, forces use of windows", action="store_true")
    parser.add_argument("--solution", help="Solution word") # to be used to "test" the solver
    parser.add_argument("--bot", help="Auto-play the game (requires solution)", action="store_true")
    args = parser.parse_args()

    # game = Game(BotPlayer(), 'aphid')
    # game.play_word('pants')
    # game.state.print()
    # assert game.state.is_valid_word('apart', True)


    if args.bot:
        player = BotPlayer()
    else:
        player = HumanPlayer()

    game = Game(player, args.solution)

    game.play()

if __name__ == "__main__":
    main()