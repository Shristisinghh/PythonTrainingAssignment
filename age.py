# Function to calculate age based on birth year
def calculate_age(birth_year):
    # Getting the current year
    from datetime import datetime
    current_year = datetime.now().year

    # Calculating the age
    age = current_year - birth_year

    return age


# Main function to take user input and calculate age
def main():
    try:
        # Taking input from the user
        birth_year = int(input("Enter your birth year: "))

        # Calculating the age
        age = calculate_age(birth_year)

        # Printing the result
        print(f"You are {age} years old.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")


# Calling the main function
main()
