import turtle
import random
from time import sleep

janela = turtle.Screen()
janela.setup(700, 500)
janela.bgcolor('gray')
janela.title('Corrida de Tartarugas !!!')

def linha_chegada():
    
  xd = turtle.Turtle()
  xd.shape('circle')
  xd.color('red')
  xd.hideturtle()
  xd.pensize(4)
  xd.penup()
  xd.goto(320,-240)
  xd.left(90)
  xd.pendown()
  xd.setposition(320,300)

nomes = ["josycreide", "snoop", "snake", "python", "wolf"]
cores = ["red", "blue", "yellow", "pink", "White"]
posicoes = [(-300, 10), (-300, 100), (-300, 200), (-300, -100), (-300, -200)]

corredores = dict()


linha_chegada()

for nome, cor,posicoes in zip(nomes, cores, posicoes):

  corredores[nome] = turtle.Turtle()
  corredores[nome].hideturtle()
  corredores[nome].shape("turtle")
  corredores[nome].penup()
  corredores[nome].color(cor)
  corredores[nome].setpos(posicoes)
  corredores[nome].showturtle()
  corredores[nome].right(360)
  corredores[nome].write("Ola, Aposta em mim")
    
vencedor = ""

while not vencedor:
    for nome in nomes:
        distancia = random.randint(1, 5)
        corredores[nome].forward(distancia)
        if corredores[nome].pos()[0] > 300:
            vencedor = nome
            break
            print(f' {vencedor} Foi a Vencedor(a) !!!')

dd = turtle.Turtle()
dd.shape('turtle')
dd.color('black')
dd.penup()
sleep(2.0)
mensagem = "A tartaruga vencedora foi = {}".format(vencedor)
fonte = ("arial", 20)

dd.write(mensagem, True, "center", fonte)
dd.right(360)

janela.mainloop()
