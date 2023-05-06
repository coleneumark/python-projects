# Pseudocode:
# Prompt user for a number to calculate factorial
# if number < 0 then
#    print("Error: Number entered was less than 0.")
# else then
#    if number >= 0 then
#        for i in range(2) then
#            fact = 1
#        for i in range(2, number +1) then
#            fact *= i
#    print("Factorial of", number, "is", fact)
# Program finishes
#############

# Prompt user for a number to calculate factorial
number = int(input("Enter the number for which you wish to calculate the factorial (an int >= 0): "))

if number < 0:
    print("Error: Number entered was less than 0.")
else:
    if number >= 0:
        for i in range(2):
            fact = 1
        for i in range(2, number +1):
            fact *= i
    print("Factorial of", number, "is", fact)
print("Finished!")