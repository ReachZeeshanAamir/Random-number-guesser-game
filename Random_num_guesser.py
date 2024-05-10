import random

top_of_range = input("Enter a number: ")

if top_of_range.isdigit:
        top_of_range = int(top_of_range)
        if top_of_range <- 0:
            print("please enter a number grater than 0.")
            quit()

else: 
    print("Please enter a number.")
    quit()

randomnumber = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses +=1
    user_guess = input("Make a Guess: ")
    if user_guess.isdigit:
        user_guess = int(user_guess)
        
    else: 
        print("Please enter a number.")
        quit()
        continue
    if user_guess == randomnumber:
        print("You got it")
        break
    
    elif user_guess > randomnumber:
        print("You were above number")
    else:
        print("You were below number")

print("You got it on", guesses, "guesses")