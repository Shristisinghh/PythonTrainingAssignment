# Function to check if a number is even or odd
def check_even_or_odd():
    try:
        # Taking input from the user
        number = int(input("Enter a number: "))

        # Checking if the number is even or odd
        if number % 2 == 0:
            print(f"The number {number} is even.")
        else:
            print(f"The number {number} is odd.")
    except ValueError:
        print("Invalid input. Please enter an integer.")


# Calling the function
check_even_or_odd()
