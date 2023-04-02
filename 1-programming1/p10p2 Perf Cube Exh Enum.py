# Pseudocode:
# Prompt the user for a positive integer
# U# Program uses exhaustive enumeration to find an approximate solution
# Define variables
# Establish list of perfect cubes
# if number > 0 or number < 0 then
#    while abs(number - cube ** 3) >= epsilon and cube <= number then
#        cube += step
#        numGuesses += 1
#    if abs(number - cube ** 3) < epsilon then
#        print("The approximate cube root of", number, "is", cube)
#    else then
#        print("Failed to find a cube root of", number)  
#    if number in cube_root_list then
#        print(number, "is a perfect cube.")
# else then
# Program finishes
#############


# Program uses exhaustive enumeration to find an approximate solution
# Define variables
epsilon = 0.01
step = epsilon ** 2
numGuesses = 0

# Prompt user to enter a number
number = int(input("Enter a number to find its cube root: "))
cube = 0
if number > 0 or number < 0:
    while abs(number - cube ** 3) >= epsilon and cube <= number:
        cube += step
        numGuesses += 1
    if abs(number - cube ** 3) < epsilon:
        print("The approximate cube root of", number, "is", cube)
    else:
        print("Failed to find a cube root of", number)  
else:
    print("Finished!")