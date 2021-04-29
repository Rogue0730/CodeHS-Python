categories = 3

for i in range(categories):
    type_per_cat = 3
    category = input("Enter a category: ")
    a = category + ": "
    for x in range(type_per_cat):
        something = input("Enter something in that category: ")
        a = a + something + " "
    print a