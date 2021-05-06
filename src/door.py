import pygame
from statics import *

door_img = pygame.image.load(path.join(img_dir, "Scifi Spritesheet.png"))
door_orig_img = pygame.transform.scale(door_img, (60, 60))



doors_animation = []
for i in range(11):
    file_name = "image" + "_" + str(i + 1) + ".png"
    file = pygame.image.load(path.join(doors_animation_dir, file_name))
    file = pygame.transform.scale(file, (60, 60))
    image = file
    image.set_colorkey(BLACK)
    doors_animation.append(image)

class Door(pygame.sprite.Sprite):
    def __init__(self,x,y, players):
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


    def animated(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(doors_animation):
                self.kill()
            else:
                center = self.rect.center
                self.image = doors_animation[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def touch_player(self):
        hit_with_player = pygame.sprite.spritecollide(self, self.players, False, pygame.sprite.collide_circle)
        if len(hit_with_player) > 0:
            self.animated()

    def update(self):
        self.touch_player()
