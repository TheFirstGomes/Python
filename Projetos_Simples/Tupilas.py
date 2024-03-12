import turtle as tl
import colorsys as cs 

tl.setup(800,700)
tl.speed(0)
tl.tracer(15)
tl.width(2)
tl.bgcolor("black")

for j in range(25):
    for i in range(15):
        tl.color(cs.hsv_to_rgb(i/15, j/25, 1))
        tl.right(90)
        tl.circle(200-j*4,90)
        tl.left(90)
        tl.circle(200-j*4,90)
        tl.right(180)
        tl.circle(50,24)
tl.hideturtle()
tl.done()