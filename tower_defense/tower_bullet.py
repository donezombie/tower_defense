import tower_defense.game_object
from tower_defense.game_object import GameObject
from physics.box_collider import BoxCollider
from tower_defense.game_object import collide_with,add as add_game_object
from tower_defense.enemy import *
from tower_defense.boss import *
from renderers.animation import Animation
from tower_defense.enemy_explosion import EnemyExplosion
from tower_defense.game_object import *
from quick_math import *
from img_animation import list_bullet
class TowerBullet(GameObject):
    def __init__(self,x,y,e_x,e_y):
        GameObject.__init__(self,x,y)
        self.box_collider = BoxCollider(15,15)
        self.renderer = Animation(list_bullet,loop=True,frame_delay=1)
        self.e_x = e_x
        self.e_y = e_y
        self.cooldown = 80
        self.velocity = (0,0)
        self.vectorX = 0
        self.vectorY = 0
        self.velocityX = 0
        self.velocityY = 0
        

    def pyshicsWithEnemy(self):
        try:
            collide_list = collide_with(self.box_collider)
            for game_object in collide_list:
                if type(game_object) == Enemy and game_object.is_active:
                    # explosion = EnemyExplosion(game_object.x, game_object.y)
                    # add_game_object(explosion)
                    # game_object.deactivate()
                    game_object.stun = True
                    self.deactivate()
                    tower_defense.game_object.game_objects.remove(self)
                    collide_list.remove(self)
                    # tower_defense.game_object.coin += 1

                if type(game_object) == Boss and game_object.is_active:
                    game_object.HP -= 1
                    if game_object.HP <= 0:
                        explosion = EnemyExplosion(game_object.x, game_object.y)
                        add_game_object(explosion)
                        game_object.deactivate()
                        self.deactivate()
                        tower_defense.game_object.game_objects.remove(game_object)
                        tower_defense.game_object.game_objects.remove(self)
                        collide_list.remove(game_object)
                        collide_list.remove(self)
                        tower_defense.game_object.coin += 2

        except ValueError:
            pass
        

    def FollowEnemy(self,e_x,e_y):
        if self.is_active:
            try:
                distance = (get_distance((self.x, self.y),
                                         (e_x, e_y)))
                self.velocity = ((-e_x + self.x) / distance * -5,
                                 (-e_y + self.y) / distance * -5)
            except ZeroDivisionError:
                pass

        self.vx, self.vy = self.velocity
        self.x += self.vx
        self.y += self.vy

    def move(self):
        # if self.x > self.e_x:
        #     self.x -= speed
        # elif self.x < self.e_x:
        #     self.x += speed
        # # Movement along y direction
        # if self.y < self.e_y:
        #     self.y += speed
        # elif self.y > self.e_y:
        #     self.y -= speed
        try:
            self.vectorX = self.e_x - self.x
            self.vectorY =  self.e_y - self.y
            self.velocityX = self.vectorX/((self.vectorX**2 + self.vectorY**2)**(1/2))*5
            self.velocityY = self.vectorY/((self.vectorX**2 + self.vectorY**2)**(1/2))*5
        except ZeroDivisionError:
            pass
        
        

    def update(self):
        GameObject.update(self)
        self.pyshicsWithEnemy()
        self.move()
        self.x += self.velocityX
        self.y += self.velocityY
        self.cooldown -= 1
        if self.cooldown <= 0:
            self.deactivate()
            self.cooldown = 80

    def clear(self):
        self.velocity = (0, 0)


    def deactivate(self):
        self.is_active = False