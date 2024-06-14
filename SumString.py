# Function to calculate the sum of numbers in a list
def calculate_sum(numbers):
    total_sum = sum(numbers)
    return total_sum


# Main function to take user input and call calculate_sum function
def main():
    try:
        # Taking input from the user
        input_list = input("Enter a list of numbers separated by spaces: ").strip().split()

        # Converting input values to integers
        numbers = [int(num) for num in input_list]

        # Calculating the sum of numbers
        total_sum = calculate_sum(numbers)

        # Printing the sum
        print(f"The sum of numbers is: {total_sum}")
    except ValueError:
        print("Invalid input. Please enter numbers separated by spaces.")


# Calling the main function
main()
