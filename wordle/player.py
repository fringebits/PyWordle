
class IPlayer:
    def __init__(self):
        self.round = 0

class HumanPlayer(IPlayer):
    def __init__(self):
        self.Name = "Human"

class BotPlayer(IPlayer):
    def __init__(self):
        self.Name = "Human"