import pygame
from tower_defense.game_object import *
from tower_defense.input_manager import InputManager,global_input_manager
from frame_counter import *
from physics.box_collider_player import *
from tower_defense.tower import Tower
from tower_defense.player_animator import PlayerAnimator
import tower_defense.game_object
from tower_defense.hole import *
from cost_tower import *
position_hole = (-999,-999)
class Player(GameObject):
    def __init__(self,x,y):
        global position_hole
        GameObject. __init__(self,x,y)
        self.frame_counter = FrameCounter(20)
        self.tower_lock = False
        self.box_collider =  BoxColliderPlayer(10,20)
        self.renderer = PlayerAnimator()
        self.dx = 0
        self.dy = 0
    def update_animator(self):
        self.renderer.update(self.dx,self.dy)

    def update(self):
        GameObject.update(self)
        self.update_animator()
        self.move()
    
    def build_hole(self):
        collide_list = collide_with(self.box_collider)
        for game_object in collide_list:
            if type(game_object) == Hole and game_object.builded == False:
                if tower_defense.game_object.coin >= tower_ice :
                    tower_defense.game_object.coin -= tower_ice
                    game_object.deactivate()
                    game_object.builded = True
                    position_hole = game_object.x, game_object.y
                    new_tower = Tower(position_hole[0],position_hole[1])
                    add(new_tower)

    def move(self):
        self.dx = 0
        self.dy = 0
        if global_input_manager.right_pressed:
            self.dx +=5
        if global_input_manager.left_pressed:
            self.dx-=5
        if global_input_manager.up_pressed:
            self.dy -=5
        if global_input_manager.down_pressed:
            self.dy+=5
        if global_input_manager.x_pressed:
            tower_defense.game_object.build_stt = True

        self.x += self.dx
        self.y += self.dy
        self.frame_counter.run()
        if global_input_manager.x_pressed:
            self.build_hole()
                



