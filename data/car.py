import math
import pygame


class Car:
    def __init__(self, image):
        self.image = image
        self.pos = image.get_rect()
        self.angle = 0
        self.speed = 5

    def handle_keys(self, pressed):
        radians = math.radians(self.angle)
        x = self.speed * math.cos(radians)
        y = self.speed * math.sin(radians)
        if pressed[pygame.K_UP] or pressed[pygame.K_w]:
            self.pos = self.pos.move(x, -y)
        if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
            self.pos = self.pos.move(-x, y)
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            self.angle -= 5
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
            self.angle += 5
