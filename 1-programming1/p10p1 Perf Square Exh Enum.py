# Pseudocode:
# Program uses exhaustive enumeration to find an approximate solution
# Define variables
# Establish list of perfect squares
# Prompt user to enter a number to find its square root
# if number >= 0 then
#    while abs(number - root ** 2) >= epsilon and root <= number then
#        root += step
#        numGuesses += 1
#    print("Number of guesses:", numGuesses)
#    if abs(number - root ** 2) < epsilon then
#        print("The approximate square root of", number, "is", root)
#    else then
#        print("Failed to find a square root of", number)
#    if number in perfect_square_list then                 
#        print(number, "is a perfect square.")
# else then
# Program finishes

# None of the numbers will be a perceived as a perfect square, because
# exhaustive enumeration presents the square root as just beneath the whole
# number. That is why it will always say it is not a perfect square and why I
# used a list of perfect squares to identify them.
#############


# Program uses exhaustive enumeration to find an approximate solution
# Define variables
epsilon = 0.01
step = epsilon ** 2
numGuesses = 0
# Establish list of perfect squares
perfect_square_list = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961]

# Prompt user to enter a number to find its square root
number = int(input("Enter a number to find its square root: "))
root = 0
if number >= 0:
    while abs(number - root ** 2) >= epsilon and root <= number:
        root += step
        numGuesses += 1
    print("Number of guesses:", numGuesses)
    if abs(number - root ** 2) < epsilon:
        print("The approximate square root of", number, "is", root)
    else:
        print("Failed to find a square root of", number)
    if number in perfect_square_list:                      
        print(number, "is a perfect square.")
else:
    print("Finished!")