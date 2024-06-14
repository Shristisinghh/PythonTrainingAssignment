# Function to find minimum and maximum values in a list
def find_min_max(numbers):
    if not numbers:
        return None, None

    min_value = min(numbers)
    max_value = max(numbers)

    return min_value, max_value


# Main function to take user input and call find_min_max function
def main():
    try:
        # Taking input from the user
        input_list = input("Enter a list of numbers separated by spaces: ").strip().split()

        # Converting input values to integers
        numbers = [int(num) for num in input_list]

        # Finding minimum and maximum values
        min_value, max_value = find_min_max(numbers)

        # Printing the result
        print(f"The minimum value is: {min_value}")
        print(f"The maximum value is: {max_value}")
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")


# Calling the main function
main()
