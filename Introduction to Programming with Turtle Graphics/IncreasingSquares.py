length = 50
speed(0)

def draw_square(length):
    for i in range(4):
        forward(length)
        left(90)

while length < 400:
    penup()
    backward(length/2)
    right(90)
    forward(length/2)
    left(90)
    pendown()
    draw_square(length)
    penup()
    forward(length/2)
    left(90)
    forward(length/2)
    right(90)
    length = length + 50