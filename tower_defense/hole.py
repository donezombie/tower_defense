from tower_defense.game_object import GameObject
from renderers.image_renderer import ImageRenderer
from physics.box_collider import BoxCollider
class Hole(GameObject):
    def __init__(self,x,y):
        GameObject.__init__(self,x,y)
        self.builded = False
        self.box_collider = BoxCollider(70, 70)
    
    def deactivate(self):
        self.is_active = False