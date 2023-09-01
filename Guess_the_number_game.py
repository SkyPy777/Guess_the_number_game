
import random

while True:
    print("\nWelcome to the number guessing game!")
    print("Guess the number between 1 and 100.")

    hidden_number = random.randint(1, 100)

    attempts = 0

    while True:
        guess = int(input("\nEnter the number: "))
        attempts += 1

        if guess > hidden_number:
            print("Too high, try again.")
        elif guess < hidden_number:
            print("Too low, try again.")
        else:
            print(f"\nCongrats! You have guessed the number {hidden_number} in {attempts} attempts!")
            break

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        print("Thanks for playing again.")
    else:
        print("\nThanks for playing! Goodbye.")
        break




