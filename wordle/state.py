import re

def remove_letter(mask, letter):
    return mask.replace(letter, '')
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
        for ii in range(0,5):
            if not (score[ii] == 'g' or score[ii] == 'y'):
                self.mask[ii] = remove_letter(self.mask[ii], word[ii])
                if not word[ii] in self.required:
                    #print(f'Excluding letter {word[ii]}')
                    self.excluded.extend(word[ii])

        return score == 'ggggg'

    def is_valid_word(self, word, verbose = False):
        # first, filter word list based on state.required, state.excluded
        if not all(c in word for c in self.required):
            if verbose:
                print(f'{word} does not include required letters {self.required}')
            return False
        if any(c in word for c in self.excluded):
            if verbose:
                print(f'{word} contains excluded letters {self.excluded}')
            return False

        # next, filter based on the regex from the state character mask    
        p = re.compile(self.GetRegex())
        if not p.match(word):
            return False
        return True

    def print(self):
        print(f'REQUIRED={self.required}')
        print(f'EXCLUDED={self.excluded}')
        for m in self.mask:
            print(m)