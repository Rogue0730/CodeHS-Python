speed(0)

def draw_square(order):
    pendown()
    if order % 2 == 0:
        begin_fill()
    for i in range(4):
        forward(20)
        left(90)
    if order % 2 == 0:
        end_fill()
    penup()
    forward(30)
    
penup()
backward(85)
for order in range(6):
    draw_square(order)