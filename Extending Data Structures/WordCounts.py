my_dictionary = {}

text = input("Enter some text: ")

my_list = text.split()

for word in my_list:
    if word in my_dictionary:
        my_dictionary[word] = my_dictionary[word] + 1
    else: 
        my_dictionary[word] = 1
        
print(my_dictionary)