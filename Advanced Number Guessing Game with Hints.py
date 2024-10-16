 
#Description: Enhance the basic number guessing game by providing hints based on how close the guess is to the actual number (e.g., "You're getting warmer" or "Too cold"). Use advanced conditional statements to handle the hint logic.
#Concepts Covered:
#Advanced use of if, else, and elif.
#Functions for encapsulating game logic.
#Git branching to add new features (e.g., hints).
#Stretch Goal: Add a scoring system based on the number of attempts

import random

def guess_number(target_number):
    attempts = 0
    last_difference = None  # To store the difference from the previous guess

    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 10): "))
            attempts += 1
            if guess == target_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                return attempts
            else:
                difference = abs(target_number - guess)

                if last_difference is None:
                    # This is the first guess, so no hint for comparison
                    if guess < target_number:
                        print("Too low. Try again.")
                    else:
                        print("Too high. Try again.")
                else:
                    # Provide hints on whether the guess is warmer or colder
                    if difference < last_difference:
                        print("You're getting warmer!")
                    else:
                        print("You're getting colder!")

                last_difference = difference  # Update the last difference for the next round

        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    target_number = random.randint(1, 10)
    print("Welcome to the Number Guessing Game!")
    print("I've selected a number between 1 and 10. Try to guess it!")

    attempts = guess_number(target_number)
    # Scoring system: fewer attempts lead to a higher score
    score = max(10 - attempts, 0)  # Ensure the score doesn't go negative
    print(f"Your score is: {score}")

if __name__ == "__main__":
    main()
