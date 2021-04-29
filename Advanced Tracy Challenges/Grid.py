speed(0)
xaxis = -185
yaxis = -200

yaxis1 = 185
def draw_axis():
    penup()
    backward(200)
    pendown()
    forward(400)
    setposition(0, 0)
    left(90)
    backward(200)
    forward(400)
    
def draw_line():
    color("gray")
    forward(400)
    
def new_col():
    penup()
    setposition(xaxis, yaxis)
    pendown()
def new_row():
    left(90)
    forward(17)
    right(90)
def draw_row():
    color("gray")
    forward(400)
    penup()
    backward(400)
    pendown()
    
draw_axis()

for i in range(28):
    new_col()
    draw_line()
    xaxis = xaxis + 17
    
speed(3) 
penup()
left(90)
setposition(200, 185)
pendown()
for i in range(28):
    speed(0)
    draw_row()
    new_row()

penup()
setposition(0, 0)
pendown()
pensize(5)
color("black")
draw_axis()