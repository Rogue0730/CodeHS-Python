"""
The program first postions the turtle in the correct
area then start looping the circles for each row
"""
penup()
left(90)
backward(200)
right(90)
backward(100)
pendown()
# For loop that loops the circle row 1 (bottom)
for i in range(3):
    speed(10)
    circle(50)
    penup()
    forward(100)
    pendown()
    
penup()
backward(250)
left(90)
forward(100)
right(90)
pendown()
# Row 2 middle
for i in range(2):
    speed(10)
    circle(50)
    penup()
    forward(100)
    pendown()
    
penup()
backward(150)
left(90)
forward(100)
right(90)
pendown()
# Row 3 top
for i in range(1):
    speed(10)
    circle(50)
    penup()
    forward(100)
    pendown()