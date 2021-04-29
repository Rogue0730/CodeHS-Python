speed(0)

pensize(10)

def green_check():
    color("green")
    penup()
    backward(25)
    right(45)
    pendown()
    forward(35)
    left(90)
    forward(75)
    
user_number = int(input("guess a number between 1 and 10 "))
secret_number = 7

while user_number != secret_number:
    user_number = int(input("guess a number between 1 and 10 "))
green_check()