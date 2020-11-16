import requests
import random
from Game import Game


class RouletteGame(Game):
    def __init__(self, diff_game, name):
        super().__init__(diff_game, name)
        self.guesses_taken = 0
        self.amount = random.randint(1, 101)
        self.currency = None
        self.guess = None
        self.convert = None

    def get_guess(self):
        self.guess = input('Guess the amount of USD: ')
        if not self.guess.isdigit():
            print('Not a valid guess.')
            return False
        self.guess = int(self.guess)
        return True

    def play(self):

        key = '2639ccac02d7c15359d45f9a2bc9d8ea'
        params = {'access_key': key, 'currencies': 'USD,ILS', 'format': 1}
        req = requests.get('http://apilayer.net/api/live', params=params)
        currency = req.json()['quotes']['USDILS']

        currency = int(currency) * self.amount
        self.currency = (currency - (5 - self.diff), currency + (5 - self.diff))

        print("Welcome to Currency Roulette\n"
              f"Well {self.name},  The amount in ILS is between {self.currency}")

        while self.guesses_taken < 6:
            if not self.get_guess():
                continue
            self.guesses_taken += 1

            if self.guess < self.amount:
                print('Your guess is too low.')
            elif self.guess > self.amount:
                print('Your guess is too high.')
            else:
                print(f'Good job, {self.name}! You guessed my number in {self.guesses_taken} guesses!')
                return

        print(f'Nope. The amount I was thinking of was {self.amount}')