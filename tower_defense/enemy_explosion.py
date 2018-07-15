from tower_defense.game_object import GameObject
from renderers.animation import Animation
from img_animation import *
class EnemyExplosion(GameObject):
    def __init__(self,x,y):
        GameObject.__init__(self,x,y)
        self.renderer = Animation(enemydie)

class BossExplosion(GameObject):
    def __init__(self,x,y):
        GameObject.__init__(self,x,y)
        self.renderer = Animation(bossdie)
