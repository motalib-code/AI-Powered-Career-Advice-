
number_guessing_game.py
# ========================================
# NUMBER GUESSING GAME
# ========================================

import random

def play_game():
    """Main game function"""
    print("=" * 50)
    print("Welcome to the NUMBER GUESSING GAME!")
    print("=" * 50)
    print("\nI'm thinking of a number between 1 and 100.")
    print("Can you guess it?\n")

    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            # Get user input
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess < 1 or guess > 100:
                print("⚠️  Please enter a number between 1 and 100!\n")
                continue

            if guess < secret_number:
                print("📈 Too low! Try a higher number.\n")
            elif guess > secret_number:
                print("📉 Too high! Try a lower number.\n")
            else:
                print("\n" + "=" * 50)
                print(f"🎉 CONGRATULATIONS! You guessed it!")
                print(f"The number was {secret_number}")
                print(f"You won in {attempts} attempts!")
                print("=" * 50)
                return True

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")

    # Game over
    print("\n" + "=" * 50)
    print(f"💔 GAME OVER! You've used all {max_attempts} attempts.")
    print(f"The correct number was {secret_number}")
    print("=" * 50)
    return False

def main():
    """Main program loop"""
    while True:
        play_game()

        # Ask to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Goodbye! 👋")
            break
        print("\n")

# Run the game
if __name__ == "__main__":
    main()
