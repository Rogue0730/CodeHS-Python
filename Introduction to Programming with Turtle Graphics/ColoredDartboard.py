radius = 100

def draw_circle():
    pendown()
    color(color_choice)
    begin_fill()
    circle(radius)
    end_fill()
    penup()
    left(90)
    forward(25)
    right(90)
    
penup()
setposition(0, -100)

for i in range(4):
    color_choice = input("What color would you like to point your circle?") 
    draw_circle()
    radius = radius - 25