import turtle


def quadrado(lado):
    """ Desenha um quadrado de lado."""
    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)


def triangulo(lado):
    """ Desenha um triangulo de lado."""
    for i in range(3):
        turtle.forward(lado)
        turtle.left(120)


def pentagono(lado):
    """ Desenha um pentagono de lado."""
    for i in range(5):
        turtle.forward(lado)
        turtle.left(72)


def poligono(lado, num_lados):
    """ Desenha um poligono de num_lados ."""
    for i in range(num_lados):
        turtle.forward(lado)
        turtle.left(360 / num_lados)


def formas(lado, num_lados, angulo):
    """ Desenha sequências de segmentos eventualmente produzindo formas fechadas."""
    for i in range(num_lados):
        turtle.forward(lado)
        turtle.left(angulo)

quadrado(150)
#poligono(10,5)
#formas(100, 5, 144)
#formas(100, 8, 135)
#formas(100, 10, 108)