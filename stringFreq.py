# Function to count the frequency of each character in a string
def count_character_frequency(input_string):
    # Initialize an empty dictionary to store character frequencies
    frequency = {}

    # Count frequency of each character
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


# Main function to take user input and call the count_character_frequency function
def main():
    # Taking input from the user
    input_string = input("Enter a string: ")

    # Calculating character frequencies
    character_frequency = count_character_frequency(input_string)

    # Printing the frequency of each character
    print("Character frequencies:")
    for char, freq in character_frequency.items():
        print(f"{char}: {freq}")


# Calling the main function
main()
