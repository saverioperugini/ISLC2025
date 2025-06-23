import turtle as t

#head

t.circle(50)

#neck

t.right(90)

t.forward(50)

#left arm

t.right(135)

t.forward(100)

t.right(180)

t.forward(100)

#right arm

t.left(90)

t.forward(100)

#flag

t.left(45)

t.forward(250)

t.right(90)

t.fillcolor("green")

t.begin_fill()

t.forward(200)

t.right(90)

t.forward(150)

t.right(90)

t.forward(200)

t.right(90)

t.forward(150)

t.end_fill()

t.right(90)

t.penup()

t.forward(100)

t.right(90)

t.forward(20)

t.pendown()

t.fillcolor("yellow")

t.begin_fill()

t.left(60)

t.forward(110)

t.right(120)

t.forward(110)

t.right(60)

t.forward(110)

t.right(120)

t.forward(110)

t.end_fill()

t.penup()

t.right(120)

t.forward(90)

t.left(90)

t.pendown()

t.fillcolor("blue")

t.begin_fill()

t.circle(30)

t.end_fill()

t.penup()

t.goto(0,-50)

t.pendown()

t.fillcolor("black")

#torso

t.right(90)

t.forward(100)

#left leg

t.right(45)

t.forward(100)

t.right(180)

t.forward(100)

#right leg

t.right(90)

t.forward(100)

#done

t.done()
