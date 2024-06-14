# Function to write user input to a text file
def write_to_file():
    # Taking input from the user
    user_input = input("Enter a string to write to the file: ")

    # Specifying the file name
    file_name = "output.txt"

    # Writing the input to the file
    with open(file_name, "w") as file:
        file.write(user_input)

    # Confirming the write operation
    print(f"The string has been written to {file_name}.")


# Calling the function
write_to_file()
