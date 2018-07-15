from tower_defense.game_object import GameObject
from renderers.image_renderer import ImageRenderer
from physics.box_collider import *
from tower_defense.enemy_explosion import *
from tower_defense.game_object import *
from tower_defense.enemy import *
from tower_defense.boss import *
from scenes.scene_manager import *
from scenes.game_over_scene import GameOverScene
# from game_over.game_over import GameOver 
# game_over = GameOver()

class Castle(GameObject):
    def __init__(self,x,y):
        GameObject. __init__(self,x,y )
        self.renderer = ImageRenderer("images/castle.png")
        self.box_collider = BoxCollider(70,70)
        self.HP = 5

    def update(self):
        GameObject.update(self)
        self.pyshicsWithEnemy()
        # print(self.HP)
        if self.HP == 0:
            game_over = GameOverScene()
            global_scene_manager.change_scene(game_over)
            self.deactivate()
            # print("Thua")

    def pyshicsWithEnemy(self):
        collide_list = collide_with(self.box_collider)
        for game_object in collide_list:
            if type(game_object) == Enemy and game_object.is_active:
                explosion = EnemyExplosion(game_object.x, game_object.y)
                add(explosion)
                game_object.deactivate()
                self.HP -= 1
                tower_defense.game_object.hp_castle = self.HP

            if type(game_object) == Boss and game_object.is_active:
                explosion = BossExplosion(game_object.x, game_object.y)
                add(explosion)
                game_object.deactivate()
                self.HP -= 1
                tower_defense.game_object.hp_castle = self.HP
            
    def deactivate(self):
        self.is_active = False

