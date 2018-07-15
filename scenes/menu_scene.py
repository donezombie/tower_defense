from menu.menu import Menu
from tower_defense.game_object import *
from menu.end_scene import *
from menu.start import Start
class MenuScene:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('music/intro.wav')
        pygame.mixer.music.play(-1)
    def setup(self):
        # print("Menu scene setup")
        menu = Menu(300,400)
        add(menu)
        start = Start(300,500)
        add(start)

        
    def destroy(self):
        clear()