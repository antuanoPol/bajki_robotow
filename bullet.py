#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from statics import *
from functions import rotate

bullet_img = pygame.image.load(path.join(img_dir, "laserRed05.png"))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, parent, boss):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img.convert()
        if boss:
            self.image = pygame.transform.scale(bullet_img, (20, 40))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = parent.rect.centery
        self.rect.centerx = parent.rect.centerx
        self.speed = 25
        self.direction = parent.direction
        if parent.direction == None:
            self.direction = UP
        if self.direction == LEFT or self.direction == RIGHT:
            self.image = rotate(90, self.image)
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.centerx = parent.rect.centerx
            self.rect.bottom = parent.rect.centery
        if self.direction == UP:
            self.rect.bottom = parent.rect.top - 20
        if self.direction == DOWN:
            self.rect.bottom = parent.rect.bottom + 60
        if self.direction == RIGHT:
            self.rect.right = parent.rect.right + 60
        if self.direction == LEFT:
            self.rect.left = parent.rect.left - 60

    def update(self):
        if self.direction == LEFT:
            self.rect.x -= self.speed
        if self.direction == UP:
            self.rect.y -= self.speed
        if self.direction == DOWN:
            self.rect.y += self.speed
        if self.direction == RIGHT:
            self.rect.x += self.speed

        if self.rect.left < 0 or self.rect.right > WIDTH or self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.kill()
