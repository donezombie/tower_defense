import pygame
import tower_defense.game_object
from tower_defense.game_object import *
from tower_defense.input_manager import global_input_manager
from scenes.scene_manager import global_scene_manager
from scenes.menu_scene import MenuScene
from scenes.game_over_scene import EndScene
from tower_defense.boss_spawner import *

pygame.init()
myfont = pygame.font.SysFont("monospace", 30)
clock = pygame.time.Clock()

SCREEN_SIZE= (600,800)
canvas = pygame.display.set_mode(SCREEN_SIZE)
background_image = pygame.image.load("images/background/background.png")
pygame.display.set_caption("Tower Defense")

menu_scene = MenuScene()
global_scene_manager.change_scene(menu_scene)

# if tower_defense.game_object.hp_castle == 0:
   
#     end = End(300,400)
#     global_scene_manager.change_scene(end)


loop = True
new_wave = False
while loop:    
    for game_object in game_objects:
        if type(game_object) == EndScene and game_object.is_active:
            if global_input_manager.enter_pressed:
                menu_scene = MenuScene()
                global_scene_manager.change_scene(menu_scene)
                tower_defense.game_object.coin = 35
                tower_defense.game_object.wave = 30
                tower_defense.game_object.score = 0
                tower_defense.game_object.hp_castle = 5

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            global_input_manager.update(event)
    #update
    label = myfont.render("Score:{0}".format(tower_defense.game_object.score), 1, (255,0,0))
    coin = myfont.render("Coin: {0}".format(tower_defense.game_object.coin),1,(255,0,0))
    hp = myfont.render("HP:{0}".format(tower_defense.game_object.hp_castle),1,(255,0,0))
    update()

    #canvas
    canvas.blit(background_image,(0,0))
    canvas.blit(hp,(90,670))
    canvas.blit(label, (230, 750))
    canvas.blit(coin,(400,750))

    render(canvas)
    pygame.display.flip()
    clock.tick(60)
