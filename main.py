
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
    guesses = [word]

    while (len(guesses) < 6) and not winner:
        
        # Get the next guess
        word = player.GetNextGuess(solver, state)

        score = player.ScoreWord(word)

        winner = solver.UpdateState(word, score)





    while not done:


        print(f'Round {len(guesses)}')
        print(f'\tGUESS {word}')
        score = score_word(word, args.solution)
        print(f'\tSCORE {score}')

        state.UpdateState(word, score)

        list = solver.GetMatchingWords(state)

        if len(list) > 1:
            print(list)
            if args.solution is not None and args.autoplay:
                word = solver.GetNextGuess(state)
            else:
                word = input(f'\tNEXT GUESS? [enter for random choice] ')
                if (len(word) < 5):
                    word = solver.GetNextGuess(state)
            guesses.append(word)
        elif len(list) == 1:
            guesses.append(list[0])
            done = True
        else:
            assert False, "List of candidate words is empty!!"

    print()
    print()
    for g in guesses:
        print(f'{g}')

if __name__ == "__main__":
    main()