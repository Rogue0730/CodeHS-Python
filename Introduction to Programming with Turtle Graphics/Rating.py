rating = int(input("Enter a rating 1-10: "))
def bad_rating():
    color("red")
    pensize(10)
    left(45)
    for i in range(4):
        forward(50)
        backward(50)
        left(90)
def ok_rating():
    color("green")
    pensize(5)
    left(60)
    forward(100)
    backward(100)
    right(270)
    forward(20)
    
def good_rating():
    color("yellow")
    right(90)
    penup()
    backward(200)
    pendown()
    forward(400)


if rating <= 4:
    bad_rating()
elif rating >= 8:
    ok_rating()
else:
    good_rating()