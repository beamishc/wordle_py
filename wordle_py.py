from icecream import ic
from functions.input_lower import input_lower
from functions.check_chars import check_chars
import random

game_title = "WordlePy"

# Load words
with open("words.txt", "r") as f:
    words = f.read().splitlines()

# Choose a random word
target_word = random.choice(words).lower()
ic(target_word)

# Variables
correct = ['_', '_', '_', '_', '_']
misplaced = []
incorrect = []
max_attempts = 6
current_attempts = 0
errors = 0

# Print game title
print(f'''Welcome to {game_title}! You have get 6 attempts to guess today's random 5 letter word. Best of luck!''')
print(f"You have {max_attempts} attempts remaining.")

guess = input("Time for your first guess. Choose wisely! _ _ _ _ _    ").lower()

if guess == target_word:
    print(f"Are you some kind of psychic? Because you guessed the word on your first try! The word was {target_word}.")

else:
    # Game loop
    while current_attempts < max_attempts and errors < 3:

        if guess == target_word:
            print(f"Congratulations! You guessed the word after {current_attempts} attempts! The word was {target_word}.")
            break

        elif guess.isalpha():
            if len(guess) == 5:
                current_attempts += 1
                correct, misplaced, incorrect = check_chars(guess, target_word, correct, misplaced, incorrect)

                print('\n',''.join(correct).upper())
                print('\nMisplaced letters: ', ' '.join(misplaced).upper())
                print('\nIncorrect letters: ', ' '.join(incorrect).upper())

                guess = input_lower("incorrect", current_attempts, max_attempts)

            else:
                guess = input_lower("is_five", current_attempts, max_attempts)
                errors += 1
        else:
            guess = input_lower("is_alpha", current_attempts, max_attempts)
            errors += 1
