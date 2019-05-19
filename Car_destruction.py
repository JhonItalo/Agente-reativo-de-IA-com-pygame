#!/usr/bin/python
import pygame
from random import randint
import time

#inicializando e variaveis
pygame.init()
largura = 600
altura = 600

#cores interface
azul = (99, 184, 255)
azul_claro = (126, 192, 238)
preto = (0, 0, 0);
branco = (255, 255, 255)
vermelho = (255, 0, 0)

class Player:
    def __init__(self, x, y, cor, cor_parede):
        self.x = x
        self.y = y
        self.cor = cor
        self.cor_parede = cor_parede
        self.j = 1
        self.x_ant_1 = x
        self.y_ant_1 = y
        self.x_ant_2 = x
        self.y_ant_2 = y
        self.x_ant_3 = x
        self.y_ant_3 = y

    def mover(self):
        temp_x = int(self.x)
        temp_y = int(self.y)
        
        #limites (140,180) / (140,460) / (500,460) / (500,180)
        #x entre 140 e 500 y entre 180 e 460

        if self.j > 1:
            self.x_ant_1 = self.x_ant_2
            self.y_ant_1 = self.y_ant_2
            self.x_ant_2 = self.x_ant_3
            self.y_ant_2 = self.y_ant_3
            self.x_ant_3 = self.x
            self.y_ant_3 = self.y

            pygame.draw.rect(fundo, self.cor_parede, [self.x_ant_1, self.y_ant_1, 15, 15])
            pygame.draw.rect(fundo, self.cor_parede, [self.x_ant_2, self.y_ant_2, 15, 15])
            pygame.draw.rect(fundo, self.cor_parede, [self.x_ant_3, self.y_ant_3, 15, 15])
          
        self.j +=1
        
        a = randint(0,3)
        
        if a == 0:
            if temp_x + 40 > 500 :
                self.mover()
            else:
                self.x += 40
                
        elif a == 1:
            if temp_x - 40 < 140 :
                self.mover()
            else:
                self.x -= 40

        elif a == 2:
            if temp_y + 40 > 460:
                self.mover()
            else:
                self.y += 40

        elif a == 3:
            if temp_y - 40 < 180:
                self.mover()
            else:
                self.y -= 40

        pygame.draw.rect(fundo, self.cor, [self.x, self.y, 15, 15])



#player 1
p1 = Player(140, 180, azul_claro, preto)
#player 2
p2 = Player(500, 460, vermelho, preto)

#criação da tela
fundo = pygame.display.set_mode((largura, altura));
#nome da tela e icone
pygame.display.set_caption("Car destruction");

img = pygame.image.load("img.png")

#criar cenario
def criar_cenario():
    fundo.blit(img,(-200,-50))
    fundo.blit(img,(-80,-50))
    fundo.blit(img,(40,-50))
    fundo.blit(img,(160,-50))

    fundo.blit(img,(-200,70))
    fundo.blit(img,(-80,70))
    fundo.blit(img,(40,70))
    fundo.blit(img,(160,70))

    fundo.blit(img,(-200,190))
    fundo.blit(img,(-80,190))
    fundo.blit(img,(40,190))
    fundo.blit(img,(160,190))

def criar_cenario2():
    pygame.draw.lines(fundo, preto,False, [(120,160),(120,480),(520,480),(520,160),(120,160)], 5)
    #linhas horizontais
##    pygame.draw.lines(fundo,preto,False,[(120,200),(520,200)],5)
##    pygame.draw.lines(fundo,preto,False,[(120,240),(520,240)],5)
##    pygame.draw.lines(fundo,preto,False,[(120,280),(520,280)],5)
##    pygame.draw.lines(fundo,preto,False,[(120,320),(520,320)],5)
##    pygame.draw.lines(fundo,preto,False,[(120,360),(520,360)],5)
##    pygame.draw.lines(fundo,preto,False,[(120,400),(520,400)],5)
##    pygame.draw.lines(fundo,preto,False,[(120,440),(520,440)],5)
   #linhas verticais
##    pygame.draw.lines(fundo,preto,False,[(160,160),(160,480)],5)
##    pygame.draw.lines(fundo,preto,False,[(200,160),(200,480)],5)
##    pygame.draw.lines(fundo,preto,False,[(240,160),(240,480)],5)
##    pygame.draw.lines(fundo,preto,False,[(280,160),(280,480)],5)
##    pygame.draw.lines(fundo,preto,False,[(320,160),(320,480)],5)
##    pygame.draw.lines(fundo,preto,False,[(360,160),(360,480)],5)
##    pygame.draw.lines(fundo,preto,False,[(400,160),(400,480)],5)
##    pygame.draw.lines(fundo,preto,False,[(440,160),(440,480)],5)
##    pygame.draw.lines(fundo,preto,False,[(480,160),(480,480)],5)
    
def mov_random(a, b):
    x = int(a)
    y = int(b)
    #limites (140,180) / (140,460) / (500,460) / (500,180)
    #x entre 140 e 500 y entre 180 e 460
    a = randint(0,3)
    if a == 0:
        if x + 40 > 500 :
            mov_random(a,b)
        else:
            x += 40
            return "x+40"
            
    elif a == 1:
        if x - 40 < 140:
            mov_random(a,b)
        else:
            x -= 40
            return "x-40"

    elif a == 2:
        if y + 40 > 460:
            mov_random(a,b)
        else:
            y += 40
            return "y+40"
            

    elif a == 3:
        if y - 40 < 180:
            mov_random(a,b)
        else:
            y -= 40
            return "y-40"
            
   
    
#Programa sempre ficar rodando e desenhando     
cond = True;
while cond:
    #capturar eventos do mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cond = False;
    fundo.fill(branco)
    criar_cenario2()
    
    p1.mover()
    p2.mover()
    
    print(randint(0,3))
    time.sleep(0.1)

    pygame.display.flip()
    pygame.display.update()

pygame.quit();
quit();
