speed(0)

def draw_circle_row():
    for i in range(10):
        pendown()
        begin_fill()
        color("light blue")
        circle(20)
        end_fill()
        penup()
        forward(40)
        
def move_up_a_row():
    left(90)
    forward(40)
    right(90)
    backward(400)
    
def make_highlight():
    for i in range(10):
        pendown()
        pensize(2)
        color("white")
        circle(10, 90)
        pensize(1)
        penup()
        backward(50)
        right(90)
        backward(10)
        
penup()
setposition(-180,-200)

for i in range(10):
    draw_circle_row()
    move_up_a_row()
    
left(90)
setposition(-170,-180)
for i in range(10):
    make_highlight()
    right(90)
    move_up_a_row()
    left(90)