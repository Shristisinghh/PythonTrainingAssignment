# Function to calculate the sum of digits of a number
def sum_of_digits(number):
    # Initialize sum to zero
    digit_sum = 0

    # Iterate over each digit in the number
    while number > 0:
        # Extract the last digit using modulo operation
        digit = number % 10
        # Add the digit to the sum
        digit_sum += digit
        # Remove the last digit from the number
        number //= 10

    return digit_sum


# Main function to take user input and calculate sum of digits
def main():
    try:
        # Taking input from the user
        num = int(input("Enter a number: "))

        # Calculating the sum of digits
        result = sum_of_digits(num)

        # Printing the result
        print(f"The sum of digits of {num} is: {result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")


# Calling the main function
main()
