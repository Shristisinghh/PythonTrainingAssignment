# Function to count occurrences of an element in a list
def count_occurrences(input_list, element):
    count = 0
    for item in input_list:
        if item == element:
            count += 1
    return count


# Main function to take user input and call count_occurrences function
def main():
    try:
        # Taking input from the user
        input_list = input("Enter a list of elements separated by spaces: ").strip().split()
        element = input("Enter the element to count: ")

        # Converting input values to appropriate types
        element = eval(element)  # Using eval() to convert element to appropriate type

        # Converting input_list elements to appropriate types
        input_list = [eval(item) for item in input_list]

        # Counting occurrences of element
        occurrences = count_occurrences(input_list, element)

        # Printing the result
        print(f"The element {element} occurs {occurrences} time(s) in the list.")
    except ValueError:
        print("Invalid input. Please enter elements correctly.")


# Calling the main function
main()
