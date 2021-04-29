# This function takes a single argument and returns nothing. It assumes the
# argument is a list. It appends the number 6 to the list.
def change_my_list(my_list):
    my_list.append(6)

numbers = [1, 2, 3]
print numbers

# This will affect numbers!
change_my_list(numbers)
print numbers