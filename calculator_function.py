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
