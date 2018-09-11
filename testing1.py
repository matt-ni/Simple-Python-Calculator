import time

# Welcome message
print("Welcome to the calculator!")
time.sleep(5)


def ask():
    while True:
        prompt = input("Do you want to perform another calculation? ")
        if prompt == "Yes":
            calc()
        elif prompt == "No":
            print("Thanks for using this program! ")
            exit()
        else:
            print("Invalid answer. Try again. ")
            continue


def calc():
    while True:
        operation = input("""Please choose an operation:
    + Addition
    - Subtraction
    * Multiplication
    / Division
    % Modulo
    """)

        # Ask user for two numbers.
        num1 = float(input("Enter your first number here. "))
        num2 = float(input("Enter your second number here. "))

        if operation == "+":
            print(" {} + {} = ".format(num1, num2))
            print(num1 + num2)
        elif operation == "-":
            print("{} - {} = ".format(num1, num2))
            print(num1 + num2)
        elif operation == "*":
            print("{} * {} = ".format(num1, num2))
            print(num1 + num2)
        elif operation == "/":
            print("{} / {} = ".format(num1, num2))
            print(num1 / num2)
        elif operation == "%":
            print("{} % {} = ".format(num1, num2))
            print(num1 % num2)
        else:
            print("You did not enter a valid operation, please try again. ")
            continue
        ask()

calc()
