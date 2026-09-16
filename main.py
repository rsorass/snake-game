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
maca.shapesize(3)
maca.penup()
maca.teleport(random.randint(-400,400), random.randint(-300,300))

cobra = Turtle()
cobra.color("#000000")
cobra.fillcolor("#0F78DA")
cobra.begin_fill()
cobra.shapesize(4.5)
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
    if cobra.distance(maca) < 80:
        novo_corpo = Turtle()
        novo_corpo.shape("square")
        novo_corpo.color("#000000")
        novo_corpo.fillcolor("#0F78DA")
        novo_corpo.begin_fill()
        novo_corpo.shapesize(4.5)
        novo_corpo.penup()
        ultimo_corpo_pos = tamanho_corpo[-1].pos()
        tamanho_corpo.append(novo_corpo)
        ## * DESEMPACOTA VALORES GUARDADOS EM TUPLAS ##
        novo_corpo.teleport(*ultimo_corpo_pos)
        maca.teleport(random.randint(-400,400), random.randint(-300,300))

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