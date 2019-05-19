#!/usr/bin/python
import pygame
from random import randint
import time

#cores interface
Azul = (99,184,255);
Azulclaro = (126,192,238);
preto = (0,0,0);
branco = (255,255,255)
vermelho = (255,0,0)
#inicializando e variaveis
pygame.init();
largura = 600;
altura = 600;
j = 1
#player 1
pos_x_player_1 = 140;
pos_y_player_1 = 180
pos_x_player_1_anterior = 140
pos_y_player_1_anterior = 180
tamanho = 10;
#player 2
pos_x_player_2 = 500;
pos_y_player_2 = 460;
tamanho = 10;
pos_x_player_2_anterior = 480
pos_y_player_2_anterior = 440
#criação da tela
fundo = pygame.display.set_mode((largura, altura));
#nome da tela e icone
pygame.display.set_caption("Car destruction");

img = pygame.image.load("C:\Eu\Ia/img.png")
img2 = pygame.image.load("C:\Eu\Ia/pacman.png")
img3 = pygame.image.load("C:\Eu\Ia/pacmanv.png")

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
##    
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

     
    
    
    
    

    
    if j > 1:
      pos_x_player_1_anterior = pos_x_player_1
      pos_y_player_1_anterior = pos_y_player_1

      pos_x_player_2_anterior = pos_x_player_2
      pos_y_player_2_anterior = pos_y_player_2
      pygame.draw.rect(fundo, Azulclaro, [pos_x_player_1,pos_y_player_1,15,15])
      
    j +=1
    
    h = mov_random(pos_x_player_1, pos_y_player_1)
    l = mov_random(pos_x_player_2, pos_y_player_2)


   
    
    if h == "x+40":
        pos_x_player_1 += 40
    if h == "x-40":
        pos_x_player_1 -= 40
    if h == "y+40":
        pos_y_player_1 += 40
    if h == "y-40":
        pos_y_player_1 -= 40

    if l == "x+40":
        pos_x_player_2 += 40
    if l == "x-40":
        pos_x_player_2 -= 40
    if l == "y+40":
        pos_y_player_2 += 40
    if l == "y-40":
        pos_y_player_2 -= 40

    fundo.blit(img2,(pos_x_player_1,pos_y_player_1))
    fundo.blit(img3,(pos_x_player_2,pos_y_player_2))
##    pygame.draw.rect(fundo, vermelho , [pos_x_player_2,pos_y_player_2,15,15])
     
    

    
    
    print(randint(0,3))
    time.sleep(0.5)
    pygame.display.flip()
    pygame.display.update()









pygame.quit();
quit();
