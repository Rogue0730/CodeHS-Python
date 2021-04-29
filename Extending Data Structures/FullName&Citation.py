first_name = input("Enter your first name: ")
last_name = input("Enter you last name: ")

print("Full name = " + first_name + " " + last_name)

first_name, last_name = last_name, first_name

print("Citation: " + first_name + ", " + last_name)