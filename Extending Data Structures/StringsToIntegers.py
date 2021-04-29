list_of_strings = ["a", "2", "7", "zebra"]

num=[]
a=input("Enter the number count")
i=0

for i in range(0,int(a)):
   b=input("Enter the number")
   num.append(b)

def safe_int(string):
    return int(string) if string.isdigit() else 0

list_of_strings = ["a", "2", "7", "zebra"]
list_of_numbers = [safe_int(num) for num in list_of_strings] # <-- use the function INSIDE the list comprehension
print(list_of_numbers)