my_string = list(input('Enter text: '))
my_string = ['!' if char == 'i' else char
             for char in my_string]
print(''.join(my_string))