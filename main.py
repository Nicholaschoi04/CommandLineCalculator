print("Hello! This is Nicholas' calculator!")


def addition():
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")


def subtraction():
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")


def multiplication():
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")


def division():
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")


while True:
    print("Please select an operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Select (1-4) for calculations or 5 to quit: ")
    if choice == "1":
        addition()
    elif choice == "2":
        subtraction()
    elif choice == "3":
        multiplication()
    elif choice == "4":
        division()
    else:
        quit()