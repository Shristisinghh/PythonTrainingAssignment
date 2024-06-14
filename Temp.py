def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def main():
    try:
        choice = input("Enter '1' to convert Celsius to Fahrenheit, or '2' to convert Fahrenheit to Celsius: ")

        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")

        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius.")

        else:
            print("Invalid choice. Please enter '1' or '2'.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Calling the main function
main()
