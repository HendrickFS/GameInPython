import random
from tokenize import String
import pygame
import numpy
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Snake game with Python")
snkBody = pygame.image.load('Sprites\SnakeBody.png')
snkBg = pygame.image.load('Sprites\SnakeBg.png')
snkGm = pygame.image.load('Sprites\SnakeGameOver.png')
snkFood = pygame.image.load('Sprites\SnakeHead.png')
font = pygame.font.Font('freesansbold.ttf', 11)
text = font.render('<Press Space to play again>', True, (255,0,0))
score = font.render('Score: ', True, (255,0,0))
x=200
y=150
v=5
scr=0
snkH=[x,y]
snk=[]
size=1
dir=1
FlagEat=False
FlagGameOver=False
xF=random.randint(0,350)
yF=random.randint(0,350)
OpenedWindow = True
while OpenedWindow:
    pygame.time.delay(50)
    while FlagEat:
        xF=random.randint(0,350)
        yF=random.randint(0,350)
        for i in snk:
            if (i[0]-xF<=15 and i[0]-xF>=-15) and (i[1]-yF<=15 and i[1]-yF>=-15):
                FlagEatInLoop=True
            else:
                FlagEatInLoop=False
        if FlagEatInLoop:
            FlagEat=True
        else:
            FlagEat=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            OpenedWindow=False
    Key = pygame.key.get_pressed()
    if Key[pygame.K_UP]:
        if (dir==3):
            dir=3
        else:
            dir=4
            change=(x,y)
    if Key[pygame.K_DOWN]:
        if (dir==4):
            dir=4
        else:
            dir=3
            change=(x,y)
    if Key[pygame.K_LEFT]:
        if (dir==2):
            dir=2
        else:
            dir=1
            change=(x,y)
    if Key[pygame.K_RIGHT]:
        if (dir==1):
            dir=1
        else:
            dir=2
            change=(x,y)
    if Key[pygame.K_SPACE]:
        x=200
        y=150
        snkH=[x,y]
        snk=[]
        size=1
        scr=0
        dir=1
        FlagGameOver=False
    if (dir==1):
        x-=v
        if (x<=-10):
            FlagGameOver=True
    if (dir==2):
        x+=v
        if (x>=410):
            FlagGameOver=True
    if (dir==3):
        y+=v
        if (y>=410):
            FlagGameOver=True
    if (dir==4):
        y-=v
        if (y<=-10):
            FlagGameOver=True
    snkH=[x,y]
    snk.append(snkH)
    if len(snk)>size:
        del snk[0]
    if ((x-xF<=15 and x-xF>=-15) and (y-yF<=15 and y-yF>=-15)):
        size+=3
        scr+=1
        FlagEat=True
    if snk.count(snkH)>1:
        FlagGameOver=True
    countScore="Score: "+ str(scr)
    score = font.render(countScore, True, (255,0,0))
    screen.blit(snkBg, (0,0))
    if FlagGameOver==False:
        for i in snk:
            screen.blit(snkBody, (i[0],i[1]))
        screen.blit(snkFood, (xF,yF))
        screen.blit(score, (10,10))
    else:
        screen.blit(snkGm, (150,150))
        screen.blit(text, (120,250))
        screen.blit(score, (10,10))
    pygame.display.update()
pygame.quit()