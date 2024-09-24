#Loops and indents
# Author: Flanny Xue
# Date: 25-09-2024
# Version 2
#TODO:
    # Get user input (ask the user for their name)
    # Ask the user for two numbers
    # Add the numbers together

# Ask the user for thier name
name = input ("What is your name?")
print(f"Kia ora {name}.") #f stands for format. We are formatting the print statement.

# Ask the user for two numbers
num_1 = int(input("What is your favourite number?"))
num_2 = int(input("What is your least favourite number?"))

# Add numbers togther
sum = (num_1 + num_2)
print(f"The numbers added together equal to {sum}")


# for loops, repeat for a set number of times.
# for starts the loop
# next is the name of the loop
# in range tells the loop how many times to run
# the number in the () is how many times it repeats
for name_of_loop in range(5):
    print("ha")

# while loop, runs unti a condition is met or no longer is met
keep_going = "" # empty variable
while keep_going == "":
    print("looping")
    print("still looping")

    keep_going = input("Again? Or press any other key to quit")