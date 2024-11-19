# This is a bits calulator that calculates the number of bits needed to represent data in its uncompressed form.
# Author: Flanny Xue
# Date: 13-11-2024
# Version 1

'''
 Info that I gathered from the interent: 
Text: Each character is represented using ASCII encoding, which requires 8 bits per character.
Image: Each pixel in a 24-bit color image requires 24 bits.
Integer: The number of bits needed depends on the integer value's size.

I think I'm supposed to write three calculators, one for each.
I copies some little parts from my fence cost calculator program.
'''
# This is the bits calculator for integers
def calculate_bits_for_integer():
    while True:
        try:
            # Prompt the user to enter a value
            value = input("Enter a non-negative integer: ")

            # Convert the input to an integer
            number = int(value)

            # Check if the integer is greater than or equal to 0
            if number >= 0:
                # Calculate the number of bits needed to store this integer
                if number == 0:
                    bits = 1  # the number zero needs 1 bit
                else:
                    bits = number.bit_length()  # Calculate the number of bits required

                # Display the result and break the loop
                print(f"Bits needed for the integer {number}: {bits} bits")
                break
            else:
                print("The value must be a non-negative integer. Please try again.")
        except ValueError:
            # Handle the case where the input is not an integer
            print("Invalid input. Please enter a valid non-negative integer.")


# This is the bits calculator for text 
def calculate_bits_for_text():
    while True:
        try:
            # Ask the user to enter a string of text
            text = input("Enter a text string: ")

            # Ensure the input is not empty
            if text.strip() == "":
                print("The text cannot be empty. Please try again.")
                continue

            # Calculate the number of bits needed to store this text
            bits = len(text) * 8  # ASCII encoding uses 8 bits per character
            print(f"Bits needed for the text '{text}': {bits} bits")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")


# This is the bits calucaltor for image
def calculate_bits_for_image():
    while True:
        try:
            # Ask the user for image dimensions 
            width = int(input("Enter the image width (in pixels): "))
            height = int(input("Enter the image height (in pixels):"))

            # Convert the input to an integer
            number = int(value)

            # Check if the integer is greater than or equal to 0
            if number >= 0:
                # Calculate the number of bits needed for a 24-bit color image
                bits = width * height * 24 # 24 bits per pixel

                # Display the result and break the loop
                print(f"Bits needed for a {width}x{height} image: {bits} bits")
                break
            else:
                print("The value must be a non-negative integer. Please try again.")
        except ValueError:
            # Handle the case where the input is not an integer
            print("Invalid input. Please enter a valid non-negative integer.")

# Main program starts here
print("Choose the data type:")
print("1. Integer")
print("2. Text")
print("3. Image")

choice = input("Enter your choice (1,2, or 3): ")


# Decide which function to call based on user's choice
if choice == '1':
    calculate_bits_for_integer()
elif choice == '2':
    calculate_bits_for_text()
elif choice == '3':
    calculate_bits_for_image()
else:
    print("Invalid choice. Please enter 1, 2, or 3.")
    






