# Calculating the Fibonacci Sequence with a for loop
# Establish changeable numbers for the initial steps of sequence
# Program prompts the user for the number of terms
# Calculate the number of terms in the sequence
# while limit >= 0 then
#    if limit <= 0 then
#        print("Error: Number entered was less than or equal to 0.")
#    elif limit == 1 then
#        print("Series is:", f_0)
#   elif limit == 2 then
#       print("Series is: ", f_0, ", ", f_1, sep="")
#    else then
#        print("Series is: ", f_0, ", ", f_1, sep="", end="")
#        b, a = f_1, f_0
#        for i in range(2, limit) then
#            b, a = b + a, b
#            print(",", b + a, end="")
#    print newline
#    Program prompts the user for another number of terms
# else then
#    print("End of program.")
# print newline
# Program finishes
###############

# Establish changeable numbers for the initial steps of sequence
f_0 = 0
f_1 = 1

# Prompt the user for how far they want to go
limit = int(input("Enter the number of terms you want to calculate (an int >= 0: "))

while limit >= 0:
    if limit <= 0:
        print("Error: Number entered was less than or equal to 0.")
    elif limit == 1:
        print("Series is:", f_0)
    elif limit == 2:
        print("Series is: ", f_0, ", ", f_1, sep="")
    else:
        print("Series is: ", f_0, ", ", f_1, sep="", end="")

        b, a = f_1, f_0
        for i in range(2, limit):
            b, a = b + a, b
            print(",", b + a, end="")
    print()
    limit = int(input("Enter the number of terms you want to calculate (an int >= 0: "))
else:
    print("End of program.")
print()
print("Finished!")