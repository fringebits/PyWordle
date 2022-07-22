

class IPlayer:
    def __init__(self):
        self.round = 0
        self.words = []

    def is_first_guess(self):
        return len(self.words) == 0
class HumanPlayer(IPlayer):
    def __init__(self):
        super(HumanPlayer, self).__init__()
        self.name = "Human"

    def GetNextGuess(self, solver, state):
        if not self.is_first_guess():
            print(f'{len(solver.words)}: {solver.words}')
        word = input(f'\tINPUT GUESS? [enter for random choice] ')
        if (len(word) < 5):
            word = solver.GetNextGuess(state)
        self.words.append(word)
        return word
class BotPlayer(IPlayer):
    def __init__(self, input = []):
        super(BotPlayer, self).__init__()
        self.Name = "Bot"
        self.Input = input

    def GetNextGuess(self, solver, state):
        if len(self.Input) > 0:
            word = self.Input[0]
            self.Input.pop(0)
        elif len(self.words) == 0:
            word = solver.Seed()
        else:
            word = solver.GetNextGuess(state)
        self.words.append(word)
        return word

