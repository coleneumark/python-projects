# Task:
# (a) Write a function that takes as its argument a non-negative integer and prints out that
# number of terms of the Fibonacci Series. This function should not return an explicit value.
# (b)  Write a program that prompts the user for an integer and checks that the number entered
# is non-negative. If it is, it calls the function defined in part (a); if not, it prints out an
# appropriate error message.
################
# Pseudocode:
# Prompt user to enter a number to find its square root
# if number >= 0 then
#    def approx_square_root(x) returns the Fibonacci sequence of its argument
# Declare variables for approximate result in exhaustive enumeration
#        epsilon = 0.01
#        step = epsilon ** 2
#        root = 0
#        while abs(number - root ** 2) >= epsilon and root <= number then
#            root += step
#        if abs(number - root ** 2) < epsilon then
#            return root
#        else then
#            return print("Failed to find a square root of", number)
#    print("The square root of", number, "is", approx_square_root(number))
# else then
#    print("Error. The number needs to be >= 0.")
#################


# Prompt user to enter a number to find its square root
number = float(input("Enter a number to find its square root: "))
if number >= 0:
    def approx_square_root(x):
        """Function that returns the Fibonacci sequence of its argument
    
        Assumes a non-negative integer as its argument
        """
        epsilon = 0.01
        step = epsilon ** 2
        root = 0
        while abs(number - root ** 2) >= epsilon and root <= number:
            root += step
        if abs(number - root ** 2) < epsilon:
            return root
        else:
            return print("Failed to find a square root of", number)
    print("The square root of", number, "is", approx_square_root(number))
else:
    print("Error. The number needs to be >= 0.")