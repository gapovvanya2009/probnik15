from turtle import *
screensize(1000, 1000)
tracer(20)
left(90)
down()
k = 20
right(315)
for i in range(9):
    forward(22 * k)
    right(90)
    forward(6 * k)
    right(90)
up()
right(90)
forward(5 * k)
left(90)
down()
for i in range(9):
    forward(53 * k)
    right(90)
    forward(75 * k)
    right(90)
up()
for y in range(-30, 30):
    for x in range(-30, 30):
        goto(x * k, y * k)
        dot(3, 'red')
done()