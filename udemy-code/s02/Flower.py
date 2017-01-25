import turtle
t = turtle.Pen()
turtle.bgcolor("light blue")
t.speed(0)
colors = ["purple", "hot pink"]
sides = 4
t.pencolor()
for x in range(310):
    t.width(1)
    t.pencolor( colors[ x % 2] )
    t.forward(x)
    t.left(92)

    
    
