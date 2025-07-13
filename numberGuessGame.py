import random
# number guessing game

# this is a test comment

# Create a function to introduce the game
# and explain the rules to the player
def intro():
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the secret number between 1 and 100.")
    print("You have 6 attempts to guess the number correctly.")
    print("Let's see if you can guess in 6 guesses or less!")

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Call the intro function to start the game
intro()

# Initialize guess count
max_guess = 6
guess_count = 0
print("\nA random number has been chosen. Start guessing!\n")

# Loop until the player guesses the number
while guess_count < max_guess:
    try:
        guess = int(input("Enter your guess (1-100): "))
    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 100.")
        continue
    
    # Check if the guess is within the valid range
    if guess < 1 or guess > 100:
        print("Your guess is out of range. Please guess a number between 1 and 100.")
        continue
    # Increment the guess count
    guess_count += 1

    # show the number of attempts left
    attempts_left = max_guess - guess_count
    print(f"You have {attempts_left} attempts left.")

    # Provide feedback based on the guess
    if guess == random_number:
        print(f"Congratulations! You've guessed the number {random_number} in {guess_count} attempts.")
        break
    else:
        difference = abs(guess - random_number)

        if difference <= 5:
            print("You're close! Keep trying.\n")
        
        if guess < random_number:
            print("Your guess is too low. Try again.\n")
        else:
            print("Your guess is too high. Try again.\n")
        print()
else:
    print(f"Sorry, you've used all {max_guess} attempts. The secret number was {random_number}. Better luck next time!")