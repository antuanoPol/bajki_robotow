import pygame

from src.question import Question
from src.question import questions_datas
from src.statics import *

pygame.mixer.init()  # inicjalizuje dzwięki
door_img = pygame.image.load(path.join(img_dir, "Scifi Spritesheet.png"))
door_orig_img = pygame.transform.scale(door_img, (60, 60))
door_open_sound = pygame.mixer.Sound(path.join(snd_dir, "door.mp3"))

doors_animation = []
for i in range(11):
    file_name = "image" + "_" + str(i + 1) + ".png"
    file = pygame.image.load(path.join(doors_animation_dir, file_name))
    file = pygame.transform.scale(file, (60, 60))
    image = file
    image.set_colorkey(BLACK)
    doors_animation.append(image)


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, players, question_number, exit_door):
        pygame.sprite.Sprite.__init__(self)
        self.image = door_orig_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 20
        self.players = players
        self.question = Question(questions_datas[question_number])
        self.hit_with_player = None
        self.exit_door = exit_door

    def update(self):
        self.is_player_touched()

    def animated(self):
        now = pygame.time.get_ticks()
        door_open_sound.play()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(doors_animation):
                self.question.kill()
                self.hit_with_player.points += self.question.answer_points
                self.kill()
            else:
                center = self.rect.center
                self.image = doors_animation[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def is_player_touched(self):
        hit_with_players = pygame.sprite.spritecollide(self, self.players, False, pygame.sprite.collide_circle)
        if self.question.finished:
            self.animated()
            return
        if len(hit_with_players) > 0:
            self.hit_with_player = hit_with_players[0]
            self.question.initialized = True
