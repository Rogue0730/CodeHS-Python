"""
This program asks the user for three ingredients,
three amounts, and a number of servings, and
determines how much of each ingredient is needed
to serve the specified number of servings.
"""
# Ingredient One
in1 = str(input("Enter ingredient 1: "))
in1_ounces = float(input("Ounces of "+ str(in1)))
# Ingredient Two
in2 = str(input("Enter ingredient 2: "))
in2_ounces = float(input("Ounces of "+ str(in2)))
# Ingredient Three
in3 = str(input("Enter ingredient 3: "))
in3_ounces = float(input("Ounces of "+str(in3)))
# Number of servings
numserv = int(input("Number of servings: "))

print("Total ounces of " + in1 + ": " + str((in1_ounces*numserv)))
print("Total ounces of " + in2 + ": " + str((in2_ounces*numserv)))
print("Total ounces of " + in3 + ": " + str((in3_ounces*numserv)))