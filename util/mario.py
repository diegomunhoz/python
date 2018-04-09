#-*-coding:latin1-*-
import pygame
from pygame.locals import Rect, QUIT, KEYDOWN,KEYUP,K_LEFT,K_RIGHT,K_UP,K_DOWN
pygame.init();
countFrames = 0;
def pintar(scr,estados,personagem):
	listaFramesPintaveis = estados[personagem["estado"]];
	i = personagem["numFrame"];
	if(i >= len(listaFramesPintaveis)):
		i = 0;
	
	numQuadro = listaFramesPintaveis[i];
	frame = personagem["frames"][numQuadro];
	scr.blit(frame,personagem["pos"]);
	i+=1;
	personagem["numFrame"] = i;
	
screen = pygame.display.set_mode((800,600),0,32);
mario = pygame.image.load("C:/Temp/mario.png").convert_alpha();
frames = [];
clk = pygame.time.Clock();
for linha in range(2):
	for coluna in range(4):
		x = coluna * 40;
		y = linha * 40;
		frames.append(pygame.transform.scale(mario.subsurface(Rect((x,y),(40,40))),(100,100)));
		
for linha in range(2):
	for coluna in range(4):
		x = coluna * 40;
		y = linha * 40;
		frames.append( pygame.transform.flip(pygame.transform.scale(mario.subsurface(Rect((x,y),(40,40))),(100,100)), True, False) );		
i = 0;
incr = 1;
estados = {"parado":[0],"andando":[1,2,3],"correndo":[4,5,6,7,6,5,4]};
marioPlayer = {"frames":frames,"pos":(100,100),"estado":"parado","numFrame":0};

while(True):
	screen.fill((0,0,0));
	if(countFrames):
		pintar(screen,estados,marioPlayer);
		
	countFrames+=1;
	pygame.display.update();
	clk.tick(40);
	for e in pygame.event.get():
		if(e.type==QUIT):
			exit();
		if(e.type==KEYDOWN):
			if(e.key==K_RIGHT):
				marioPlayer["estado"]="correndo";
			if(e.key==K_LEFT):
				marioPlayer["estado"]="parado";
			if(e.key==K_UP):
				marioPlayer["estado"]="andando";