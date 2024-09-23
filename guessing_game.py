import random

chosen_number = random.choice(list(range(1, 11)))
guessed_numbers = []
attempts = 0
max_attempts = 5

# Read input from the file instead of interactive input
with open('guesses.txt', 'r') as file:
    guesses = file.read().splitlines()

for guess_number in guesses:
    if attempts >= max_attempts:
        break

    guess_number = int(guess_number)
    
    if guess_number in guessed_numbers:
        print(f'{guess_number} is already guessed. Try another number')
        continue

    guessed_numbers.append(guess_number)

    attempts += 1

    if guess_number < chosen_number:
        print(f'{guess_number} is too low. Guess a higher number')
    elif guess_number > chosen_number:
        print(f'{guess_number} is too high. Guess a lower number')
    else:
        print('Your guess is correct. You win!!')
        break

if attempts == max_attempts:
    print(f'Game over. The number chosen was {chosen_number}.')
