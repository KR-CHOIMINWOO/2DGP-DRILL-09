from pico2d import load_image

class Grass():
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        grass_y = 20
        self.image.draw(400, grass_y)
        grass_y -= 20

    def update(self):
        pass
