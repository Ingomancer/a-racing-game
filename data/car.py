import math

MAX_SPEED = 8

class Car:
    def __init__(self, image, controls):
        self.image = image
        self.pos = image.get_rect()
        self.angle = 0
        self.speed = 0
        self.x = self.pos.centerx
        self.y = self.pos.centery
        self.up, self.down, self.right, self.left = controls

    def handle_keys(self, pressed):
        radians = math.radians(self.angle)
        dx = self.speed * math.cos(radians)
        dy = -self.speed * math.sin(radians)
        if pressed[self.up]:
            if self.speed < MAX_SPEED:
                self.speed += 1
        if pressed[self.down]:
            if self.speed > -MAX_SPEED:
                self.speed -= 1
        if pressed[self.right]:
            self.angle -= 5
        if pressed[self.left]:
            self.angle += 5
        self.x += dx
        self.y += dy
        self.pos.centerx = int(self.x)
        self.pos.centery = int(self.y)
