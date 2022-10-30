from turtle import *

speed("fast")
hideturtle()
title("u are so precious to me :)")

pensize(2)
left(90)

def layer(layerColor, radius, startingX, doubledX):
  begin_fill()
  color(layerColor)
  forward(startingX)
  for i in range(8):
    circle(radius, 200)
    forward(doubledX)
  circle(radius, 200)
  forward(startingX)
  end_fill()

layer("#ffa6c1", -35, 200, 400)
layer("#ffacc5", 35, 200, 400)
layer("#ff87ab", -26, 150, 300)
layer("#ff97b7", 26, 150, 300)
layer("#ff5d8f", -18, 100, 200)
layer("#ff5d8f", 18, 100, 200)

setpos(0, -20)
color("black")
write("hi carlie\nily! :D", False, align="center", font=("Arial", 16, "normal"))
done()