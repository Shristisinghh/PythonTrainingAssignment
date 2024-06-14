import csv


# Function to read and print data from a CSV file
def read_csv_file(filename):
    try:
        # Opening the CSV file in read mode
        with open(filename, mode='r') as file:
            # Creating a CSV reader object
            csv_reader = csv.reader(file)

            # Reading each row from the CSV file
            for row in csv_reader:
                # Printing each row to the console
                print(', '.join(row))  # Joining elements of row with a comma and space
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error occurred: {e}")


# Calling the function to read and print data from 'data.csv'
read_csv_file('data.csv')
