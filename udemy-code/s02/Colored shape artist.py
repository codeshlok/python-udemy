import turtle #turtle
t = turtle.Pen() #pen
turtle.bgcolor("light blue") #background color
t.speed(0)
colors = ["purple", "hot pink"] #change colors
sides = 6 #how many sides the shape has. do not modify
t.pencolor() #not sure. do not modify
for x in range(360): #the amount of times you draw a pixel
    t.width(x*sides/100) #width program
    t.forward(x * 3 / sides + x) # drawing program. do not modify
    t.left(360/sides + 1) #turning the turtle so it will draw a shape. do not modify
    
    
