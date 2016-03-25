import pygame
from math import *
from pygame.locals import *

class Tank:
    def __init__(self, position, angle, lienImage, vitesse) :
        self.image = pygame.image.load(lienImage).convert_alpha()
        self.imageTournee = self.image
        self.angle = angle
        self.position = position
        self.vitesse = vitesse
		
    def reculer(self) :
        self.position= self.position.move(-self.vitesse*cos(self.angle*3.14/180),self.vitesse*sin(self.angle*3.14/180))
		
    def avancer(self):
        self.position = self.position.move(self.vitesse*cos(self.angle*3.14/180),-self.vitesse*sin(self.angle*3.14/180))
		
    def tournerADroite(self, angle):
        self.angle += angle
        self.imageTournee=pygame.transform.rotate(self.image,self.angle-90)
		
