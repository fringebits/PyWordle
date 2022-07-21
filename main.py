
from wordle.solver import Solver
from wordle.state import State
from wordle.player import HumanPlayer, BotPlayer

import argparse
import random
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
    parser.add_argument("--seed", help="Starting word")
    parser.add_argument("--solution", help="Solution word") # to be used to "test" the solver
    parser.add_argument("--autoplay", help="Autoplay, assuming solution was provided", action="store_true")
    args = parser.parse_args()

    solver = Solver()
    state = State()

    player = HumanPlayer(args.solution)

    winner = False
    guesses = []

    while (len(guesses) < 6) and not winner:
        
        # Get the next guess
        word = player.GetNextGuess(solver, state)    

        score = player.ScoreWord(word)

        print(score)

        winner = state.UpdateState(word, score)

if __name__ == "__main__":
    main()