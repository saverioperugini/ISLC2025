import turtle
import math

def bonhomme(tortue):

    #head

       #shape

    circumference = 2 * math.pi * 25

    n = 50

    length = circumference / n

    angle = 360 / n

    for i in range (n):

        tortue.fd(length)

        tortue.lt(angle)

       #eyes

    turtle.penup()

    turtle.pensize(8)

    turtle.goto(-10,25)

    turtle.pendown()

    turtle.goto(-10,24)

    turtle.penup()

    turtle.goto(10,25)

    turtle.pendown()

    turtle.goto(10,24)

       #hat

    """

    turtle.pensize(10)

    turtle.pencolor("brown")

    turtle.penup()

    turtle.goto(-40,n-10)

    turtle.pendown()

    turtle.goto(-15,n-10)

    turtle.pensize(28)

    turtle.penup()

    turtle.goto(-12,n+3)

    turtle.pendown()

    turtle.goto(12,n+3)

    turtle.pensize(10)

    turtle.penup()

    turtle.goto(-15,n-10)

    turtle.pendown()

    turtle.goto(40,n-10)

    """

       #bérêt

    turtle.pensize(20)

    turtle.penup()

    turtle.goto(-14,n+3)

    turtle.pendown()

    turtle.goto(20,n-3)

    turtle.penup()

    turtle.pensize(3)

    turtle.goto(3,60)

    turtle.pendown()

    turtle.goto(3,65)

 

    #body

        #shape

    turtle.pensize(2)

    turtle.pencolor("black")

    tortue.rt(90)

    tortue.fd(10)

    tortue.goto(25,-10)

    tortue.goto(25,-110)

    tortue.goto(-25,-110)

    tortue.goto(-25,-10)

    tortue.lt(90)

    tortue.fd(25)

        #stripes

    turtle.pencolor("blue")

    x,y=-25,-10

    for i in range (20):

        turtle.penup()

        turtle.goto(x,y)

        turtle.pendown()

        turtle.goto(x+50,y)

        y-=5

    turtle.pencolor("black")  

    #legs

       #left

    turtle.penup()

    turtle.pensize(5)

    turtle.goto(-10,-110)

    turtle.pendown()

    turtle.goto(-10,-200)

    turtle.goto(-15,-200)

       #right

    turtle.penup()

    turtle.goto(10,-110)

    turtle.pendown()

    turtle.goto(10,-200)

    turtle.goto(15,-200)

    #arms

       #left

    turtle.penup()

    turtle.pensize(3)

    turtle.goto(-25,-15)

    turtle.pendown()

    turtle.goto(-90,20)

       #right

    turtle.penup()

    turtle.pensize(3)

    turtle.goto(25,-15)

    turtle.pendown()

    turtle.goto(90,20)

       #wine

    turtle.penup()

    turtle.pensize(5)

    turtle.goto(90,35)

    turtle.pendown()

    turtle.goto(90,15)

    turtle.pencolor("purple")

    turtle.pensize(18)

    turtle.goto(90,-35)

       #baguette

    turtle.pencolor("yellow")

    turtle.penup()

    turtle.pensize(13)

    turtle.goto(-70,70)

    turtle.pendown()

    turtle.goto(-110,-30)

    #go back to start (finish the bowtie)

    turtle.penup()

    turtle.goto(0,-10)

    turtle.pendown()

    turtle.lt(180)

tortue = turtle.Turtle()

ecran = turtle.Screen()        

bonhomme(tortue)

ecran.exitonclick()
