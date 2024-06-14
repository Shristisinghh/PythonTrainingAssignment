import string


# Function to remove punctuation from a string
def remove_punctuation(input_string):
    # Define a translation table that maps each punctuation character to None
    translator = str.maketrans('', '', string.punctuation)

    # Use translate() method to remove punctuation
    cleaned_string = input_string.translate(translator)

    return cleaned_string


# Main function to take user input and call remove_punctuation function
def main():
    # Taking input from the user
    input_string = input("Enter a string with punctuation: ")

    # Removing punctuation
    cleaned_string = remove_punctuation(input_string)

    # Printing the cleaned string
    print("String without punctuation:")
    print(cleaned_string)


# Calling the main function
main()
