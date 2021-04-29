radius = 20

penup()
setposition(0, -180)
pendown()


for i in range(7):
    circle(radius, 360, i)
    radius = radius + 20