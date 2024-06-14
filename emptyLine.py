# Function to read and print multiple lines of input
def read_multiple_lines():
    lines = []

    print("Enter multiple lines of text. Press Enter on an empty line to finish.")

    while True:
        # Reading input line
        line = input()

        # Checking if the line is empty
        if line == "":
            break

        # Appending the line to the list of lines
        lines.append(line)

    # Printing all the lines entered
    print("\nThe lines you entered are:")
    for line in lines:
        print(line)


# Calling the function
read_multiple_lines()
