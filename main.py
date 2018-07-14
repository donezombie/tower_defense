import pygame
import tower_defense.game_object
from tower_defense.game_object import *
from tower_defense.input_manager import global_input_manager
from scenes.scene_manager import global_scene_manager
from scenes.menu_scene import MenuScene

pygame.init()

clock = pygame.time.Clock()

SCREEN_SIZE= (600,800)
canvas = pygame.display.set_mode(SCREEN_SIZE)
background_image = pygame.image.load("images/background/background.png")
pygame.display.set_caption("Tower Defense")

menu_scene = MenuScene()
global_scene_manager.change_scene(menu_scene)


loop = True
while loop:
    print(tower_defense.game_object.coin)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            global_input_manager.update(event)
    #update
    update()

    #canvas
    canvas.blit(background_image,(0,0))


    render(canvas)
    pygame.display.flip()
    clock.tick(60)
