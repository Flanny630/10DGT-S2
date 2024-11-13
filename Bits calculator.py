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

def calculate_bits_for_integer():
    #Ask the user for an integer input
    number = int(input("Enter an integer:"))

    # Calculate the number of bits needed to store this integer
    if number == 0:
        bits = 1 # the number zero would need 1 bit
    else: 
        bits = number.bit_length() # bit_length gives the number of bits to represent the number 
    
    print(f"Bits needed for the integer {number}: {bits} bits")

def calculate_bits_for_text():
    # Ask the user for a text input
    text = input("Enter the text: ")

    # Calculate the number of bits needed to store this text
    bits = len(text) * 8 # ASCII encoding uses 8 bits per character

    print(f"Bits needed for the text '{text}': {bits} bits")

def calculate_bits_for_image():
    # Ask the user for image dimensions 
    width = int(input("Enter the image width (in pixels): "))
    height = int(input("Enter the image height (in pixels):"))

    # Calculate the number of bits needed for a 24-bit color image
    bits = width * height * 24 # 24 bits per pixel

    print(f"Bits needed for a {width}x{height} image: {bits} bits")

# Main program starts here
print("Choose the data type:")
print("1. Integer")
print("2. Text")
print("3. Image")

choice = input("Enter your choice (1,2, or 3): ")

# Decide which function to call based on user's choice
if choice == "1":
    calculate_bits_for_integer()
elif choice == "2":
    calculate_bits_for_text()
elif choice == "3":
    calculate_bits_for_image()
else:
    print("Invalid choice. Please enter 1, 2, or 3.")



'''
# functions go here
#1 usage

def statement_generator (statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Main routine goes here
statement_generator( statement: "Instructions", decoration: "-")
'''