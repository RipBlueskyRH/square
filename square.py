import turtle
turtle.Screen().bgcolor("cyan")
turtle.Screen().setup(500,500)
side=4
angle=360/side
square=turtle.Turtle()
square.color("orange")
for i in range(side):
    square.forward(94)
    square.right(angle)
turtle.done()