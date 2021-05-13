#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from statics import *

sand_img = pygame.image.load(path.join(img_dir, "sand.png"))
sand_orig_img = pygame.transform.scale(sand_img, (60, 60))

class Sand(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = sand_orig_img.convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.bottom = y
