class Character:
    def __init__(self, x, y, angle, width, height, sprite, flip, observer):
        self.observer = observer
        self.flip = flip
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.sprite = sprite
        self.angle = angle

    def move(self, x, y):
        self.x += x
        self.y += y

    def rotate(self, angle):
        self.angle += angle
