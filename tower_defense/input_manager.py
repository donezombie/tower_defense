import pygame
import tower_defense.game_object
from cost_tower import *
class InputManager:
    def __init__(self):
        self.right_pressed = False
        self.left_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.x_pressed = False
        self.c_pressed = False
        self.z_pressed = False
        self.enter_pressed = False
    def update(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.right_pressed = True
            elif event.key == pygame.K_LEFT:
                self.left_pressed = True
            elif event.key == pygame.K_UP:
                self.up_pressed = True
            elif event.key == pygame.K_DOWN:
                self.down_pressed = True
            elif event.key == pygame.K_x:
                self.x_pressed = True
            elif event.key == pygame.K_RETURN:
                self.enter_pressed = True
            elif event.key == pygame.K_c:
                self.c_pressed = True
            elif event.key == pygame.K_z:
                self.z_pressed = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.right_pressed = False
            elif event.key == pygame.K_LEFT:
                self.left_pressed = False
            elif event.key == pygame.K_UP:
                self.up_pressed =False
            elif event.key == pygame.K_DOWN:
                self.down_pressed = False
            elif event.key == pygame.K_x:
                self.x_pressed = False
            elif event.key == pygame.K_RETURN:
                self.enter_pressed = False
            elif event.key == pygame.K_c:
                self.c_pressed = False
            elif event.key == pygame.K_z:
                self.z_pressed = False

global_input_manager = InputManager()

