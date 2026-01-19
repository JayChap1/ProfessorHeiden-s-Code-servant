# Putting  this at the TOP of my file so you know what programs I'm using
import math  
# Step 1: Store first name in lowercase
first_name = "jason"
# Step 2: Store last name in uppercase
last_name = "CHAPMAN"
# Step 3: Print with first name uppercase, last name lowercase
print("Hello,", first_name.upper(), last_name.lower())
# Step 4: Print two newlines
print("\n\n")
# Step 5: Create variable with full name
full_name = first_name + " " + last_name
# Step 6: Slice last name from full_name and print
print(full_name[6:])
# Step 7: Replace last name with new string and print
full_name = full_name.replace("CHAPMAN", "CHAPMAN, Walsh College Student")
print(full_name)
# Step 8: Print quote with quotation marks
print("\"Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi\"")
# Step 9: Store two decimal numbers
num1 = 10.5
num2 = 3.2
# Step 10: Store math operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
# Step 11a: Concatenation
print(str(num1) + " plus " + str(num2) + " equals " + str(addition))
# Step 11b: String formatting expression
print("%s minus %s equals %s" % (num1, num2, subtraction))
# Step 11c: String formatting method
print("{} times {} equals {}".format(num1, num2, multiplication))
# Step 12: Square root of multiplication result
sq_root = round(math.sqrt(multiplication), 2)
print(f"The square root of {multiplication} equals {sq_root}")
# Step 13: Store month and day
month = "January"
day = 19
# Step 14: Print date with newline and two tabs
print("\n\t\tToday is day " + str(day) + " of the month of " + month + ".")