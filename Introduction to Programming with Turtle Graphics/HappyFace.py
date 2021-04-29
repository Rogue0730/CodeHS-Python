def draw_circle(radius, color_choice):
    pendown
    color("yellow")
    begin_fill()
    circle(radius)
    end_fill()
    penup()
    
def smile():
    setposition(-60, 0)
    pendown()
    right(90)
    pensize(10)
    circle(60,180)
    
penup()


happy = input("Are you happy?: ")


if happy == "yes":
    setposition(0, -100)
    draw_circle(100, "yellow")
    
    setposition(30, 30)
    draw_circle(10,"black")
    
    setposition(-30, 30)
    draw_circle(10, "black")
    
    smile()