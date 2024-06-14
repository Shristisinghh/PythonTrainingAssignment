# Function to generate the first n Fibonacci numbers
def generate_fibonacci(n):
    fibonacci_sequence = []

    # Handling edge case for n = 0
    if n == 0:
        return fibonacci_sequence

    # Initializing the first two Fibonacci numbers
    fibonacci_sequence.append(0)
    if n > 1:
        fibonacci_sequence.append(1)

    # Generating Fibonacci sequence
    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence


# Main function to take user input and generate Fibonacci sequence
def main():
    try:
        # Taking input from the user
        n = int(input("Enter the number of Fibonacci numbers to generate: "))

        # Generating the Fibonacci sequence
        fibonacci_numbers = generate_fibonacci(n)

        # Printing the Fibonacci sequence
        if fibonacci_numbers:
            print(f"The first {n} Fibonacci numbers are: {fibonacci_numbers}")
        else:
            print("No Fibonacci numbers to generate.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


# Calling the main function
main()
