
from wordle.solver import Solver
from wordle.state import State

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

# given a word, produce a score.  the score is 5 chracters, one of [g,y,x] that
# represent the accuracy of the word relative to the solution.  If solution is 
# not provided, the user must score the word interactivly.
def score_word(word, solution):
    if solution is None:
        score = input(f'\tSCORE {word} [y=yellow, g=green, x=none]: ')
    else:
        # in order to test the 'auto-solver' mode, need to write this function.
        assert False, 'not implemented yet'
    return score

def main():
    logging.debug("PiFrame main")

    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="Debug mode, forces use of windows", action="store_true")
    parser.add_argument("--seed", help="Starting word")
    parser.add_argument("--solution", help="Solution word") # to be used to "test" the solver
    args = parser.parse_args()

    solver = Solver()
    state = State()
    
    # get the starting word
    if args.seed is not None:
        word = args.seed
    else:
        word = input(f'FIRST GUESS? [enter for random seed] ')
        if (len(word) < 5):
            word = solver.Seed()

    done = False
    guesses = [word]

    while not done:

        print(f'Round {len(guesses)}')
        print(f'\tGUESS {word}')
        score = score_word(word, args.solution)

        state.UpdateState(word, score)

        list = solver.GetMatchingWords(state)

        if len(list) > 1:
            print(list)
            word = input(f'\tNEXT GUESS? [enter for random choice] ')
            if (len(word) < 5):
                word = random.choice(list)
            guesses.append(word)
        elif len(list) == 1:
            guesses.append(list[0])
            done = True

    print()
    print()
    for g in guesses:
        print(f'{g}')

if __name__ == "__main__":
    main()