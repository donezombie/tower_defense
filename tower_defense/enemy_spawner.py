from frame_counter import FrameCounter
from tower_defense.enemy import Enemy
from tower_defense.game_object import *
from tower_defense.boss import Boss
import tower_defense.game_object
import pygame
import random

class EnemySpawner(GameObject):
    def __init__(self,x,y):
        GameObject.__init__(self, 0, 200)
        self.frame_counter = FrameCounter(tower_defense.game_object.wave)

    def update(self):
        GameObject.update(self)
        self.frame_counter.run()
        if tower_defense.game_object.hasTower == True:
            if self.frame_counter.flag:
                tower_defense.game_object.hasEnemy = True
                enemy = Enemy(425,0)
                add(enemy)
                self.frame_counter.reset()
            if tower_defense.game_object.score >= 60 and tower_defense.game_object.score < 65:
                self.frame_counter = FrameCounter(15)

