age = input("Age: ")
was_born_in_us = input("Born in the U.S.? (Yes/No): ")
years_of_residency = input("Years of Residency: ")

if int(age) >= 35 and was_born_in_us == "Yes" and years_of_residency >= 14:
    print("You are eligible to run for president!")
else:
    print("You are not eligible to run for president.")