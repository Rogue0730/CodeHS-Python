penup()
setposition(0,-200)
pendown()

def ball(radius):
    begin_fill()
    color("gray")
    circle(radius)
    end_fill()

get_radius = int(input("What should the radius be? "))


ball(get_radius)

penup()
left(90)
forward(200)
right(90)

ball(get_radius / 2)

penup()
left(90)
forward(100)
right(90)

ball(get_radius / 4)