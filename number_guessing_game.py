"""Number Guessing Game

Player must guess a random number between 1 and 100.
"""

import random


def guess_game():
    target = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I chose a number between 1 and 100. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if guess < target:
            print("Too low! Try again.")
        elif guess > target:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break


if __name__ == "__main__":
    guess_game()
