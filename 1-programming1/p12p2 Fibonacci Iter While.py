# Task:
# (a) Write a function that takes as its argument a non-negative integer and prints out that
# number of terms of the Fibonacci Series. This function should not return an explicit value.
# (b)  Write a program that prompts the user for an integer and checks that the number entered
# is non-negative. If it is, it calls the function defined in part (a); if not, it prints out an
# appropriate error message.
################
# Pseudocode:
# Prompt the user for terms of Fibbonacci sequence to calculate
# if limit >= 0 thwn
#    def fib(number) returns the Fibonacci sequence of its argument
# Assigns first two values to variables
#        f_0 = 0
#        f_1 = 1
# Calculate the number of terms in the sequence
#        if number == 1 then
#            print("Series is:", f_0)
#        elif number == 2 then
#            print("Series is: ", f_0, ", ", f_1, sep="")
#        else then
#            print("Series is: ", f_0, ", ", f_1, sep="", end="")
#            b, a = f_1, f_0
#            i = 2
#            while i < number then
#                print(",", b + a, end="")
#                b, a = b + a, b
#                i += 1
# else then
#    print("Error. The number needs to be >= 0.")
# fib(limit)
####################


# Prompt the user for how far they want to go
limit = int(input("Enter the number of terms you want to calculate (an int >= 0: "))

if limit >= 0:
    def fib(number):
        """Function that returns the Fibonacci sequence of its argument
    
    Assumes a non-negative integer as its argument"""
        # Assigns first two values to variables
        f_0 = 0
        f_1 = 1
        # Calculate the number of terms in the sequence
        if number == 1:
            print("Series is:", f_0)
        elif number == 2:
            print("Series is: ", f_0, ", ", f_1, sep="")
        else:
            print("Series is: ", f_0, ", ", f_1, sep="", end="")
            b, a = f_1, f_0
            i = 2
            while i < number:
                print(",", b + a, end="")
                b, a = b + a, b
                i += 1
else:
    print("Error. The number needs to be >= 0.")

fib(limit)