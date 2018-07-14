from menu.menu import Menu
from tower_defense.game_object import *
from menu.start import Start
class MenuScene:
    def __init__(self):
        pass
    def setup(self):
        # print("Menu scene setup")
        menu = Menu(300,400)
        add(menu)
        start = Start(300,500)
        add(start)
        pass
    def destroy(self):
        clear()