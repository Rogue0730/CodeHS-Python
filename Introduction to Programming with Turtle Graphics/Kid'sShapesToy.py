def set_position():
    penup()
    setposition(-100, 75)
    pendown()

penup()
setposition(-100, 75)
pendown()
begin_fill()
color("red")
circle(60, 360, 4)
end_fill()

penup()
setposition(100, 75)
pendown()
begin_fill()
color("blue")
circle(60)
end_fill()

penup()
setposition(100, -75)
pendown()
begin_fill()
color("green")
circle(60, 360, 5)
end_fill()

penup()
setposition(-100, -75)
pendown()
begin_fill()
color("yellow")
circle(60, 180)
end_fill()