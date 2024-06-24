from turtle import *
color('red')
begin_fill()
left(50)
forward(100)
circle(40, 180)     
left(260)
circle(40, 180) 
forward(100)
end_fill()
done()

# This is another system create a heart.
import turtle
def done():
    turtle.color('red')
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(100)
    turtle.circle(40, 180)
    turtle.left(260)
    turtle.circle(40, 180)
    turtle.forward(100)
    turtle.end_fill()
done()
turtle.done()

# This is also another system is creating heart.
import turtle
turtle.Screen().bgcolor("black")
t = turtle.Turtle()
def draw_heart():
    t.color("red")
    t.begin_fill()
    t.left(50)
    t.forward(100)
    t.circle(40, 180)
    t.left(260)
    t.circle(40, 180)
    t.forward(100)
    t.end_fill()
draw_heart()
turtle.done()