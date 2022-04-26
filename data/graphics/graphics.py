import os
import pygame


def load(name, alpha=False):
    image = pygame.image.load(os.path.join(os.path.dirname(__file__), name))

    if alpha:
        return image.convert_alpha()
    return image.convert()
