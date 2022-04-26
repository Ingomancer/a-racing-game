import math
import pygame


class Car:
    def __init__(self, image, controls):
        self.image = image
        self.pos = image.get_rect()
        self.angle = 0
        self.speed = 5
        self.up, self.down, self.right, self.left = controls

    def handle_keys(self, pressed):
        radians = math.radians(self.angle)
        x = self.speed * math.cos(radians)
        y = self.speed * math.sin(radians)
        if pressed[self.up]:
            self.pos = self.pos.move(x, -y)
        if pressed[self.down]:
            self.pos = self.pos.move(-x, y)
        if pressed[self.right]:
            self.angle -= 5
        if pressed[self.left]:
            self.angle += 5
