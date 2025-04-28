import turtle
turtle.Screen() .bgcolor ("white") 
board = turtle.Turtle()
size = 0
speed = 999999999999999999999999
board.speed (speed)
while True:
    
    for i in range (4):
        board.fd (size - 1)
        board.left (90)
        size = size + 5
       
    size = size - 1
   
    