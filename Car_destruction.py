#!/usr/bin/python
import pygame
from random import randint
from threading import Thread
import time

#inicializando e variaveis
pygame.init()
largura = 600
altura = 600

t_player = 20
pos_frent = 2

#cores interface
azul_claro = (126, 192, 238, 255)
preto = (0, 0, 0, 255)
branco = (255, 255, 255, 255)
vermelho = (255, 0, 0, 255)
verde = (0, 255, 0, 255)
azul_escuro = (0, 0, 255, 255)

class Player:
    def __init__(self, x, y, cor, nome):
        self.x = x
        self.y = y
        self.cor = cor
        self.nome = nome
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

            pygame.draw.rect(fundo, self.cor, [self.x_ant_1, self.y_ant_1, t_player, t_player])
            pygame.draw.rect(fundo, self.cor, [self.x_ant_2, self.y_ant_2, t_player, t_player])
            pygame.draw.rect(fundo, self.cor, [self.x_ant_3, self.y_ant_3, t_player, t_player])
          
        self.j +=1
        
        a = randint(0,3)
        flag = True
        
        if a == 0:
            if temp_x + t_player > 500 :
                self.mover()
            else:
                temp_temp_x = temp_x + (t_player * pos_frent)
                if fundo.get_at((temp_temp_x, temp_y)) != self.cor and fundo.get_at((temp_temp_x, temp_y)) != branco and fundo.get_at((temp_temp_x, temp_y)) != preto:
                    self.mover()
                elif fundo.get_at((temp_x + t_player, temp_y)) == self.cor or fundo.get_at((temp_x + t_player, temp_y)) == branco:
                    self.x += t_player
                    flag = True
                else:
                    flag = False
                    
        elif a == 1:
            if temp_x - t_player < 140 :
                self.mover()
            else:
                temp_temp_x = temp_x - (t_player * pos_frent)
                if fundo.get_at((temp_temp_x, temp_y)) != self.cor and fundo.get_at((temp_temp_x, temp_y)) != branco and fundo.get_at((temp_temp_x, temp_y)) != preto:
                    self.mover()
                elif fundo.get_at((temp_x - t_player, temp_y)) == self.cor or fundo.get_at((temp_x - t_player, temp_y)) == branco:
                    self.x -= t_player
                    flag = True
                else:
                    flag = False

        elif a == 2:
            if temp_y + t_player > 460:
                self.mover()
            else:
                temp_temp_y = temp_y + (t_player * pos_frent)
                if fundo.get_at((temp_x, temp_temp_y)) != self.cor and fundo.get_at((temp_x, temp_temp_y)) != branco and fundo.get_at((temp_x, temp_temp_y)) != preto:
                    self.mover()
                if fundo.get_at((temp_x, temp_y + t_player)) == self.cor or fundo.get_at((temp_x, temp_y + t_player)) == branco:
                    self.y += t_player
                    flag = True
                else:
                    flag = False

        elif a == 3:
            if temp_y - t_player < 180:
                self.mover()
            else:
                temp_temp_y = temp_y - (t_player * pos_frent)
                if fundo.get_at((temp_x, temp_temp_y)) != self.cor and fundo.get_at((temp_x, temp_temp_y)) != branco and fundo.get_at((temp_x, temp_temp_y)) != preto:
                    self.mover()
                if fundo.get_at((temp_x, temp_y - t_player)) == self.cor or fundo.get_at((temp_x, temp_y - t_player)) == branco:
                    self.y -= t_player
                    flag = True
                else:
                    flag = False

        if flag:
            pygame.draw.rect(fundo, self.cor, [self.x, self.y, t_player, t_player])
            return flag
        else:
            pygame.draw.rect(fundo, branco, [self.x_ant_1, self.y_ant_1, t_player, t_player])
            pygame.draw.rect(fundo, branco, [self.x_ant_2, self.y_ant_2, t_player, t_player])
            pygame.draw.rect(fundo, branco, [self.x_ant_3, self.y_ant_3, t_player, t_player])
            pygame.draw.rect(fundo, branco, [self.x, self.y, t_player, t_player])
            return flag


ps = []
#player 1
p1 = Player(500, 460, vermelho, "Vermelho")
ps.append(p1)
#player 2
p2 = Player(140, 180, azul_claro, "Azul")
ps.append(p2)
#player 3
p3 = Player(420, 260, verde, "Verde")
ps.append(p3)
#player 4
p4 = Player(340, 460, azul_escuro, "Azul Escuro")
ps.append(p4)

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

#Programa sempre ficar rodando e desenhando     
cond = True;

while cond:
    #capturar eventos do mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cond = False
    fundo.fill(branco)
    criar_cenario2()

    r = randint(0, len(ps) - 1)
    i = r
    while (i < len(ps)):
        if ps[i].mover() == False:
            ps.remove(ps[i])

        if i + 1 == r:
            i = len(ps)
        if i + 1 == len(ps):
            if (r == 0):
                i += 1
            else:
                i = 0
        else:
            i += 1

    if len(ps) == 1:
        pygame.font.init()
        fonte = pygame.font.get_default_font()
        fonte_ganhador = pygame.font.SysFont(fonte, 80)
        text = fonte_ganhador.render(ps[0].nome, 1 , ps[0].cor)
        fundo.blit(text, (200, 300))
    
    time.sleep(0.01)

    pygame.display.flip()
    pygame.display.update()

pygame.quit();
quit();
