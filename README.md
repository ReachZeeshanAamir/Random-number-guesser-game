# Number Guessing Game Documentation

## Overview
This is a simple number guessing game written in Python. The game generates a random number within a range specified by the user, and the user attempts to guess the number. The game provides feedback on whether the guess is too high, too low, or correct. It also tracks the number of guesses made by the user.

## How It Works
1. The user is prompted to enter a positive number, which sets the upper bound for the random number range.
2. If the input is not a valid digit, the game exits with an error message.
3. The game generates a random number between 0 and the user's specified upper bound.
4. The user is then prompted to guess the generated random number.
5. If the user's guess is not a valid digit, the game exits with an error message.
6. If the user's guess is correct, the game announces the correct guess and the number of attempts made.
7. If the guess is incorrect, the game provides feedback indicating whether the guess is too high or too low, and the loop continues.

## Key Components
- **Random Number Generation:** Generates a random number within the specified range.
- **User Input:** Collects input from the user for setting the upper bound and making guesses.
- **Validation:** Validates the user input to ensure it is a positive integer.
- **Game Loop:** Continues to prompt the user for guesses until the correct number is guessed.
- **Feedback:** Provides feedback on the user's guess and displays the total number of guesses when the correct number is guessed.

## Code Explanation
### Setting the Range
The game begins by prompting the user to enter a positive number to set the upper bound for the random number range. If the user input is not a digit or if it is less than or equal to 0, the game exits with a relevant message.

```python
import random

top_of_range = input("Enter a number: ")

if not top_of_range.isdigit():
    print("Please enter a number.")
    quit()

top_of_range = int(top_of_range)

if top_of_range <= 0:
    print("Please enter a number greater than 0.")
    quit()
```
### Generating a Random Number
Once the upper bound is validated, the game generates a random number between 0 and the specified upper bound.
```python
random_number = random.randint(0, top_of_range)
guesses = 0
```
### Game Loop and User Feedback
The game enters a loop where it prompts the user to guess the random number. It keeps track of the number of guesses made. If the user input is not a valid digit, the game exits. Otherwise, it provides feedback if the guess is too high or too low.
```python
while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if not user_guess.isdigit():
        print("Please enter a number.")
        quit()

    user_guess = int(user_guess)

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number.")
    else:
        print("You were below the number.")
```

### Final Output
If the user guesses the correct number, the game displays a success message along with the total number of guesses.

```python
print("You got it in", guesses, "guesses!")
```
# Known Limitations
- No support for guessing negative numbers.
- No handling for non-integer inputs beyond simple quit on invalid input.
- The game always starts at 0, which might not be intuitive for all users.
# Future Enhancements
- Implement advanced error handling for various invalid inputs.
- Add support for more flexible guess range options.
- Improve user feedback with more detailed instructions or guidance.
With this documentation, you should have a clear understanding of how the game works and how to use it
