import turtle

x1 , y1 = eval(input("enter the x1 AND y1 :"))
x2 , y2 = eval(input("enter the x2 AND y2 :"))

distance = ((x1-x2)**2 + (y1-y2)**2)**0.5

#display line
turtle.penup()
turtle.goto(x1 , y1)
turtle.pendown()
turtle.write("point1")
turtle.goto(x2 , y2)
turtle.write("point2")

turtle.penup()
turtle.goto((x1+x2)/2 , (y1+y2)/2)
turtle.write("distance")

turtle.done()
