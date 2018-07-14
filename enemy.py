from game_object import GameObject

class Enemy(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)

    def update(self):
        GameObject.update(self)
        self.y += 3