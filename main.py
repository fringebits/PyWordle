
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


# test case
# --seed raise --solution wedge --autoplay

# given a word, produce a score.  the score is 5 chracters, one of [g,y,x] that
# represent the accuracy of the word relative to the solution.  If solution is 
# not provided, the user must score the word interactivly.
def score_word(word, solution):
    if solution is None:
        score = input(f'\tSCORE {word} [y=yellow, g=green, x=none]: ')
    else:        
        # in order to test the 'auto-solver' mode, need to write this function.
        score = ['x', 'x', 'x', 'x', 'x']
        local = []
        for ch in solution:
            local.append(ch)

        print(local)

        for ii in range(0,5):
            if word[ii] == local[ii]:
                score[ii] = 'g'
                local[ii] = '.' # mark this as being 'used'
        for ii in range(0,5):
            if score[ii] != 'g':
                # find out if letter ii is in the solution at all
                tmp = ''.join(map(str,local))
                pos = tmp.find(word[ii])
                if pos != -1:
                    score[ii] = 'y'
                    local[ii] = '.'

        print(score)

        score = ''.join(map(str, score))
    return score

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