# Function to calculate the factorial of a number
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


# Main function to take user input and calculate the factorial
def main():
    try:
        # Taking input from the user
        number = int(input("Enter a number to calculate its factorial: "))

        # Calculating the factorial
        result = factorial(number)

        # Printing the result
        print(f"The factorial of {number} is {result}.")
    except ValueError:
        print("Invalid input. Please enter an integer.")


# Calling the main function
main()
