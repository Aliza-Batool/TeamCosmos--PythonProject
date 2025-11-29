import random

def Abeeha():
    num = random.randint(1, 50)
    print("==== THE NUMBER GUESSING GAME ====")
    print("A number has been generated randomly.")
    print("You have 10 tries to guess the number.")
    print("The number is between 1-50.")

    guess = 0
    i = 0

    while guess != num and i < 10:
        i += 1
        print("----------------------")
        print("Try number", i)
        print("----------------------")
        guess = int(input("Enter your guess: "))
        if i == 10:  
            break
        if guess > num:
            print("Your guess is too high. Guess lower.")
        elif guess < num:
            print("Your guess is too low. Guess higher.")

    if guess == num:
        print("You guessed the correct number!")
    else:
        print("Oops! You are out of tries!")
        print("The correct number was:", num)


Abeeha()
