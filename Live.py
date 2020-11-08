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

    if g.isdigit() and 0 < int(g) < 4:
            g = int(g)
            game = games[g]
            print(f"The chosen game is {game}")
    else:
        return "No game was chosen. Exiting!"

    d = input("Please choose game difficulty from 1 to 5: ")

    if d.isdigit() and 0 < int(d) < 6:
        return f"The chosen difficulty is {d}"
    else:
        return "No difficulty was chosen. Exiting!"


if __name__ == "__main__":

    name = input("Enter your name: ")
    print(welcome(name))
    print(load_game())