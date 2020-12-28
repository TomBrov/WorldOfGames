from os import path
from Utils import *


class Game:
    def __init__(self, diff_game, name):
        self.diff = diff_game
        self.name = name
        self.guesses_taken = 0
        self.guess = None
        self.value = (self.diff * 3) + 5

    def get_guess(self):
        self.guess = input('Take a guess: ')
        if not self.guess.isdigit():
            print('Not a valid guess.')
            return False
        self.guess = int(self.guess)
        return True

    def add_score(self):
        p = f'./{SCORES_FILE_NAME}'
        if path.exists(p):
            with open(f"{SCORES_FILE_NAME}", 'r') as p:
                f = p.read()
                if f.isdigit():
                    f = int(f)
                    sum = str(f + self.value)
                    with open(f"{SCORES_FILE_NAME}", "w") as p:
                        p.write(f'{sum}')
                else:

        else:
            with open(f"{SCORES_FILE_NAME}", 'w') as p:
                p.write(f'{str(self.value)}')
