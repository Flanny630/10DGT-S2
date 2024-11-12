# Area and perimeter calculator
# Author: Flanny Xue
# Date: 31-10-2024
# Version 2:0

''' # Ask the user for the width and height
# (assume they put in valid data)

width = float(input("Width "))
height = float(input("Height "))

# Calculate the area / perimeter
area = width * height
perimeter = 2 * (width + height)

# Output the area and perimeter 
print()
print(f"Perimeter: {perimeter} units")
print(f"Area: {area} square units") '''

# Ask user for width and loop until they enter a number that is more than zero
# This is version 1, and I have debuged a few errors that formed here.

def num_check(question): 
    done = False
    while not done:
        try: # This tries for a valid input
            num = float(input(question)) 
            if num > 0 :
                done = True
            else: 
                print("That is not a valid number. Please try again.")
        
        except ValueError:
            print("That is not a valid number. Please try again.")

    return(num) # Gives back the value of num
                # so that I can use it outside of the function.

# Main Routine starts here

keep_going = ""
while keep_going == "":
    print("\n Would you like a calculation for area and width? Please enter a width and a height.")

    # Get width and height
    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate area/ perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Display output
    print()
    print(f"Perimeter: {perimeter:.2f}m")
    print(f"Area: {area:.2f} square m")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

print("Thank you for using the area / perimeter calculator!")
