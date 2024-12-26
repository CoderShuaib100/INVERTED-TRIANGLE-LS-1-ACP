import turtle
win = turtle.Screen()
win.bgcolor("orange")
win.title("INVERTED TRAINGLE")
win.setup(600,600)

pen = turtle.Turtle()

pen.up()
pen.left(90)
pen.fd(100)
pen.left(90)
pen.fd(200)
pen.down()
pen.right(180)
for i in range (1,4):
    pen.fd(400)
    pen.right(120)   
turtle.done()