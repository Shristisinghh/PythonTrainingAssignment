# Function to get user input and calculate the sum
def sum_two_numbers():
    try:
        # Taking input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Calculating the sum
        total = num1 + num2

        # Printing the result
        print(f"The sum of {num1} and {num2} is {total}.")
    except ValueError:
        print("Invalid input. Please enter numerical values.")


# Calling the function
sum_two_numbers()
