my_dictionary = {}

while True:
    name = input("Enter a name: ")
    if name=="":
        break
    elif name in my_dictionary:
        print("phone number: " + my_dictionary[name])
    else:
        phone_num = input("Enter a phone number: ")
        my_dictionary[name] = phone_num
print(my_dictionary)