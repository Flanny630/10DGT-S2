# Conditional statements and while loops
# Author: Flanny Xue
# Date : 2024-09-07
# Version 1
# TODO: Create a program that asks a user a question and returns a response based on the answer of the user.


# Main loop. Keeps running until a condition is met
keep_going = ""
while keep_going == "":
    # Asking the user for an input to a solution
    like_coffee = input("Do you like coffee? ").lower()
    # .lower() convet the input to lower case

    if like_coffee == "yes" or like_coffee == "y":
        print ("I like coffee too!")
    elif like_coffee == "no" or like_coffee == "n":
        print("You are missing out")      

        like_tea= input("Would you like tea instead? ").upper()
        #.upper() converts to upper case.
        if like_tea == "YES" or like_tea == "Y":
            print("Good for you. Give coffee another try!")
        elif like_tea == "NO" or like_tea == "N":
            print("Sorry, that is all I have")


    else: 
        print ("I don't understand")

    keep_going = input("Press <enter> to continue or any key to quit")
