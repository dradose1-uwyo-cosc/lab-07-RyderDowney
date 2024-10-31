# Ryder Downey
# UWYO COSC 1010
# Submission Date: 10/28/2024
# Lab 07
# Lab Section: 14
# Sources, people worked with, help given to: John Jones
# your
# comments
# here


# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered

while(True):
    factorial = 1
    upper_bound = input("Type 'exit' to end. Upper Bound:")
    if upper_bound.isdigit():
        if int(upper_bound) < 0:
            print("Must be a positive integer")
        elif int(upper_bound) > 0:
            for i in range(1, int(upper_bound)+1):
                factorial = factorial * i 
            print(factorial)
    elif upper_bound == "exit":
        break
    else:
        print("You need to enter a positive integer")    

print("*"*75)

# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 

num_sum = 0
while True:
    new_int = input("Type 'exit' to end. Pick a number: ")
    if new_int.lower() == "exit":
        print(f"Your final sum is {num_sum}")
        break
    elif new_int.lstrip('-').isdigit():  
        new_int = int(new_int)  
        num_sum += new_int  
    else:
        print("You need to enter a positive or negative integer!")

print("*"*75)

# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 

while True:
    user_input = input("Enter calculation (Type 'exit' to leave): ").strip()
    if user_input.lower() == "exit":  
        print("Goodbye!")
        break

    expression = user_input.replace(" ", "")  
    result = None  
    
    # Addition
    if "+" in expression:
        operands = expression.split("+")
        if operands[0].isdigit() and operands[1].isdigit(): #uses indexing to get operands
            result = int(operands[0]) + int(operands[1])
    # Subtraction
    elif "-" in expression:
        operands = expression.split("-")
        if operands[0].isdigit() and operands[1].isdigit():
            result = int(operands[0]) - int(operands[1])
    # Multiplication
    elif "*" in expression:
        operands = expression.split("*")
        if operands[0].isdigit() and operands[1].isdigit():
            result = int(operands[0]) * int(operands[1])
    # Division
    elif "/" in expression:
        operands = expression.split("/")
        if operands[0].isdigit() and operands[1].isdigit():
            # Check for division by zero
            if int(operands[1]) != 0:
                result = int(operands[0]) / int(operands[1])
            else:
                print("Error: Division by zero is undefined.")
                continue
    # Modulus
    elif "%" in expression:
        operands = expression.split("%")
        if operands[0].isdigit() and operands[1].isdigit():
            result = int(operands[0]) % int(operands[1])
    
    if result is not None:
        print("Result:", result)
    else:
        print("Invalid input; please use 'operand operator operand' format.")
