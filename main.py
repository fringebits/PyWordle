
from wordle.solver import Solver
from wordle.state import State

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

def score_word(word, solution):
    if solution is None:
        score = input(f'Score {word} [y=yellow, g=green, x=none]:')
    else:
        assert(False, 'not implemented yet')
    return score

def main():
    logging.debug("PiFrame main")

    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="Debug mode, forces use of windows", action="store_true")
    parser.add_argument("--seed", help="Starting word")
    parser.add_argument("--solution", help="Solution word")
    args = parser.parse_args()

    solver = Solver()
    state = State()
    state.Print()

    # score word
    word = args.seed if args.seed is not None else solver.Seed()
    list = [0, 0] # just need a list longer than 1

    while len(list) > 1:

        print(f'GUESS {word}')
        score = score_word(word, args.solution)

        for ii in range(0,5):
            if score[ii] == 'g':
                print(f'Adding required letter {word[ii]}, removing it from letter mask[{ii}]')
                state.required.extend(word[ii])
                state.mask[ii] = word[ii]
            elif score[ii] == 'y':
                print(f'Adding required letter {word[ii]}, removing it from letter mask[{ii}]')
                state.required.extend(word[ii])
                state.mask[ii] = state.mask[ii].replace(word[ii], '')
            else:
                print(f'Excluding letter {word[ii]}')
                state.excluded.extend(word[ii])

        state.Print()

        list = solver.GetMatchingWords(state)
        print(list)
        word = list[0]    

if __name__ == "__main__":
    main()