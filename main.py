from art import logo
import random

RANDOM_NUMBER = random.randint(0, 100)
life = 0


def guess_result(value):
    while value > 0:
        print(f"You have {value} attempts remaining to guess the number.")
        guessed_num = int(input("Make a guess: "))
        if guessed_num == RANDOM_NUMBER:
            print(f"You got it! The answer was {RANDOM_NUMBER}.")
            break
        elif guessed_num > RANDOM_NUMBER:
            print("Too high.")
            value -= 1
            if value == 0:
                print("You've run out of guesses, you lose.")
        elif guessed_num < RANDOM_NUMBER:
            print("Too low.")
            value -= 1
            if value == 0:
                print("You've run out of guesses, you lose.")


print(logo)
print("Welcome to the Number Guessing Game!")
game_difficulties = input("Choose a difficulty. Type 'easy' or 'medium' or 'hard': ").lower()
if game_difficulties == 'easy':
    life = 10
    guess_result(life)
elif game_difficulties == 'medium':
    life = 7
    guess_result(life)
elif game_difficulties == 'hard':
    life = 5
    guess_result(life)
else:
    print("Wrong input, goodbye!")
