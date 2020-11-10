from src.character import Character


class Player(Character):
    def __init__(self, x, y, angle, width, height, sprite, flip, observer, max_vspeed, max_hspeed, friction, vacceleration,
                 hacceleration):
        super().__init__(x, y, angle, width, height, sprite, flip, observer)
        self.vacceleration = vacceleration
        self.hacceleration = hacceleration
        self.friction = friction
        self.max_hspeed = max_hspeed
        self.max_vspeed = max_vspeed
        self.vspeed = 0
        self.hspeed = 0

    def update_position(self):
        self.x += self.vspeed
        self.y += self.hspeed
        self.hspeed *= (1 - self.friction)
        self.vspeed *= (1 - self.friction)
        if self.x < -10:
            self.x = self.observer.width - 10
        elif self.x > self.observer.width + 10:
            self.x = 10

    def send_input(self, key):
        if key == "w":
            self.hspeed = self.hspeed + (self.max_hspeed - abs(self.hspeed)) * -self.hacceleration
        if key == "s":
            self.hspeed = self.hspeed + (self.max_hspeed - abs(self.hspeed)) * self.hacceleration
        if key == "a":
            self.vspeed = self.vspeed + (self.max_vspeed - abs(self.vspeed)) * -self.vacceleration
        if key == "d":
            self.vspeed = self.vspeed + (self.max_vspeed - abs(self.vspeed)) * self.vacceleration
        if self.vspeed < 0:
            self.flip = True
        elif self.vspeed > 0:
            self.flip = False