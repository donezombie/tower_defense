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
        self.frame_counter = FrameCounter(120)

    def update(self):
        GameObject.update(self)
        self.frame_counter.run()
        if self.frame_counter.flag:
            tower_defense.game_object.hasEnemy = True
            if tower_defense.game_object.score <60:
                boss = Boss(425,0)
                add(boss)
            elif tower_defense.game_object.score >= 60 and tower_defense.game_object.score < 65:
                self.frame_counter = FrameCounter(80)
                boss = Boss(425,0)
                boss.HP = 7
                add(boss)
            elif tower_defense.game_object.score >= 120 and tower_defense.game_object.score < 130:
                self.frame_counter = FrameCounter(50)
                boss = Boss(425,0)
                boss.HP = 13
                add(boss)
            else:
                self.frame_counter = FrameCounter(120)
                boss = Boss(425,0)
                boss.HP = 50
                # boss.renderer = Animation(,loop=True,frame_delay=1)
                add(boss)
            self.frame_counter.reset()
