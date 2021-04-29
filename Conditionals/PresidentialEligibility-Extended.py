age = int(input("Age: "))
is_born_in_us = input("Born in the U.S? (yes/no): ")
time_of_residency = int(input("Years of Residency "))

if age >= 35 and is_born_in_us == "Yes" and time_of_residency >= 14:
    print ("You are eligible to run for president. ")
else: 
    print ("You are not eligible to run for president. ")
    
if age < 35:
    print ("You are too young. You must be at least 35 years old. ")
if is_born_in_us == "No":
    print ("You must be born in the U.S. to run for president. ")
if time_of_residency < 14:
    print ("You have not been a resident for long enough. ")