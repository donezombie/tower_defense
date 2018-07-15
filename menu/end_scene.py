from tower_defense.game_object import GameObject
from renderers.animation import Animation
from tower_defense.input_manager import *
# from scenes.scene_manager import global_scene_manager
# from scenes.gameplay_scene import *
# import tower_defense.game_object
# from scenes.game_over_scene import GameOverScene

class EndScene(GameObject):
    def __init__(self,x,y):
        GameObject.__init__(self,x,y)
        self.renderer = Animation(["images/gameover1.png",
        "images/gameover2.png",
        "images/gameover3.png",
        "images/gameover4.png",
        "images/gameover5.png",
        "images/gameover6.png",
        "images/gameover7.png",
        "images/gameover8.png",],loop = True,frame_delay=10)
    # def update(self):
    #     GameObject.update(self)
    #     if global_input_manager.enter_pressed:
    #         gameplay_scene = GamePlayScene()
    #         global_scene_manager.change_scene(gameplay_scene)