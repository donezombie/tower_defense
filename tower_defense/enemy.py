import random
from tower_defense.game_object import GameObject
from physics.box_collider import BoxCollider
import tower_defense.game_object
from control_move_enemy import *
from renderers.animation import Animation
from img_animation import  *
from frame_counter import FrameCounter
class Enemy(GameObject) :
    def __init__(self,x,y):
        GameObject. __init__(self,x,y)
        self.box_collider = BoxCollider(50,50)
        self.first_move = False
        self.sec_move = False
        self.renderer = Animation(list_enemy,loop = True,frame_delay=1)
        self.stun = False
        self.stunCooldown = 20


    def update(self):
        GameObject.update(self)
        if self.stun:
            self.stunCooldown -= 1
            if self.stunCooldown == 0:
                self.stun = False
                self.stunCooldown = 20
        if not self.stun:
            self.enemy_move(5)
        self.deactivate_if_need()
        # self.x += self.velocityX
        # self.y += self.velocityY


    def deactivate(self):
        self.is_active = False

    def enemy_move(self,vantoc):
        if self.y < 150 and self.first_move is False :
            self.y += vantoc
        if self.y == 150 and self.first_move is False:
            self.x-= vantoc
        if  self.x ==90 :
            self.first_move = True
            self.y+= vantoc
        if self.y == 360 :
            self.x += vantoc
        if self.x == 520:
            self.y += vantoc
        if self.y == 620:
            self.x -= vantoc

    # def caigiday(self):
    #     self.vectorX = self.x_player - self.x
    #     self.vectorY =  self.y_player - self.y
    #     self.velocityX = self.vectorX/((self.vectorX**2 + self.vectorY**2)**(1/2))*5
    #     self.velocityY = self.vectorY/((self.vectorX**2 + self.vectorY**2)**(1/2))*5
    #     self.x += self.velocityX
    #     self.y += self.velocityY

        tower_defense.game_object.get_position_from_main = (self.x, self.y)  # new
    def deactivate_if_need(self):
        if self.y >=800:
            self.deactivate()
            try:
                tower_defense.game_object.game_objects.remove(self)
            except ValueError:
                pass
            
