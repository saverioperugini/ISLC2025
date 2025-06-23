import turtle

i = 0

def tree(branch_len, t, w=None):
    global i
    i = i + 1
    if i == 7:  # book
        # if i == 5:  # site
        w.getcanvas().postscript(file=f"tree1.ps")
    # if i == 2 ** 7:  # book
    if i == 2 ** 5:  # site
        w.getcanvas().postscript(file=f"tree2.ps")
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t, w)
        t.left(40)
        tree(branch_len - 15, t, w)
        t.right(20)
        t.backward(branch_len)

def draw_tree():
    # turtle.setup(600, 600)  # book
    turtle.setup(300, 300)  # site
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.ht()
    t.left(90)
    t.up()
    # t.backward(200)  # book
    t.backward(100)  # site
    t.down()
    # t.color("black")  # book
    t.color("green")  # site
    # tree(110, t, my_win)  # book
    tree(75, t, my_win)  # site
    my_win.exitonclick()

draw_tree()
