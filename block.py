#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

from statics import *

block_img = pygame.image.load(path.join(img_dir, "metal.png"))
block_img_warning = pygame.image.load(path.join(img_dir, "metalCenterWarning.png"))
block_img_warning_sticker = pygame.image.load(path.join(img_dir, "metalCenterSticker.png"))
block_orig_img = pygame.transform.scale(block_img, (60, 60))


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        self._layer = 2
        pygame.sprite.Sprite.__init__(self)
        if img == 1:
            self.image = block_orig_img.convert()
        if img == 2:
            self.image = block_img_warning.convert()
        if img == 3:
            self.image = block_img_warning_sticker.convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.bottom = y
