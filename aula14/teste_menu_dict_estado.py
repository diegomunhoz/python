import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYDOWN, K_ESCAPE


def colidiu_ponto_rectangulo(pos, rect):
    xMouse = pos[0]
    yMouse = pos[1]
    if xMouse > rect.x and xMouse < (rect.x + rect.w) \
            and yMouse > rect.y and yMouse < (rect.y + rect.h):
        return True
    else:
        return False

estado = "menu"

pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32)

font = pygame.font.Font("c:/Windows/Fonts/SHOWG.TTF", 48)


def calcula_se(obj, str_imagem):
    r = obj[str_imagem].get_rect()
    x_se = int(obj["pos"][0] - r.w / 2)
    y_se = int(obj["pos"][1] - r.h / 2)
    return x_se, y_se


def gerar_detalhes( d ):
    global font
    d["imagem"] = font.render(d["texto"], True, d["cor"])
    d["rect"] = d["imagem"].get_rect()
    pos = calcula_se(d, "imagem")
    d["rect"].x = pos[0]
    d["rect"].y = pos[1]
    d["imagem_large"] = pygame.transform.scale(d["imagem"], ( int(d["rect"].w*1.5), int(d["rect"].h*1.5)))

botoes = []
botoes.append({"texto": "Jogar", "pos": (200, 100), "cor": (255, 255, 0)})
botoes.append({"texto": "Configurar", "pos": (200, 200), "cor": (255, 255, 0)})
botoes.append({"texto": "Sair", "pos": (200, 300), "cor": (255, 255, 0)})
for b in botoes:
    gerar_detalhes(b)

while True:
    screen.fill((0, 0, 0))

    if estado == "Jogar":
        pygame.draw.circle(screen, (255, 0, 0), (400, 300), 200, 5)
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    estado = "menu"

    elif estado == "Configurar":
        img_conf = font.render("Configurando", True, (255, 255, 0))
        screen.blit(img_conf, (350, 275))
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    estado = "menu"

    elif estado == "Sair":
        exit()

    else:
        for b in botoes:
            pos = pygame.mouse.get_pos()
            if colidiu_ponto_rectangulo(pos, b["rect"]):
                b["rect"].x, b["rect"].y = calcula_se(b, "imagem_large")
                screen.blit(b["imagem_large"], (b["rect"].x, b["rect"].y))
            else:
                b["rect"].x, b["rect"].y = calcula_se(b, "imagem")
                screen.blit(b["imagem"], (b["rect"].x, b["rect"].y))

        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            elif e.type == MOUSEBUTTONDOWN:
                for b in botoes:
                    if colidiu_ponto_rectangulo(e.pos, b["rect"]):
                        estado = b["texto"]

    pygame.display.update()

