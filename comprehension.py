def string_to_list(input_string):
    char_list = [char for char in input_string]
    return char_list


def main():
    try:
        input_string = input("Enter a string: ")

        # Convert string to list of characters
        char_list = string_to_list(input_string)

        # Print the list of characters
        print(f"The string '{input_string}' converted to a list of characters:")
        print(char_list)

    except Exception as e:
        print(f"An error occurred: {e}")


# Calling the main function to start the program
main()
