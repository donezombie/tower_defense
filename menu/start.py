from tower_defense.game_object import GameObject
from renderers.image_renderer import ImageRenderer
from scenes.scene_manager import global_scene_manager
from scenes.gameplay_scene import GamePlayScene
from tower_defense.input_manager import global_input_manager

class Start(GameObject):
    def __init__(self,x,y):
        GameObject.__init__(self,x,y)
        self.renderer = ImageRenderer("c4t-online-starter-master/images/menu.png")
    def update(self):
        GameObject.update(self)
        if global_input_manager.enter_pressed:
            gameplay_scene = GamePlayScene()
            global_scene_manager.change_scene(gameplay_scene)