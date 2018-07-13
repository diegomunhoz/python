import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32)

font = pygame.font.Font("c:/Windows/Fonts/SHOWG.TTF", 48)

img_texto_jogar = font.render("Jogar", True, (255, 255, 0))
img_texto_configurar = font.render("Configurar", True, (255, 255, 0))

def colidiu_ponto_rectangulo(pos, rect):
    xMouse = pos[0]
    yMouse = pos[1]
    if xMouse > rect.x and xMouse < (rect.x + rect.w) \
            and yMouse > rect.y and yMouse < (rect.y + rect.h):
        return True
    else:
        return False

while True:
    screen.fill((0, 0, 0))
    screen.blit(img_texto_jogar, (200, 100))
    screen.blit(img_texto_configurar, (200, 200))
    pygame.display.update()

    rect_jogar = img_texto_jogar.get_rect()
    rect_jogar.x = 200
    rect_jogar.y = 100

    rect_configurar = img_texto_configurar.get_rect()
    rect_configurar.x = 200
    rect_configurar.y = 200

    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        elif e.type == MOUSEBUTTONDOWN:
            if colidiu_ponto_rectangulo(e.pos, rect_jogar):
                print ("Clicou na opção Jogar")
            elif colidiu_ponto_rectangulo(e.pos, rect_configurar):
                print ("Clicou na opção Configurar")