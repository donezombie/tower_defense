# from tower_defense.game_object import GameObject
# from renderers.image_renderer import ImageRenderer
# from scenes.gameplay_scene import GamePlayScene
# from scenes.scene_manager import global_scene_manager
# from tower_defense.castle import *

# class GameOver(GameObject):
#     def __init__(self,x,y):
#         GameObject .__init__(self,x,y)
#         self.renderer = ImageRenderer("c4t-online-starter-master/images/background/background.png")
#     def update(self):
#         GameObject.update(self)
#         if tower_defense.game_object.hp_castle == 0:
#             gameplay_scene = GamePlayScene()
#             global_scene_manager.change_scene(gameplay_scene)
