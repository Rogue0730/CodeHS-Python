def draw_circle(radius, color_choice):
    pendown
    color(color_choice)
    begin_fill()
    circle(radius)
    end_fill()
    penup()
    
def happy_face():
    setposition(-60, 0)
    pendown()
    right(90)
    pensize(10)
    circle(60,180)

def sad_face():
    setposition (60,-50)
    pendown()
    left(90)
    pensize(10)
    circle(60,180)
    
penup()


happy = input("Are you happy?: ")

setposition(0, -100)
draw_circle(100, "yellow")
setposition(30, 30)
draw_circle(10,"black")
setposition(-30, 30)
draw_circle(10, "black")

if happy == "yes":
    happy_face()
else: 
    sad_face()