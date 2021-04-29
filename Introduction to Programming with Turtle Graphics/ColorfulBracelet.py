speed(0)

def draw_red_link():
    color("red")
    penup()
    forward(100)
    begin_fill()
    pendown()
    circle(10)
    penup()
    end_fill()
    backward(100)
    left(10)
    
def draw_blue_link():
    color("blue")
    penup()
    forward(100)
    begin_fill()
    pendown()
    circle(10)
    penup()
    end_fill()
    backward(100)
    left(10)
    
def draw_purple_link():
    color("purple")
    penup()
    forward(100)
    begin_fill()
    pendown()
    circle(10)
    penup()
    end_fill()
    backward(100)
    left(10)
    
for i in range(12):
    draw_red_link()
    draw_blue_link()
    draw_purple_link()