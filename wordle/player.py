
class IPlayer:
    def __init__(self, solution):
        self.round = 0
        self.solution = solution

    # given a word, produce a score.  the score is 5 chracters, one of [g,y,x] that
    # represent the accuracy of the word relative to the solution.  If solution is 
    # not provided, the user must score the word interactivly.
    def ScoreWord(self, word):
        if self.solution is None:
            score = input(f'\tSCORE {word} [y=yellow, g=green, x=none]: ')
        else:        
            # in order to test the 'auto-solver' mode, need to write this function.
            score = ['x', 'x', 'x', 'x', 'x']
            local = []
            for ch in self.solution:
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

            score = ''.join(map(str, score))
            return score




class HumanPlayer(IPlayer):
    def __init__(self):
        self.Name = "Human"

    def GetNextGuess(self, solver, state):
        word = input(f'\tINPUT GUESS? [enter for random choice] ')
        if (len(word) < 5):
            word = solver.GetNextGuess(state)
        self.Words.append(word)
class BotPlayer(IPlayer):
    def __init__(self, input):
        self.Name = "Bot"
        self.Input = input

    def GetNextGuess(self, solver, state):
        if len(self.Input) > 0:
            word = self.Input[0]
            self.Input.pop(0)
        else:
            word = solver.GetNextGuess(state)
        self.Words.append(word)
        return word

