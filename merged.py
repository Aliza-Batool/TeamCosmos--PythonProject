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
def aliza():
    print("=== Calculator ===")

    # Taking first number input
    num1 = input("Enter first number: ")
    while True:
        try:
            num1 = float(num1)
            break
        except ValueError:  #applied input validation
            print("Invalid input! Please enter a valid number.")
            num1 = input("Enter first number: ")

    # Taking second number input
    num2 = input("Enter second number: ")
    while True:
        try:
            num2 = float(num2)
            break
        except ValueError:   #applied input validation
            print("Invalid input! Please enter a valid number.")
            num2 = input("Enter second number: ")

    # Taking operator input
    op = input("Enter operator (+, -, x, /): ")
    while op not in ['+', '-', 'x', '/']:   #operator validation
        print("Invalid operator! Try again.")
        op = input("Enter operator (+, -, *, /): ")

    # Calculations
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == 'x':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            result = "Error! Cannot divide by zero."
        else:
            result = num1 / num2

    print("Result:", result)


aliza()
