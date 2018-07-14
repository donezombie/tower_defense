from renderers.animation import Animation
from img_animation import *
import tower_defense.game_object
class PlayerAnimator:
    def __init__(self):
        self.left_animation = Animation(left_player,loop=True)
        self.straight_animation = Animation(straight_player,loop=True)
        self.right_animation = Animation(right_player,loop=True)
        self.build_animation = Animation(build_animation,loop=True)
        self.current_animation = self.straight_animation
    def render(self,canvas,x,y):
        self.current_animation.render(canvas,x,y)
    def update(self,player_dx,player_dy):
        if player_dx <0:
            self.current_animation = self.left_animation
        elif player_dx >0 :
            self.current_animation = self.right_animation
        else:
            self.current_animation = self.straight_animation
        if tower_defense.game_object.build_stt == True:
            self.current_animation = self.build_animation
            tower_defense.game_object.build_stt = False
