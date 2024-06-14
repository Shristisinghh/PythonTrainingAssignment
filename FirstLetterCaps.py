# Function to convert a string to title case
def convert_to_title_case(input_string):
    # Using the title() method to convert string to title case
    title_case_string = input_string.title()
    return title_case_string


# Main function to take user input and call the convert_to_title_case function
def main():
    # Taking input from the user
    input_string = input("Enter a string: ")

    # Converting the string to title case
    title_case_string = convert_to_title_case(input_string)

    # Printing the title case string
    print("String in title case:")
    print(title_case_string)


# Calling the main function
main()
