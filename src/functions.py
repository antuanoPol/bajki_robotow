import pygame

from src.statics import *

# Iniclaizowanie potrzebnych zmiennych
font_name = pygame.font.match_font("arial")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
background = pygame.image.load(path.join(img_dir, "background-scifi.png")).convert()


def rotate(rot, image):
    new_image = pygame.transform.rotate(image, rot)
    return new_image


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def calculate_direction(keystate):
    direction = None
    if keystate[pygame.K_LEFT]:
        direction = LEFT
    if keystate[pygame.K_RIGHT]:
        direction = RIGHT
    if keystate[pygame.K_UP]:
        direction = UP
    if keystate[pygame.K_DOWN]:
        direction = DOWN

    return direction


def show_go_screen():
    screen.blit(background, background.get_rect())
    draw_text(screen, "BAJKI ROBOTÓW", 84, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Press arrows key to move, Space to fire", 42, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Click any key to begin the game", 28, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


def exit_door_opened(doors):
    exit_door_count = 0
    for door in doors:
        if door.exit_door:
            exit_door_count += 1

    return exit_door_count < 2


def question_asked(questions):
    for q in questions:
        if q.initialized:
            return True
    return False

def show_win_screen():
    screen.blit(background, background.get_rect())
    draw_text(screen, "YOU WIN", 84, WIDTH/2, HEIGHT/ 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
