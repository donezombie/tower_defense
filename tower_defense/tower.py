from tower_defense.tower_bullet import *
from tower_defense.game_object import *
from tower_defense.game_object import GameObject
from frame_counter import *
from  physics.box_collider import BoxCollider
import  tower_defense.game_object
from physics.tower_circle import *
from renderers.animation import Animation
from img_animation import *
import pygame
class Tower(GameObject) :
    def __init__(self,x,y):
        GameObject.__init__(self,x,y-20)
        self.frame_counter = FrameCounter(30)
        self.shoot_lock = False
        self.box_collider = BoxCollider(64,80)
        # self.tower_circle = Tower_circle(0,0)
        self.rangeCheck = False
        self.range = 0
        self.enemy_x =  tower_defense.game_object.get_position_from_main[0]
        self.enemy_y =  tower_defense.game_object.get_position_from_main[1]
        self.renderer = Animation(list_tower,loop=True,frame_delay=30)

    def update(self):
        GameObject.update(self)
        self.check()

    def shoot(self,e_x,e_y):
        # print(tower_defense.game_object.hasEnemy)
        if tower_defense.game_object.hasEnemy == True:
            if self.shoot_lock == False:
                bullet = TowerBullet(self.x,self.y,e_x,e_y)
                add(bullet)
                # bullet = TowerBullet()
                self.shoot_lock = True

            self.frame_counter.run()
            if self.shoot_lock:
                if self.frame_counter.flag == True:
                    self.shoot_lock = False
                    self.frame_counter.reset()

    def check(self):
        for game_object in game_objects:
            if ((type(game_object) == Enemy or type(game_object) == Boss) and game_object.is_active):
                self.range = ((self.x - game_object.x)**2 + (self.y - game_object.y)**2)**0.5
                if self.range <= radius:
                    self.shoot(game_object.x,game_object.y)
                    self.rangeCheck = True
                    break
                else:
                    self.rangeCheck = False
            


