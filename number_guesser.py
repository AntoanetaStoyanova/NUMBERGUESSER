import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit(): # isdigit check if its number
    top_of_range = int(top_of_range)  #convert a string to number 

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()
        
randome_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)  

    else:
        print("Please type a number next time.")
        continue  #will bring us of the top of the loop rather than breaking or quitting the loop

    if user_guess == randome_number:
        print("You got it!")
        break
    elif user_guess > randome_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")