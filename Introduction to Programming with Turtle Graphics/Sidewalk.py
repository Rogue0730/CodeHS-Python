speed(0)
def draw_square():
    pendown()
    for i in range(4):
        forward(50)
        left(90)
    penup()
    
def draw_row_of_squares():
    for i in range(8):
        draw_square()
        forward(50)
        


penup()
setposition(-200, 150)

for i in range(4):
    draw_row_of_squares()
    backward(50)
    right(90)
    backward(50)