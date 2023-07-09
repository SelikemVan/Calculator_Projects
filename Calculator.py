# Display the available operations
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get the user's choice of operation
choice = input("Enter choice (1-4): ")

# Check if the choice is valid
if choice in ('1', '2', '3', '4'):
    # Get the numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the selected operation based on the choice
    if choice == '1':
        result = num1 + num2  # Addition
        print("Result:", result)
    elif choice == '2':
        result = num1 - num2  # Subtraction
        print("Result:", result)
    elif choice == '3':
        result = num1 * num2  # Multiplication
        print("Result:", result)
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2  # Division
            print("Result:", result)
        else:
            print("Error: Division by zero")
else:
    print("Invalid input. Please enter a valid choice.")
