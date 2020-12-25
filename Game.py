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

        p = './score.txt'

        if path.exists(p):
            p = open("score.txt", 'r')
            f = p.read()
            if f.isdigit():
                f = int(f)
                sum = f + self.value
                p = open("score.txt", "w")
                p.write(f'{sum}')
                p.close()
            else:
                pass
        else:
            p = open("score.txt", 'w')
            p.write(f'{self.value}')
            p.close()
