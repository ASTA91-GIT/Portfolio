import random

def number_guessing_game():
    """
    A simple number guessing game where the user tries to guess a random number.
    """
    print("🎮 Welcome to Number Guessing Game! 🎮")
    print("=" * 40)
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it!")
    print("-" * 40)
    
    while attempts < max_attempts:
        try:
            # Get user's guess
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
            attempts += 1
            
            # Check if guess is valid
            if guess < 1 or guess > 100:
                print("❌ Please enter a number between 1 and 100!")
                continue
            
            # Check the guess
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                print(f"The number was {secret_number}")
                return True
            elif guess < secret_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")
            
            # Show remaining attempts
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Attempts remaining: {remaining}")
            print("-" * 30)
            
        except ValueError:
            print("❌ Please enter a valid number!")
            continue
    
    # If we get here, the user ran out of attempts
    print(f"😔 Game Over! You ran out of attempts.")
    print(f"The number was {secret_number}")
    return False

def play_again():
    """Ask if the user wants to play again."""
    while True:
        choice = input("\nWould you like to play again? (yes/no): ").lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def main():
    """Main game loop."""
    print("🎯 NUMBER GUESSING GAME 🎯")
    print("=" * 50)
    
    while True:
        # Play the game
        number_guessing_game()
        
        # Ask if they want to play again
        if not play_again():
            print("\n👋 Thanks for playing! Goodbye!")
            break
        
        print("\n" + "=" * 50)

if __name__ == "__main__":
    main()
