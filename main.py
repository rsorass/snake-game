from turtle import *
import time
import random

lblock = 100
ablock = 100
tpasso = 100

screen = Screen()
screen.bgcolor("#96FF6D")

maca = Turtle()
maca.color("#000000")
maca.fillcolor("#FF0000")
maca.begin_fill()
maca.shape("circle")
maca.shapesize(2)
maca.penup()
maca.teleport(random.randint(-400,400), random.randint(-400,400))

cobra = Turtle()
cobra.color("#000000")
cobra.fillcolor("#0F78DA")
cobra.begin_fill()
cobra.shapesize(2.5)
cobra.shape("square")
cobra.penup()

tamanho_corpo = [cobra]

def andar():
    cobra.fd(tpasso)

direcao = "r"
def r():
    global direcao
    if direcao != "l":
        direcao = "r"
        print("Indo para a direita.")
def l():
    global direcao
    if direcao != "r":
        direcao = "l"
        print("Indo para a esquerda.")
def up():
    global direcao
    if direcao != "dwn":
        direcao = "up"
        print("Indo para cima.")
def dwn():
    global direcao
    if direcao != "up":
        direcao = "dwn"
        print("Indo para baixo.")

def comer():
    if cobra.distance(maca) < 20:
        novo_corpo = Turtle()
        novo_corpo.shape("square")
        novo_corpo.color("#0F78DA")
        novo_corpo.shapesize(2.5)
        novo_corpo.penup()
        tamanho_corpo.append(novo_corpo)
        novo_corpo.goto(1000,1000)
        maca.teleport(random.randint(-400,400), random.randint(-400,400))

onkey(r, "Right")
screen.listen()
onkey(up, "Up")
screen.listen()
onkey(l, "Left")
screen.listen()
onkey(dwn, "Down")
screen.listen()

while 1 < 2:
    for i in range(len(tamanho_corpo)-1, 0, -1):
        tamanho_corpo[i].goto(tamanho_corpo[i - 1].position())

    comer()

    if direcao == "r":
        cobra.setheading(0)
        andar()
    if direcao == "up":
        cobra.setheading(90)
        andar()
    if direcao == "l":
        cobra.setheading(180)
        andar()
    if direcao == "dwn":
        cobra.setheading(270)
        andar()
    time.sleep(0.20)
screen.listen()

done()