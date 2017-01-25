# ColorMeSpiralled.py 

import turtle   # set up turtle graphics
t=turtle.Pen()
t.speed(0)
turtle.bgcolor('yellow')
# Set up a list of any 10 valid Python color names
colors=['red', 'yellow', 'blue', 'green', 'orange',
        'purple', 'white', 'gray', 'brown', 'sea green']

# ask the user's name using turtle's textinput popup window
your_name = turtle.textinput("Enter your name", "What is your name?")
color = turtle.textinput("Color choice", "Which colors do you want?")

# ask the number of sides
sides = int(turtle.numinput("Number of sides",
                            "How many sides do you want (1-10)?", 5, 1, 10))
font = turtle.textinput("Font",
                            "What font do you want?")
loop = int(turtle.textinput("Times of name",
                            "How many times do you want your name to be printed?"))
        
# draw a spiral of the name on the screen, written 100 times
for x in range(loop):
    t.pencolor(color) # rotate through the 10 colors
    t.penup()       # don't draw the regular spiral lines
    t.forward(x*4)  # just move the turtle on the screen
    t.pendown()     # now, write the user's name, bigger each time
    t.write(your_name, font=("Times", int( (x*2 + 4) / 4), font) )
    t.left(360/sides+2)      # turn left 360/sides+2 degrees for sides

