import turtle
turtle.Screen() .bgcolor ("white") 
turtle.Screen () .setup(width = 300, height = 400) 
polygon = turtle.Turtle()
polygon.color ("black")

number_of_sides = 180
side_length = 100
angle = 360 / number_of_sides
polygon.begin_fill()
for i in range (number_of_sides):
    polygon.forward (side_length)
    polygon.right (angle)
polygon.end_fill()