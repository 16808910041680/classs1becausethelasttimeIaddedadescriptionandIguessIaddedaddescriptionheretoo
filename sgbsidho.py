import turtle
turtle.Screen() .bgcolor ("white") 
turtle.Screen () .setup(width = 300, height = 400) 
board = turtle.Turtle()
board.color ("black")
board.fillcolor ("blue")


board.forward (100)
board.left (120)
board.forward (100)
board.left (120)
board.forward (100)

board.penup ()

board.right (150)
board.forward (50)

board.pendown ()
board.right (90)
board.forward (100)
board.right (120)
board.forward (100)
board.right (120)
board.forward (90)

turtle.done()