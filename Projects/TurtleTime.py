import turtle

## Ezii the turtle draws for us!


## name the turtle
ezii = turtle.Turtle()

## draw a square
ezii.forward(100)
ezii.right(90)
ezii.forward(100)
ezii.right(90)
ezii.forward(100)
ezii.right(90)
ezii.forward(100)


## lift arm and move to new position
ezii.penup()
ezii.forward(150)


## lower arm and draw a rectangle
ezii.pendown()
ezii.forward(200)
ezii.right(90)
ezii.forward(100)
ezii.right(90)
ezii.forward(200)
ezii.right(90)
ezii.forward(100)


## lift arm and move to new position
ezii.penup()
ezii.forward(300)


## lower arm and draw an octogon
ezii.pendown()
ezii.forward(75)
ezii.right(45)
ezii.forward(75)
ezii.right(45)
ezii.forward(75)
ezii.right(45)
ezii.forward(75)
ezii.right(45)
ezii.forward(75)
ezii.right(45)
ezii.forward(75)
ezii.right(45)
ezii.forward(75)
ezii.right(45)
ezii.forward(75)


## lift arm and move to new position
ezii.penup()
ezii.right(45)
ezii.right(90)
ezii.right(90)
ezii.right(90)
ezii.forward(100)


## lower arm and draw three individual circles in a row
ezii.pendown()
ezii.circle(25)
ezii.penup()
ezii.forward(75)
ezii.pendown()
ezii.circle(25)
ezii.penup()
ezii.forward(75)
ezii.pendown()
ezii.circle(25)


## raise arm and move to new position
ezii.penup()
ezii.forward(100)


## lower arm and draw an E
ezii.pendown()
ezii.forward(160)
ezii.right(90)
ezii.right(90)
ezii.right(90)
ezii.forward(160)

ezii.penup()
ezii.right(90)
ezii.right(90)
ezii.right(90)
ezii.forward(80)
ezii.right(90)
ezii.right(90)
ezii.right(90)

ezii.pendown()
ezii.forward(160)

ezii.penup()
ezii.right(90)
ezii.forward(80)
ezii.right(90)

ezii.pendown()
ezii.forward(160)


## raise arm and move to new position
ezii.penup()
ezii.forward(50)


## lower arm and draw a Z
ezii.pendown()
ezii.forward(160)
ezii.right(90)
ezii.right(45)
ezii.forward(226)
ezii.right(45)
ezii.right(90)
ezii.right(90)
ezii.forward(160)


## raise arm and move to new position
ezii.penup()
ezii.forward(80)


## lower arm and draw an I
ezii.pendown()
ezii.right(90)
ezii.right(90)
ezii.right(90)
ezii.forward(160)


## raise arm and move to new position
ezii.penup()
ezii.right(90)
ezii.forward(100)


## lower arm and draw an I
ezii.pendown()
ezii.right(90)
ezii.forward(160)


turtle.done()
