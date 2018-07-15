from scenes.menu_scene import *
from menu.end_scene import EndScene
from tower_defense.game_object import *
class GameOverScene:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('music/outtro.wav')
        pygame.mixer.music.play(-1)
    def setup(self):
        game_over = EndScene(300,400)
        add(game_over)
        
    def destroy(self):
        clear()