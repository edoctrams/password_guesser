# Import necessary modules
import os      # Used to clear the screen
import time    # Used to pause the program for a short time
import random  # Used to pick random characters

# Ask the user to enter a password
password = input("Enter a password (only lowercase letters or numbers): ")

# List of possible characters the program can use to guess
characters = list("abcdefghijklmnopqrstuvwxyz1234567890")

# Create an empty list to store the guessed characters
guessed_password = [""] * len(password)

# Keep trying until the guessed password matches the original password
while "".join(guessed_password) != password:
    for i in range(len(password)):
        # If a character is incorrect, replace it with a new random one
        if guessed_password[i] != password[i]:
            guessed_password[i] = random.choice(characters)

    # Join the list into a string and print the current guess
    print("Trying:", "".join(guessed_password))

    # Wait for a short time (0.1 seconds)
    time.sleep(0.1)

    # Clear the screen (works on both Windows and Mac/Linux)
    os.system("cls" if os.name == "nt" else "clear")

# When the loop is done, print the final password
print("The password is:", "".join(guessed_password))
