hasEnemy = False
build_stt = False
hp_castle = 5
coin = 40
score = 0
wave = 30

import pygame
class GameObject:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.box_collider = None
        self.tower_circle = None
        self.is_active = True
        self.renderer = None

    def update(self):
        if self.box_collider is not None:
            self.box_collider.x = self.x
            self.box_collider.y = self.y
        if self.tower_circle is not None:
            self.tower_circle.x = self.x
            self.tower_circle.y = self.y

    def render(self,canvas):
        if self.renderer is not None and self.is_active:
            self.renderer.render(canvas, self.x, self.y)
        if self.box_collider is not None and self.box_collider.is_active:
            self.box_collider.render(canvas)
        if self.tower_circle is not None:
            self.tower_circle.render(canvas)

game_objects = []

# checkHole(player_x,player_y,p)

def add(new_object):
    game_objects.append(new_object)

def update():
    for game_object in game_objects:
        if game_object.is_active:
            game_object.update()

def render(canvas):
    for game_object in game_objects:
        if game_object.is_active:
            game_object.render(canvas)

get_position_from_main = (0,0)



def collide_with(box_collider):
    collide_list=[]
    for game_object in game_objects:
        if game_object.is_active and game_object.box_collider is not None:
            if game_object.box_collider.overlap(box_collider):
                collide_list.append(game_object)
    return collide_list

def recycle(t, x, y):
    for game_object in game_objects:
        if not game_object.is_active and type(game_object) == t:
            game_object.is_active = True
            game_object.x = x
            game_object.y = y
            return game_object

    new_game_object = t(x, y)
    add(new_game_object)
    return new_game_object
def clear():
    game_objects.clear()

def deactivate(self):
    self.is_active = False