from redis import Redis


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

    def add_score_db(self):
        name = 'user'
        score = self.value

        redis = Redis(password='wog123', decode_responses=True)

        current_value = redis.get(name)

        if current_value is not None:
            score += int(current_value)
        redis.set(name, score)
        redis.close()