from database import logo
import random

play_again = True
while play_again:
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

    game_on = True
    while game_on:
        # ask user to guess a number
        chosen_number = int(input("Guess a number: "))

        if chosen_number != random_number:
            # take away an attempt
            attempts -= 1

            # tell user the number is too high or too low depending on random number
            if chosen_number > random_number:
                print("Too high, guess again.")
            else:
                print("Too low, guess again.")

            # print attempts left
            print(f"You have {attempts} attempts left")

            if attempts == 0:
                game_on = False
                print(f"You lost. The number was {random_number}")

        elif chosen_number == random_number:
            print("Well done!")
            game_on = False

        if game_on == False:
            play_again = input(
                "Do you want to play again? Type 'y' or 'n': ").lower()
            if play_again == "n":
                play_again = False
