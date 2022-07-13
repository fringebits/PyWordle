
class State:
    All = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self):
        self.mask = [State.All, State.All, State.All, State.All, State.All]
        self.required = []
        self.excluded = []

    def GetRegex(self):
        # make regex for the mask
        result = ''
        for ch in self.mask:
            result = result + f'[{ch}]'
        return result

    def Print(self):
        print(self.required)
        print(self.excluded)
        for m in self.mask:
            print(m)