from tower_defense.game_object import GameObject
from renderers.image_renderer import ImageRenderer
class Menu(GameObject):
    def __init__(self,x,y):
        GameObject .__init__(self,x,y)
        self.renderer = ImageRenderer("c4t-online-starter-master/images/background/background.png")