speed(0)

def draw_square_row(row):
    for x in range(10):
        pendown()
        if (x + row) % 2 == 0:
            color("red")
        begin_fill()
        for i in range(4):
            forward(40)
            left(90)
        end_fill()
        color("black")
        penup()
        forward(40)
        
def move_up_a_row():
    left(90)
    forward(40)
    right(90)
    backward(400)
    
penup()
setposition(-200,-200)

for row in range(10):
    draw_square_row(row)
    move_up_a_row()