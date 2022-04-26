import sys
import pygame
from data.car import Car

from data.graphics.graphics import load


def main():
    screen = pygame.display.set_mode((640, 480))
    player = Car(load("player.png", alpha=True))
    background = load("grass.bmp")
    screen.blit(background, (0, 0))
    position = player.pos
    screen.blit(player.image, position)
    pygame.display.update()
    while True:
        pressed = pygame.key.get_pressed()
        player.handle_keys(pressed)
        if pressed[pygame.K_q]:
            break
        screen.blit(background, (0, 0))
        rotated_player = pygame.transform.rotate(player.image, player.angle)
        rect = rotated_player.get_rect(center=player.pos.center)
        screen.blit(rotated_player, rect)
        pygame.display.update()
        pygame.event.pump()
        pygame.time.delay(20)
