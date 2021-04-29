speed(5)
penup()

for i in range(25,101,25):
    setposition(0, 0)
    right(90)
    forward(i)
    left(90)
    pendown()
    circle(i)
    penup()