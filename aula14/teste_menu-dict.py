import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

def colidiu_ponto_rectangulo(pos, rect):
    xMouse = pos[0]
    yMouse = pos[1]
    if xMouse > rect.x and xMouse < (rect.x + rect.w) \
            and yMouse > rect.y and yMouse < (rect.y + rect.h):
        return True
    else:
        return False



pygame.init()

screen = pygame.display.set_mode((650, 450), 0, 32)
font = pygame.font.Font("c:/Windows/Fonts/SHOWG.TTF", 48)

def gerar_detalhes( d ):
    global font
    d["imagem"] = font.render(d["texto"], True, d["cor"])
    d["rect"] = d["imagem"].get_rect()
    d["rect"].x = d["pos"][0]
    d["rect"].y = d["pos"][1]

botoes = []
# botoes.append({"imagem": pygame.image.load("c:/temp/img.png"),"texto": "Jogar", "pos": (200, 100), "cor": (255, 255, 0)})
botoes.append({"texto": "Jogar", "pos": (200, 100), "cor": (255, 255, 0)})
botoes.append({"texto": "Configurar", "pos": (200, 200), "cor": (255, 255, 0)})
botoes.append({"texto": "Sair", "pos": (200, 300), "cor": (255, 255, 0)})
for b in botoes:
    gerar_detalhes(b)

while True:
    screen.fill((0, 0, 0))
    for b in botoes:
        screen.blit(b["imagem"], b["pos"])

    pygame.display.update()
    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == MOUSEBUTTONDOWN:
            for b in botoes:
                if colidiu_ponto_rectangulo(e.pos, b["rect"]):
                    print (b["texto"])