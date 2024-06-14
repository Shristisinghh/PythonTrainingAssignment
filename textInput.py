# Function to read and print the content of a text file
def read_from_file():
    # Specifying the file name
    file_name = "output.txt"

    try:
        # Reading the content of the file
        with open(file_name, "r") as file:
            content = file.read()

        # Printing the content to the console
        print("The content of the file is:")
        print(content)
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Calling the function
read_from_file()
