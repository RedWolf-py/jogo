import turtle
from random import randint


janela = turtle.Screen()
janela.setup(600, 500)
janela.bgcolor('green')
janela.title('Corrida de Tartarugas !!!')

def linha():

    xd = turtle.Turtle()
    xd.hideturtle()
    xd.shape('circle')
    xd.color('red')
    xd.pensize(4)
    xd.penup()
    xd.goto(280,-230)
    xd.left(90)
    xd.pendown()
    xd.setposition(280,250)


dd = turtle.Turtle()
dd.hideturtle()
dd.shape('turtle')
dd.color('yellow')
dd.penup()
dd.goto(-250, -50)
dd.showturtle()
dd.pendown()

vc = turtle.Turtle()
vc.hideturtle()
vc.shape('turtle')
vc.color('blue')
vc.penup()
vc.goto(-250, 50)
vc.showturtle()
vc.pendown()


dv = turtle.Turtle()
dv.hideturtle()
dv.shape('turtle')
dv.color('red')
dv.penup()
dv.goto(-250, 150)
dv.showturtle()
dv.pendown()



ff = turtle.Turtle()
ff.hideturtle()
ff.shape('turtle')
ff.color('cyan')
ff.penup()
ff.goto(-250, -150)
ff.showturtle()
ff.pendown()

linha()

while True:

	if ff.xcor() >= 257 or vc.xcor() >= 257 or dv.xcor() >= 257 or dd.xcor() >= 257:

		break

	ff.fd(1*(randint(0, 5)))
	vc.fd(1*(randint(0, 5)))
	dv.fd(1*(randint(0, 5)))
	dd.fd(1*(randint(0, 5)))

print(vc.xcor(),ff.xcor(),dv.xcor(),dd.xcor())

