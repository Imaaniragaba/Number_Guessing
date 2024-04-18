# first import the random module into python
import random

# we ask the user for the maximum number in our range of numbers
top_of_range = input("Type a number: ")

# we check whether the entered number is a digit
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    # if entered number is a digit, we check whether it's above zero
    if top_of_range <= 0:
        print("Please type a number that is greater than 0 next time!")
        quit()
else:
        print("Please type a number next time")
        quit()

# we use the random module to generate a random integer between zero and our maximum number
random_number = random.randint(0, top_of_range)
guesses = 0

# we start a while loop that execcutes until it is broken
while True:
    # below is a guess counter that increments by one everytime the program runs
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
        
    else:
        print("Please type in a number next time!")
        continue

    if user_guess == random_number:
         print("You got it!")
         break
    elif user_guess > random_number:
              print("You were above the number!")

    else:
              print("You were below the number!")
         

print("You got it in", guesses, "guesses")