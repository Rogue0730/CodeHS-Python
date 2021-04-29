length = 10


def square():
    pendown()
    for i in range (4):
        forward(length)
        left(90)
    penup()
    
def draw_square():
    square()
    forward(length * 2)
    
    
penup()
setposition(-150, 0)

for i in range(5):
    draw_square()
    length = length + 10