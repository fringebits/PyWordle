
class State:
    All = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self):
        self.mask = [State.All, State.All, State.All, State.All, State.All]
        self.required = [] # letters REQUIRED for the word
        self.excluded = [] # letters EXCLUDED for the word

    def GetRegex(self):
        # make regex for the mask
        result = ''
        for ch in self.mask:
            result = result + f'[{ch}]'
        return result

    def UpdateState(self, word, score):
        for ii in range(0,5):
            if score[ii] == 'g':
                #print(f'Adding required letter {word[ii]}, removing it from letter mask[{ii}]')
                self.required.extend(word[ii])
                self.mask[ii] = word[ii]
            elif score[ii] == 'y':
                #print(f'Adding required letter {word[ii]}, removing it from letter mask[{ii}]')
                self.required.extend(word[ii])
                self.mask[ii] = self.mask[ii].replace(word[ii], '')
            else:
                #print(f'Excluding letter {word[ii]}')
                self.excluded.extend(word[ii])

        #state.Print()


    def Print(self):
        print(self.required)
        print(self.excluded)
        for m in self.mask:
            print(m)