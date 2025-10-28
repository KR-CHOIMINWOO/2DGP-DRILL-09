from pico2d import load_image

class Grass():
    next_y = 20

    def __init__(self):
        self.image = load_image('grass.png')
        self.y = Grass.next_y
        Grass.next_y -= 20

    def draw(self):
        self.image.draw(400, self.y)

    def update(self):
        pass
