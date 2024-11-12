# Fence cost calculator
# Author: Flanny Xue
# Date: 01-11-2024
# Version 2:0

# Write a program to calculate the cost of fencing for a rectangular area.  
# You can assume that all units are in meters. 
# You need to ask the user for the length and width of the area to be fenced.  
# You also need to ask for the cost of fencing per m.  
# Your program should then calculate the cost of fencing.  
# It should be possible to do more than one calculation at a time.​

'''
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
    # Get width and height
    print("This calculates the cost of a rectangular shaped fence")
    width = num_check("Width in meter: ")
    height = num_check("Height in meter: ")
    cost = num_check("Cost of fencing per meter: ")

    # Calculate perimeter and price for the fence
    perimeter = 2 * (width + height)
    price = perimeter * cost

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Price: ${price:.2f}")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

print("Thank you for using the area / perimeter calculator!") '''

# Version 2 contains two calculators.
# The first fence calculator calculates the fence cost for a rectangular shaped fence.
# The second fence calculator calculates the fence cost for a hexagon shaped fence.


# This is a fence calculator that calculates the fence cost for a rectangular shaped fence.
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

# Main Routine for a rectangualr shaped fence starts here

keep_going = ""
while keep_going == "":
    # Get width and height
    print("\n This calculates the cost of a rectangular shaped fence")
    width = num_check("Width in meter: ")
    height = num_check("Height in meter: ")
    cost = num_check("Cost of fencing per meter: ")

    # Calculate perimeter and price for the fence
    perimeter = 2 * (width + height)
    price = perimeter * cost

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Price: ${price:.2f}")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep calculating the cost of a rectangualr fence or any key to calculate the cost of a hexagon fence. ")
    print()



# This is a fence calculator that calculates the fence cost for a hexagon shaped fence.

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

# Main Routine for a hexagon shaped fence starts here

keep_going = ""
while keep_going == "":
    # Get width and height
    print("This calculates the cost of a hexagon shaped fence")
    length = num_check("Length of one of the sides in meter: ")
    cost = num_check("Cost of fencing per meter: ")

    # Calculate perimeter and price for the fence
    perimeter = 6 * length
    price = perimeter * cost

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Price: ${price:.2f}")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

print("Thank you for using the fence cost calculator!")