

def string_to_array(word):
    local = []
    for ch in word:
        local.append(ch)
    return local

def array_to_string(word):
    result = ''.join(map(str, word))
    return result

class IPlayer:
    def __init__(self, solution):
        self.round = 0
        self.solution = solution
        self.words = []

    # given a word, produce a score.  the score is 5 chracters, one of [g,y,x] that
    # represent the accuracy of the word relative to the solution.  If solution is 
    # not provided, the user must score the word interactivly.
    def ScoreWord(self, word):
        if self.solution is None:
            score = input(f'\tSCORE {word} [y=yellow, g=green, x=none]: ')
        else:        
            # in order to test the 'auto-solver' mode, need to write this function.
            score = ['x', 'x', 'x', 'x', 'x']
            local = string_to_array(self.solution)
            word = string_to_array(word)

            # print(local)
            # print(score)
            # print(word)

            for ii in range(0,5):
                if word[ii] == local[ii]:
                    score[ii] = 'g'
                    local[ii] = '.' # mark this as being 'used'

            for ii in range(0,5):
                print(f'Testing {word[ii]} in {local}')
                if score[ii] != 'g':
                    # find out if letter ii is in the solution at all
                    tmp = ''.join(map(str,local))
                    pos = tmp.find(word[ii])
                    if pos != -1:
                        score[ii] = 'y'
                        local[pos] = '.'
                print(score)

            result = ''.join(map(str, score))
            return result




class HumanPlayer(IPlayer):
    def __init__(self, solution):
        super(HumanPlayer, self).__init__(solution)
        self.Name = "Human"

    def GetNextGuess(self, solver, state):
        word = input(f'\tINPUT GUESS? [enter for random choice] ')
        if (len(word) < 5):
            word = solver.GetNextGuess(state)
        self.words.append(word)
        return word
class BotPlayer(IPlayer):
    def __init__(self, solution, input = []):
        super(BotPlayer, self).__init__(solution)
        self.Name = "Bot"
        self.Input = input

    def GetNextGuess(self, solver, state):
        if len(self.Input) > 0:
            word = self.Input[0]
            self.Input.pop(0)
        else:
            word = solver.GetNextGuess(state)
        self.words.append(word)
        return word

