names_list = []
for i in range(0, 5):
    names_list.append(input("Name: "))
sorted_last_names = sorted([name.split()[-1] for name in names_list])
print(sorted_last_names)