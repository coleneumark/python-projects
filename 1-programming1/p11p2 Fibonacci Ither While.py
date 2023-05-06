# Calculating the Fibonacci Sequence with a while loop
# Establish changeable numbers for the initial steps of sequence
# Program prompts the user for the number of terms
# Calculate the number of terms in the sequence
# if limit <= 0 then
#    print("Error: Number entere1d was less than or equal to 0.")
# elif limit == 1 then
#    print("Series is:", f_0)
# elif limit == 2 then
#    print("Series is: ", f_0, ", ", f_1, sep="")
# else then
#    print("Series is: ", f_0, ", ", f_1, sep="", end="")
#    b, a = f_1, f_0
#    i = 2
#    while i < limit then
#        print(",", b + a, end="")
#        b, a = b + a, b
#        i += 1
# print newline
# Program finishes
###############

# Establish changeable numbers for the initial steps of sequence
f_0 = 0
f_1 = 1

# Prompt the user for how far they want to go
limit = int(input("Enter the number of terms you want to calculate (an int >= 0: "))

# Calculate the number of terms in the sequence
if limit <= 0:
    print("Error: Number entere1d was less than or equal to 0.")
elif limit == 1:
    print("Series is:", f_0)
elif limit == 2:
    print("Series is: ", f_0, ", ", f_1, sep="")
else:
    print("Series is: ", f_0, ", ", f_1, sep="", end="")

    b, a = f_1, f_0
    i = 2
    while i < limit:
        print(",", b + a, end="")
        b, a = b + a, b
        i += 1
print()
print("Finished!")