import random
from tower_defense.game_object import GameObject
from physics.box_collider import BoxCollider
import tower_defense.game_object
from control_move_enemy import *
from renderers.animation import Animation
from renderers.image_renderer import *
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
        self.isDeath = False


    def update(self):
        GameObject.update(self)
        if self.stun:
            self.renderer = Animation(enemy_stun,loop=True,frame_delay=1)
            self.stunCooldown -= 1
            if self.stunCooldown == 0:
                self.renderer = Animation(list_enemy,loop=True,frame_delay=1)
                self.stun = False
                self.stunCooldown = 20
        if not self.stun:
            self.enemy_move(3)
        self.deactivate_if_need()
        # self.x += self.velocityX
        # self.y += self.velocityY


    def deactivate(self):
        self.is_active = False

    def enemy_move(self,vantoc):
        if self.y < 150 and self.first_move is False :
            self.y += vantoc
        if self.y == 150 and self.first_move is False:
            self.x -= vantoc
        if  self.x == 89 :
            self.first_move = True
            self.y+= vantoc
        if self.y == 360 :
            self.x += vantoc
        if self.x == 518:
            self.y += vantoc
        if self.y == 618:
            self.x -= vantoc

        tower_defense.game_object.get_position_from_main = (self.x, self.y)  # new
    def deactivate_if_need(self):
        if self.y >=800:
            self.deactivate()
            try:
                tower_defense.game_object.game_objects.remove(self)
            except ValueError:
                pass
            
