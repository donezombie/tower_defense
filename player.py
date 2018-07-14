from game_object import GameObject, add
from bullet import PlayerBullet
import pygame


class Player(GameObject):
    def __init__(self, x, y, input_manager):
        GameObject.__init__(self, x, y)
        self.input_manager = input_manager

    def update(self):
        if self.input_manager.right_pressed:
            self.x += 5
        if self.input_manager.left_pressed:
            self.x -= 5
        if self.input_manager.down_pressed:
            self.y += 5
        if self.input_manager.up_pressed:
            self.y -= 5

        if self.input_manager.x_pressed:
            bullet = PlayerBullet(self.x, self.y)
            bullet.image = pygame.image.load("images/bullet/player/mb69bullet1.png")
            add(bullet)
