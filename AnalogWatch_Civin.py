#Analog watch in Python 3
#by @Cíva
#
import turtle
import time

wn = turtle.Screen()
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.title("Analog Clock by @Cíva")
wn.tracer(0)
wn.update()

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(5)

def draw_hand(pen, angle, length, color):
    pen.penup()
    pen.goto(0, 0)
    pen.color(color)
    pen.setheading(90)
    pen.right(angle)
    pen.pendown()
    pen.forward(length)

def draw_clock(pen, h, m, s):
    # Draw clock face
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("black")
    pen.pendown()
    pen.circle(210)

    # Draw hour marks
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    for i in range(12):
        pen.forward(190)
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.goto(0, 0)
        pen.right(30)

    # Draw hour hand
    hour_angle = (h / 12) * 360 + (m / 60) * 30
    draw_hand(pen, hour_angle, 50, "black")

    # Draw minute hand
    minute_angle = (m / 60) * 360
    draw_hand(pen, minute_angle, 100, "black")

    # Draw second hand
    second_angle = (s / 60) * 360
    draw_hand(pen, second_angle, 150, "red")

while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))

    draw_clock(pen, h, m, s)

    wn.update()
    time.sleep(1)

    pen.clear()

wn.mainloop()
