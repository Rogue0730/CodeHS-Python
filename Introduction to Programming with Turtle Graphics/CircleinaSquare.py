circle_radius = int(input("What radius should te circle be? "))

def draw_blue_circle():
    color("blue")
    begin_fill()
    circle(circle_radius)
    end_fill()    
    
penup()
setposition(-100,-100)
pendown()

color("red")
begin_fill()

for i in range(4):
    forward(200)
    left(90)
    
end_fill()

penup()
forward(100)
pendown()

draw_blue_circle()