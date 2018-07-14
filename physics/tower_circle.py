from tower_defense.game_object import *
import pygame
from radius import *

class Tower_circle(GameObject):
    def __init__(self,x,y):
        GameObject.__init__(self,x,y)


    def render(self,canvas):
        RED = (255,0,0)
        pygame.draw.circle(canvas, RED, (self.x, self.y), radius, 1)