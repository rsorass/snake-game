from turtle import *

# janela = Screen()
# janela.listen()

# bgcolor("#BBFF7C")

# cobra = Turtle()
# cobra.color("#000000")
# cobra.fillcolor("#2B80FF")
# cobra.shapesize(3)
# cobra.forward(30)
screen = Screen()
screen.bgcolor("#96FF6D")

cobra = Turtle()
cobra.color("#000000")
cobra.fillcolor("#0F78DA")
cobra.begin_fill()
cobra.shapesize(1.5)

direcao = "r"
def r():
    global direcao
    if direcao != "l":
        direcao = "r"
def l():
    global direcao
    if direcao != "r":
        direcao = "l"
def up():
    global direcao
    if direcao != "dwn":
        direcao = "up"
def dwn():
    global direcao
    if direcao != "up":
        direcao = "dwn"

onkey(r, "Right")
screen.listen()
onkey(up, "Up")
screen.listen()
onkey(l, "Left")
screen.listen()
onkey(dwn, "Down")
screen.listen()

while 1 < 2:
    cobra.fd(3)
    if direcao == "r":
        cobra.setheading(0)
    if direcao == "up":
        cobra.setheading(90)
    if direcao == "l":
        cobra.setheading(180)
    if direcao == "dwn":
        cobra.setheading(270)
screen.listen()

done()