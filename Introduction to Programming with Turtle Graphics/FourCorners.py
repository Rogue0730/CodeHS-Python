speed(0)
square_length = int(input("Enter the length of square: "))
def draw_square():
    pendown()
    for i in range(4):
        forward(square_length)
        left(90)
    penup()

penup()
setposition(-200, -200)
draw_square()

penup()
setposition(-200,200 - square_length)
draw_square()

penup()
setposition(200 - square_length, 200 - square_length)
draw_square()

penup()
setposition(200 - square_length, -200)
draw_square()