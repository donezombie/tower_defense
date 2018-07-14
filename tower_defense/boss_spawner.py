import random
from tower_defense.game_object import GameObject
from physics.box_collider import BoxCollider
import tower_defense.game_object
from control_move_enemy import *
from renderers.animation import Animation
from tower_defense.boss import *
from frame_counter import *
from img_animation import  *
from tower_defense.game_object import *
class BossSpawner(GameObject):
    def __init__(self,x,y):
        GameObject.__init__(self,0,200)
        self.frame_counter = FrameCounter(10)

    def update(self):
        GameObject.update(self)
        self.frame_counter.run()
        if self.frame_counter.flag:
            tower_defense.game_object.hasEnemy = True
            boss = Boss(425,0)
            add(boss)
            self.frame_counter.reset()