speed(0)

def draw_square():
    pendown()
    for i in range(4):
        forward(50)
        left(90)
    penup()
    left(90)
    forward(50)
    right(90)
    forward(25)

def draw_circle():
    pendown()
    circle(25)
    penup()
    backward(25)
    left(90)
    forward(50)
    right(90)

penup()
setposition(-25, -200)

for i in range(4):
    draw_square()
    draw_circle()