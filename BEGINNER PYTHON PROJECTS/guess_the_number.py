import random
import os

def guess():
    number = random.randint(0, 10)
    print("NB* the number is in range 0 and 10\n")

    while True:
        try:
            user_guess = int(input("What is your guess? "))

            if user_guess == number:
                os.system("cls")
                print(f"CORRECT!! THE NUMBER IS {number}")
                return 0
            elif user_guess > number:
                print("\nHINT: NUMBER IS LOWER THAN THE GUESS\n")
            elif user_guess < number:
                print("\nHINT: NUMBER IS HIGHER THAN THE GUESS\n")
        except ValueError:
            print("Guess should be an integer")
            

guess()