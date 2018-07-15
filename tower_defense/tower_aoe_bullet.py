import tower_defense.game_object
from tower_defense.game_object import GameObject
from physics.box_collider import BoxCollider
from tower_defense.game_object import collide_with,add as add_game_object
from tower_defense.enemy import *
from tower_defense.boss import *
from renderers.animation import Animation
from renderers.image_renderer import *
from tower_defense.enemy_explosion import EnemyExplosion, BossExplosion
from tower_defense.game_object import *
from quick_math import *
from img_animation import list_bullet
import pygame
import math

class TowerBulletAOE(GameObject):
    def __init__(self,x,y,e_x,e_y):
        GameObject.__init__(self,x,y)
        self.box_collider = BoxCollider(15,15)
        self.renderer = Animation(list_bullet_shotgun,loop=True,frame_delay=1)
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
                if type(game_object) == Enemy:
                    if game_object.is_active:
                        explosion = EnemyExplosion(game_object.x, game_object.y)
                        add_game_object(explosion)
                        effect = pygame.mixer.Sound('music/greentower.wav')
                        effect.play()
                        game_object.deactivate()
                        # game_object.stun = True
                        self.deactivate()
                        dead = pygame.mixer.Sound('music/monsterdeath.wav')
                        dead.play()
                        collide_list.remove(self)
                        tower_defense.game_object.game_objects.remove(game_object)
                        tower_defense.game_object.game_objects.remove(self)
                        game_object.isDeath = True             
                        tower_defense.game_object.score += 1
                        tower_defense.game_object.coin += 1
                    else:
                        self.deactivate()

                if type(game_object) == Boss and game_object.is_active:
                    effect = pygame.mixer.Sound('music/greentower.wav')
                    effect.play()
                    game_object.HP -= 1
                    self.deactivate()
                    if game_object.HP <= 0:
                        # game_object.stun = True
                        explosion = BossExplosion(game_object.x, game_object.y)
                        add_game_object(explosion)
                        dead = pygame.mixer.Sound('music/monsterdeath.wav')
                        dead.play()
                        game_object.deactivate()
                        self.deactivate()
                        tower_defense.game_object.game_objects.remove(game_object)
                        tower_defense.game_object.game_objects.remove(self)
                        collide_list.remove(game_object)
                        collide_list.remove(self)

                        tower_defense.game_object.score += 5
                        tower_defense.game_object.coin += 3

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
            if self.length(self.vectorX, self.vectorY) < 6:
                self.is_active = False
            else:
                self.velocityX = self.vectorX/((self.vectorX**2 + self.vectorY**2)**(1/2))*10
                self.velocityY = self.vectorY/((self.vectorX**2 + self.vectorY**2)**(1/2))*10
        except ZeroDivisionError:
            pass
        
    
    def length(self, x, y):
        return math.sqrt(x * x + y * y)
        
        

    def update(self):
        # print(self.velocityX, self.vectorY)
        GameObject.update(self)
        self.pyshicsWithEnemy()
        self.move()
        self.x += self.velocityX
        self.y += self.velocityY
        self.cooldown -= 1
        if self.cooldown <= 0:
            self.deactivate()
            self.cooldown = 80
        if self.x == self.e_x and self.y == self.e_y:
            self.deactivate()

    def clear(self):
        self.velocity = (0, 0)


    def deactivate(self):
        self.is_active = False