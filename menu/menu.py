from tower_defense.game_object import GameObject
from renderers.animation import Animation
class Menu(GameObject):
    def __init__(self,x,y):
        GameObject .__init__(self,x,y)
        self.renderer = Animation(["images/gamestartscreen1.png",
        "images/gamestartscreen2.png",
        "images/gamestartscreen3.png",
        "images/gamestartscreen4.png",
        "images/gamestartscreen5.png",
        "images/gamestartscreen6.png",
        "images/gamestartscreen7.png",
        "images/gamestartscreen8.png",
        "images/gamestartscreen9.png",
        "images/gamestartscreen10.png",
        "images/gamestartscreen11.png",],loop = True,frame_delay = 10)