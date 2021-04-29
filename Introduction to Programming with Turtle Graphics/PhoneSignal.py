speed(5)

for i in range(10, 51, 10):
    forward(10)
    left(90)
    forward(i)
    left(90)
    forward(10)
    left(90)
    forward(i)
    left(90)
    penup()
    forward(25)
    pendown()