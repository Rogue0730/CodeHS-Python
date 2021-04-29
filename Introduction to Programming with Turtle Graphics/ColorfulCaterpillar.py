forward_amount = 40


def draw_circle(color_choice):
    begin_fill()
    color(color_choice)
    circle(20)
    end_fill()
    


penup()
backward(150)
pendown()

for i in range(2):
    draw_circle("blue")
    penup()
    forward(forward_amount)
    pendown()
    draw_circle("green")
    penup()
    forward(forward_amount)
    pendown()
    draw_circle("yellow")
    penup()
    forward(forward_amount)
    pendown()
    draw_circle("red")
    penup()
    forward(forward_amount)
    pendown()