from ast import Load
import pygame
from data.car import Car

from data.graphics.graphics import load

wasd_controls = (pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a)
arrow_controls = (pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT)


def main():
    screen = pygame.display.set_mode((640, 480))
    players = []
    players.append(Car(load("player_red.png", alpha=True), wasd_controls))
    background = load("grass.bmp")
    screen.blit(background, (0, 0))
    for player in players:
        position = player.pos
        screen.blit(player.image, position)
    pygame.display.update()
    while True:
        pressed = pygame.key.get_pressed()
        for player in players:
            player.handle_keys(pressed)
        if pressed[pygame.K_q]:
            break
        screen.blit(background, (0, 0))
        for player in players:
            rotated_player = pygame.transform.rotate(player.image, player.angle)
            rect = rotated_player.get_rect(center=player.pos.center)
            screen.blit(rotated_player, rect)
        pygame.display.update()
        pygame.event.pump()
        pygame.time.delay(20)
