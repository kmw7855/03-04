import turtle

count = 6

turtle.penup()
turtle.goto(-250,-250)
turtle.pendown()

while(count > 0) :
    turtle.left(90)
    turtle.forward(500)
    turtle.right(180)
    turtle.forward(500)
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.pendown()
    count= count -1

turtle.penup()
turtle.goto(-250,-250)
turtle.pendown()

count = 6

turtle.left(90)

while(count > 0) :
    turtle.right(90)
    turtle.forward(500)
    turtle.right(180)
    turtle.forward(500)
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)
    turtle.pendown()
    count= count -1

turtle.exitonclick()
