print(" Welcome to the Simple Calculator App!")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Handle division by zero
    if b == 0:
        return " Cannot divide by zero!"
    return a / b

while True:
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print(" Thank you for using the Calculator!")
        break

    # Validate choice
    if choice not in ['1', '2', '3', '4']:
        print(" Invalid choice! Please try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print(" Invalid input! Please enter numbers only.")
        continue

    # Perform operation
    if choice == '1':
        result = add(num1, num2)
        symbol = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        symbol = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        symbol = '*'
    elif choice == '4':
        result = divide(num1, num2)
        symbol = '/'

    print(f"\n Result: {num1} {symbol} {num2} = {result}")