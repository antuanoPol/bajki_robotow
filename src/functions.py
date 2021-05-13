import pygame

from src.statics import *

# Iniclaizowanie potrzebnych zmiennych
font_name = pygame.font.match_font("arial")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
background_img = pygame.image.load(path.join(img_dir, "background-scifi.png")).convert()
keyboard = pygame.image.load(path.join(img_dir, "keyboard.png")).convert()
keyboard_img = pygame.transform.scale(keyboard, (360, 260))
keyboard_img.set_colorkey(BLACK)


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
    screen.blit(background_img, background_img.get_rect())
    draw_text(screen, "BAJKI ROBOTÓW", 84, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Strzałki sterują robotem a spacja to atak", 42, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Naciśnij dowolny klawisz żeby zacząć grę", 28, WIDTH / 2, HEIGHT * 3 / 4)
    draw_text(screen, "Dojdź do krzyża", 28, WIDTH/2 , HEIGHT*4 / 5)
    draw_keyboard(screen, (WIDTH / 2) - keyboard_img.get_rect().width / 2, HEIGHT / 2 , keyboard_img)
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
    screen.blit(background_img, background_img.get_rect())
    draw_text(screen, "WYGRAŁEŚ", 84, WIDTH / 2, HEIGHT / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


def show_die_screen():
    screen.blit(background_img, background_img.get_rect())
    draw_text(screen, "PRZEGRAŁEŚ", 84, WIDTH / 2, HEIGHT / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)


def draw_keyboard(surf, x, y, img):
    img_rect = img.get_rect()
    img_rect.x = x
    img_rect.y = y
    surf.blit(img, img_rect)

def draw_red_cross(surf, x, y, img):
    img_rect = img.get_rect()
    img_rect.x = x
    img_rect.y = y
    surf.blit(img, img_rect)