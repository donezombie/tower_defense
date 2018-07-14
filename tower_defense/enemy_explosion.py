from tower_defense.game_object import GameObject
from renderers.animation import Animation
class EnemyExplosion(GameObject):
    def __init__(self,x,y):
        GameObject.__init__(self,x,y)
        self.renderer = Animation(["images/player.png",
                                   "images/player-bullet.png",
                                   "images/enemy.png"])
