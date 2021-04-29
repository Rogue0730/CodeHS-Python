full_name = ""
name_amount = int(input("How many names do you have?: "))

for i in range(name_amount):
    name = input("Enter one of your names: ")
    full_name = full_name + " " + name
    
print(full_name)