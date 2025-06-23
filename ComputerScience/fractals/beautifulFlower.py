#*******************************************************************************
#         purpose: Generates a spiral tree using mutual recursion, complete 
#                  with decorative flower petals
# 
# input parameter: depth, an int representing the depth of the recursion
#    return value: None; draws the tree
#******************************************************************************/

import turtle as t

t.speed(0)
t.ht()
t.seth(90)

def teleport(pos: tuple) -> None:

   t.pu()
   t.goto(pos)
   t.pd()

def r_spractal(depth: int, size=30, angle=15) -> None:

   if depth > 0:
      pos = t.pos()
      saved_angle = t.heading()

      for edge in range(0,size):
         t.fd(size)
         t.rt(angle)
         angle += 1
         size -= 1
         l_spractal(depth-1, size-5)

      t.color("pink")
      t.circle(3)
      t.color("black")
      t.seth(saved_angle)
      teleport(pos)  

def l_spractal(depth: int, size=30, angle=15) -> None:

   if depth > 0:
      pos = t.pos()
      saved_angle = t.heading()

      for edge in range(0,size):
         t.fd(size)
         t.lt(angle)
         angle += 1
         size -= 1
         r_spractal(depth-1, size-5)

      t.color("pink")
      t.circle(3)
      t.color("black")

      t.seth(saved_angle)
      teleport(pos)

l_spractal(3)
t.exitonclick()
t.mainloop()
