speed(0)
circle_amount = 8
xpos = -180
ypos = -200

def draw_circle_row():
    for i in range(circle_amount):
        circle(25)
        penup()
        forward(50)
        pendown()

penup()
setposition(-180,-200)
pendown()
for i in range(8):
    penup()
    setposition(-180,ypos)
    pendown()
    draw_circle_row()
    ypos = ypos + 50
    circle_amount = circle_amount - 1