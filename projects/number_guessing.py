import random

print("Welcome to the Number Guessing Game!")
number_to_guess = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Guess a number between 1 and 100 (or type 'exit' to quit): ")

    if guess.lower() == 'exit':
        print("Exiting the game. Thanks for playing!")
        break

    if not guess.isdigit():
        print("Invalid input. Please enter a number or type 'exit' to quit.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < 1 or guess > 100:
        print("Please guess a number between 1 and 100.")
        continue
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    elif guess == number_to_guess:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        break

   

print("thank you for playing the Number Guessing Game!")