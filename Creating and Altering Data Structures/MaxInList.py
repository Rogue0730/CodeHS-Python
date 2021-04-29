# Write code here...
def max_int_in_list(my_list):
    highest = my_list[4]

    for num in my_list:
        if num > highest:
            highest = num
        return highest



my_list = [5, 2, -5, 10, 23, -21]
biggest_int = max_int_in_list(my_list)
print biggest_int