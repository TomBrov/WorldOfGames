import random
import time
from Game import Game
from Dockerimage.Utils import Screen_cleaner


class MemoryGame(Game):
    def __init__(self, diff_game, name):
        super().__init__(diff_game, name)
        self.sequence = []

    def play(self):

        print("Welcome to Memory Game\n"
              f"Well {self.name},  I am thinking of a sequence with {self.diff} number/s")

        for i in range(0, self.diff):
            self.sequence.append(random.randint(1, 102))
        print(self.sequence, end='')
        time.sleep(0.7)
        Screen_cleaner()

        while self.guesses_taken < 6:
            if not self.get_guess():
                continue

            self.guesses_taken += 1

            print("Number entered")
            if self.guess < self.sequence[i]:
                print('Your guess is too low.')
            elif self.guess > self.sequence[i]:
                print('Your guess is too high.')
            else:
                print(f'Good job, {self.name}! You guessed my sequence!\n'
                      f'You made {self.value} points')
                self.add_score_db()
                exit(0)
        print(f'Nope. The sequence I was thinking of was {self.sequence}')