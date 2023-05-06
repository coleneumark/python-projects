# Pseudocode:
# Prompt the user for a string to count the vowels within it
# Establish list of vowels
# Initialise vowel counter
# while string != "" then
#    for char in string then
#        if char in vowels then
#            counter_vowels += 1
#        else then
#            counter_vowels += 0
#    print("This string has", counter_vowels, "vowels.")
#    string = input("Enter a string: ")
# Program finishes
#############

string = input("Enter a string: ")
vowels = ["a", "e", "i", "o", "u"]
counter_vowels = 0

while string != "":
    for char in string:
        if char in vowels:
            counter_vowels += 1
        else:
            counter_vowels += 0
    print("This string has", counter_vowels, "vowels.")
    string = input("Enter a string: ")
print("Finished!")
    
