# Pseudocode:
# Prompt user for a number of terms to calculate Catalan numbers
# Initialise first two numbers for sequence
# if limit < 0 then
#    print("Error: Number entered was less than 0.", end="")
# else then
#    print("Catalan numbers are: ", end="")
#    if limit == 0 then
#        print(cat_0, end="")
#    if limit == 1 then
#        print(cat_0, ", ", cat_1, sep="", end="")
#    if limit > 1 then
#        print(cat_0, ", ", cat_1, sep="", end="")
#        for i in range(2, limit + 1) then
# Calculate factorial of 2n
#            if (2 * i) == 0 then
#                fact_1 = 1
#            elif (2 * i) == 1 then
#                fact_1 = 1
#            else then
#                fact_1 = 1
#                for j in range(2, (2 * i) + 1) then
#                    fact_1 *= j
# Calculate factorial of (n + 1)
#            if (i + 1) == 0 then
#                fact_2 = 1
#            elif (i + 1) == 1 then
#                fact_2 = 1
#            else then
#                fact_2 = 1
#                for k in range(2, (i + 1) + 1) then
#                    fact_2 *= k
# Calculate factorial of n
#            if i == 0 then
#                fact_3 = 1
#            elif i == 1 then
#                fact_3 = 1
#            else then
#                fact_3 = 1
#                for l in range(2, i + 1) then
#                    fact_3 *= l
# Perform final Catalan calculation
#            cat_i = fact_1 / (fact_2 * fact_3)
#            i += 1   
#            print(", ", int(cat_i), sep="", end="")
# print newline
# Program finishes
#############

limit = int(input("Enter the number of terms you want to calculate (an int >= 0): "))
cat_0 = 1
cat_1 = 1

if limit < 0:
    print("Error: Number entered was less than 0.", end="")
else:
    print("Catalan numbers are: ", end="")
    if limit == 0:
        print(cat_0, end="")
    if limit == 1:
        print(cat_0, ", ", cat_1, sep="", end="")
    if limit > 1:
        print(cat_0, ", ", cat_1, sep="", end="")
        for i in range(2, limit + 1):
        # Calculate factorial of 2n
            if (2 * i) == 0:
                fact_1 = 1
            elif (2 * i) == 1:
                fact_1 = 1
            else:
                fact_1 = 1
                for j in range(2, (2 * i) + 1):
                    fact_1 *= j
        # Calculate factorial of (n + 1)
            if (i + 1) == 0:
                fact_2 = 1
            elif (i + 1) == 1:
                fact_2 = 1
            else:
                fact_2 = 1
                for k in range(2, (i + 1) + 1):
                    fact_2 *= k
        # Calculate factorial of n
            if i == 0:
                fact_3 = 1
            elif i == 1:
                fact_3 = 1
            else:
                fact_3 = 1
                for l in range(2, i + 1):
                    fact_3 *= l
            cat_i = fact_1 / (fact_2 * fact_3)
            i += 1   
            print(", ", int(cat_i), sep="", end="")
print()
print("Finished!")