# Task:
# (a) Write a function that takes as its single argument a non-negative 
# integer and returns the factorial of the number
# (b) Write a program that prompts the user for an integer and checks that 
# the number entered is non-negative. If it is, it calls the function defined 
# in part (a) and prints out the result; if not, it prints out an appropriate error message.
##############
# Pseudocode:
# def fact(x) returns the factorial of its argument
#    result = 1
#    for i in range(1, x + 1) then
#        result *= i
#    return result
# Prompt user for input of non-negative integer
# if number >= 0 then
#    print("The factorial of", number, "is", fact(number))
# else then
#    print("Error. Number must be >= 0.")
################
#import time

def fact(x):
    """Function that returns the factorial of its argument#

    Assumes that its argument is a non-negative integer
    """
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

# Prompt user for input
number = int(input("Enter a non-negative integer to find the factorial: "))
#start = time.time()
if number >= 0:
    print("The factorial of", number, "is", fact(number)) 
else:
    print("Error. Number must be >= 0.")
#end = time.time()
#print("It took:", end - start)
