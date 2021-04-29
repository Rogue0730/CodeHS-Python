def update_counts(count_dictionary, word):
    if word in count_dictionary:
        count_dictionary[word] = count_dictionary[word] + 1
    else:
        count_dictionary[word] = 1
            
my_dictionary = {}
text = input("Enter some text: ")
my_list = text.split()
for word in my_list:
    update_counts(my_dictionary, word)
    
print my_dictionary