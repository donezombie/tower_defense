from game_object import GameObject


class PlayerBullet(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)

    def update(self):
        GameObject.update(self)
        self.y -= 10