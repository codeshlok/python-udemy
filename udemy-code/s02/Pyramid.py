import turtle
t = turtle.Pen()
t.speed(0)
size = int(turtle.numinput("Size",
                "How much size do you want?"))
for x in range(size):
    t.forward(x)
    t.left(90)
