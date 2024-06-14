# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if lengths are different
    if len(str1) != len(str2):
        return False

    # Sort characters in both strings and compare
    return sorted(str1) == sorted(str2)


# Main function to take user input and call the are_anagrams function
def main():
    # Taking input from the user
    input_str1 = input("Enter the first string: ")
    input_str2 = input("Enter the second string: ")

    # Checking if strings are anagrams
    if are_anagrams(input_str1, input_str2):
        print(f"'{input_str1}' and '{input_str2}' are anagrams.")
    else:
        print(f"'{input_str1}' and '{input_str2}' are not anagrams.")


# Calling the main function
main()
