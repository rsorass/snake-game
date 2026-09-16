from turtle import *
import time
import random

tpasso = 50
placar = Turtle()
placar.penup()
placar.hideturtle()

screen = Screen()
screen.setup(width=900, height=700)
screen.bgcolor("#96FF6D")
screen.tracer(0)

maca = Turtle()
maca.color("#000000")
maca.fillcolor("#FF0000")
maca.begin_fill()
maca.shape("circle")
maca.shapesize(1.5)
maca.penup()
maca.teleport(random.randrange(-350,350, tpasso), random.randrange(-250,250, tpasso))

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

pontos = 0
placar.teleport(-410, 300)
placar.write(f"Pontos: {pontos}", font=('Arial', 16, 'normal'))
def comer():
    global pontos
    if cobra.distance(maca) < 40:
        novo_corpo = Turtle()
        novo_corpo.shape("square")
        novo_corpo.color("#000000")
        novo_corpo.fillcolor("#0F78DA")
        novo_corpo.begin_fill()
        novo_corpo.shapesize(2.5)
        novo_corpo.penup()
        ultimo_corpo_pos = tamanho_corpo[-1].pos()
        tamanho_corpo.append(novo_corpo)
        ## * DESEMPACOTA VALORES GUARDADOS EM TUPLAS ##
        novo_corpo.teleport(*ultimo_corpo_pos)
        maca.teleport(random.randrange(-350,350, tpasso), random.randrange(-250,250, tpasso))
        # novo_corpo.speed(10)
        pontos += 1
        placar.clear()
        placar.write(f"Pontos: {pontos}", font=('Arial', 16, 'normal'))


onkey(r, "Right")
screen.listen()
onkey(up, "Up")
screen.listen()
onkey(l, "Left")
screen.listen()
onkey(dwn, "Down")
screen.listen()

pos_pontos = [(-400, 325)]

bateu_no_corpo = False
caneta = Turtle()
caneta.penup()
caneta.hideturtle()

while 1 < 2:
    antiga_pos_cobra = cobra.pos()
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

    for i in range(len(tamanho_corpo)-1, 1, -1):
        tamanho_corpo[i].goto(tamanho_corpo[i-1].pos())
    if len(tamanho_corpo) > 1:
        tamanho_corpo[1].goto(*antiga_pos_cobra)

    for i in tamanho_corpo[1:]:
        if cobra.pos() == i.pos():
            bateu_no_corpo = True
    if bateu_no_corpo == True:
        break

    if cobra.xcor() > 440 or cobra.xcor() < -440:
        print("Você saiu das bordas do mapa.")
        break
    if cobra.ycor() > 340 or cobra.ycor() < -340:
        print("Você  saiu das bordas do mapa.")
        break

    comer()
    screen.update()
    time.sleep(0.30)
    
screen.listen()

caneta.write("VOCÊ PERDEU! TENTE NOVAMENTE!", align="center", font=('Arial', 24, 'bold'))

done()