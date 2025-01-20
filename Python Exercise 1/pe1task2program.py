import random

# Generate a random number between 1 and 9
secret_number = random.randint(1, 9)

while True:
    # Prompt the user to enter a guess
    try:
        guess = int(input("Guess a number between 1 and 9: "))
        
        # Check if the guess is correct
        if guess == secret_number:
            print("Well guessed!")
            break  # Exit the loop if the guess is correct
        else:
            print("Wrong guess, try again!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue  # Skip the rest of the loop and start from the beginning

