from turtle import *
'''
my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(1200, 800)

# Нарисовать квадрат
def draw_rect(t):
    for x in range(0, 4):
        t.right(90)
        t.forward(100)

# Рисует квадраты в цикле
for x in range(0, 360):
    draw_rect(my_turtle)
    my_turtle.right(1)

# Необходимо, чтобы окно не закрывалось само, а только по клику
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()

'''

t = Turtle()
t.speed(0)
t.screen.setup(800, 600)

# Щеки и рот
t.pensize(5)
t.circle(50, 360)
t.fd(100)
t.pensize(5)
t.circle(50, 360)
t.bk(45)
t.up()
t.goto(50, -25)
t.down()
# Голова
t.pensize(5)
t.circle(130, 360) 
# Нос
t.up()
t.goto(50, 70)
t.down()
t.up()
t.circle(20, 90)
t.down()
t.begin_fill()
t.pensize(5)
t.circle(20, 181)
t.end_fill()
# Глаза
t.up()
t.goto(-35, 130)
t.down()
t.pensize(5)
t.begin_fill()
t.fillcolor("aqua")
t.circle(30, 360)
t.end_fill()
t.up()
t.goto(75, 130)
t.down()
t.pensize(5)
t.begin_fill()
t.fillcolor("aqua")
t.circle(30, 360)
t.end_fill()
#Зрачки
t.up()
t.goto(-20, 130)
t.down()
t.pensize(5)
t.begin_fill()
t.fillcolor("black")
t.circle(15, 360)
t.end_fill()
t.up()
t.goto(90, 130)
t.down()
t.pensize(5)
t.begin_fill()
t.fillcolor("black")
t.circle(15, 360)
t.end_fill()
#Уши
t.left(100)
t.up()
t.goto(-68, 138)
t.down()
t.pensize(5)
for i in range(2):
    t.begin_fill()
    t.fillcolor("grey")
    t.circle(50, 90)
    t.circle(30//4, 90)
    t.end_fill()

t.right(120)
t.up()
t.goto(138, 195)
t.down()
t.pensize(5)
for i in range(2):
    t.begin_fill()
    t.fillcolor("grey")
    t.circle(50, 90)
    t.circle(30//4, 90)
    t.end_fill()

t.screen.exitonclick()
t.screen.mainloop()