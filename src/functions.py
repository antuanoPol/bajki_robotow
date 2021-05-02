import pygame
from statics import *

# Iniclaizowanie fontow
font_name = pygame.font.match_font("arial")


def rotate(rot, image):
    new_image = pygame.transform.rotate(image, rot)
    return new_image


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def calculate_direction(main_player, keystate):
    direction = None
    if main_player:
        if keystate[pygame.K_LEFT]:
            direction = LEFT
        if keystate[pygame.K_RIGHT]:
            direction = RIGHT
        if keystate[pygame.K_UP]:
            direction = UP
        if keystate[pygame.K_DOWN]:
            direction = DOWN
    else:
        if keystate[pygame.K_a]:
            direction = LEFT
        if keystate[pygame.K_d]:
            direction = RIGHT
        if keystate[pygame.K_w]:
            direction = UP
        if keystate[pygame.K_s]:
            direction = DOWN
    return direction
