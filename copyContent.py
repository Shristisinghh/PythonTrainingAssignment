def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                # Read all contents from source file
                contents = source.read()
                # Write contents to destination file
                destination.write(contents)
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    try:
        source_file = input("Enter the source file name: ")
        destination_file = input("Enter the destination file name: ")

        # Copy contents from source to destination file
        copy_file(source_file, destination_file)

    except Exception as e:
        print(f"An error occurred: {e}")


# Calling the main function to start the program
main()
