# -*- coding: utf-8 -*-
"""
PETIOT Arthur
DREVET Carl
"""
import pygame
from math import *
from pygame.locals import *
from Tank import *

pygame.init()
fenetre = pygame.display.set_mode((750,750))
pygame.display.set_caption(titreFenetre)
icone = pygame.image.load(imageIcone)
pygame.display.set_icon(icone)

fond = pygame.image.load(imageFond)
fenetre.blit(fond, (0,0))


tank1 = Tank(pygame.Rect(100,100,0,0), 90, imageTank1 , speed)
fenetre.blit(tank1.image, tank1.position)

tank2 = Tank(pygame.Rect(200,200,0,0), 90 , imageTank2, speed)
fenetre.blit(tank2.image, tank2.position)

pygame.display.flip()

pygame.key.set_repeat(400, 50)

continuer = True

estActif = {K_ESCAPE: False, K_DOWN: False, K_RIGHT: False, K_LEFT: False, K_UP: False, K_s:False, K_w:False, K_a:False, K_d:False}

while continuer:
    for event in pygame.event.get():
        
        if event.type == KEYDOWN:
            estActif[event.key] = True
        elif event.type == KEYUP:
            estActif[event.key] = False
        
        
        if estActif[K_ESCAPE]:
            continuer = False
        
        
		
	#faire reculer le tank
        if estActif[K_DOWN]:
            tank1.reculer()
        if estActif[K_s]:
            tank2.reculer()
        #faire avancer le tank    
        if estActif[K_UP]:
            tank1.avancer()
        if estActif[K_w]:
            tank2.avancer()
		
	#rotation du tank a droite
        if estActif[K_RIGHT]:
            tank1.tourner(-22.5)
        if estActif[K_d]:
            tank2.tourner(-22.5)
        #rotation du tank a gauche
        if estActif[K_LEFT]:
            tank1.tourner(22.5)
        if estActif[K_a]:
            tank2.tourner(22.5)


    fenetre.blit(fond, (0,0))
    fenetre.blit(tank1.imageTournee, tank1.position)
    fenetre.blit(tank2.imageTournee, tank2.position)
    pygame.display.flip()
