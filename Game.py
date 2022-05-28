from curses import KEY_UP
from curses import KEY_DOWN
from curses import KEY_RIGHT
from curses import KEY_LEFT

from setuptools import Command
import pygame
pygame.init()

X=400
Y=300
xE=0
yE=0
velE=5
Velocity=15
cloud=pygame.image.load('Sprites\BloodCloud.png')
scary=pygame.image.load('Sprites\ScaryFace.png')
FirstWindow = pygame.display.set_mode((800,600))
pygame.display.set_caption("Test of game made with Python")


OpenedWindow = True

while OpenedWindow:

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            OpenedWindow=False
    Key = pygame.key.get_pressed()
    if Key[pygame.K_UP]:
        Y-=Velocity
        if (Y<=0):
            Y=0
    if Key[pygame.K_DOWN]:
        Y+=Velocity
        if (Y>=550):
            Y=550
    if Key[pygame.K_LEFT]:
        X-=Velocity
        if (X<=0):
            X=0
    if Key[pygame.K_RIGHT]:
        X+=Velocity    
        if (X>=710):
            X=710
    if (X>xE):
        xE+=velE
    if (X<xE):
        xE-=velE
    if (Y>yE):
        yE+=velE
    if (Y<yE):
        yE-=velE
    FirstWindow.fill((0,0,0))
    FirstWindow.blit(cloud,(X,Y))
    FirstWindow.blit(scary,(xE,yE))
    pygame.display.update()

pygame.quit()