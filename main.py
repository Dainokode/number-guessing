from database import logo
import random

print(logo)
print("Welcome to the Python Number Guessing Game!\n")

print("I am thinking of a number between 1 and 100\n")

attempts = 0

game_difficulty = input(
    "Choose a difficulty. Type 'easy' for 10 attempts or 'hard' for 5 attempts: ").lower()

if game_difficulty == "easy":
    attempts = 10
else:
    attempts = 5

print(f"You have {attempts} attempts to guess the number.")

numbers_list = []
for number in range(1, 101):
    numbers_list.append(number)

random_number = random.choice(numbers_list)

print(f"The random number is {random_number}")

game_on = True
while game_on:
    # ask user to guess a number
    chosen_number = int(input("Guess a number: "))

    if chosen_number != random_number:
        # take away an attempt
        attempts -= 1

        # print attempts left
        print(f"You have {attempts} attempts left")

        if attempts == 0:
            game_on = False
            print(f"You lost. The number was {random_number}")

    elif chosen_number == random_number:
        print("Well done!")
        game_on = False
