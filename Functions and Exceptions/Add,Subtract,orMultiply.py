num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
opperation = input("Choose an operation (add, subtract, multiply): ")

def add_op():
    add_output = num1 + num2
    print(str(num1) + " + " + str(num2) + " = " + str(add_output))
def sub_op():
    sub_output = num1 - num2
    print(str(num1) + " - " + str(num2) + " = " + str(sub_output))
def multiply_op(): 
    multiply_output = num1 * num2
    print(str(num1) + " * " + str(num2) + " = " + str(multiply_output))
    

if opperation == "add":
    add_op()
elif opperation == "subtract":
    sub_op()
elif opperation == "multiply":
    multiply_op()
else:
    print("Invalid operation")