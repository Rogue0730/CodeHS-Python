speed(9)

radius = 25

penup()
setposition(0,-25)

def draw_dart_board():
    pendown()
    circle(radius)
    right(90)
    penup()
    forward(25)
    pendown()
    left(90)




for i in range(4):
    draw_dart_board()
    radius = radius + 25