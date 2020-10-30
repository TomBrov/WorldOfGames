def welcome(name):
    return (f"Hello {name} and welcome to the World of Games (Wog).\n"
            f"Here you can find many cool games to play")


def load_game():
    games = {1: "Memory Game", 2: "Guess Game", 3: "Currency Roulette"}

    print("Please choose a game to play:\n"
          "1. Memory Game - a sequence of numbers ill appear for 1 second and you have to guess it back.\n"
          "2. Guess Game - guess a number and see if you chose like the computer.\n"
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS.")

    g = input("Choose your game: ")

    if g.isdigit():
            g = int(g)
            game = games[g]
            print(f"The chosen game is {game}")

    diff = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5}

    d = input("Please choose game difficulty from 1 to 5: ")

    if d.isdigit():
        chosen = diff[d]
        return f"The chosen difficulty is {chosen}"


if __name__ == "__main__":

    name = input("Enter your name: ")
    print(welcome(name))
    print(load_game())