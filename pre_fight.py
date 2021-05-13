#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

from statics import *


class PreFight(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 60
        self.height = 40
        self.image_org = pygame.image.load(path.join(terminal_dir, "terminal.png"))
        self.image = pygame.transform.scale(self.image_org, (0, 0))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 15
        self.frame = 0
        self.font = pygame.font.SysFont("Arial", 24)
        self.initialized = False
        self.closed = False
        self._layer = 5

    def update(self):
        if not self.initialized:
            return
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate and self.frame < 14:
            self.last_update = now
            self.frame += 1

        self.image = pygame.transform.scale(self.image_org, (self.width * self.frame, self.height * self.frame))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.image.set_colorkey(WHITE)

        if self.frame == 14:
            self.draw_info()
        self.check_key()

    def draw_info(self):
        self.image.blit(self.font.render(u"Mały, nędzny Robociku! ", 1, WHITE), [50, 100])
        self.image.blit(self.font.render(u"Wykazałeś się wiedzą, ale...", 1, WHITE), [50, 130])

        self.image.blit(self.font.render(u"wiedza to nie wszystko, czasem w bezmiarze przestrzeni liczy", 1, WHITE),
                        [50, 160])
        self.image.blit(self.font.render(u"się tylko brutalna siła!", 1, WHITE), [50, 190])
        self.image.blit(self.font.render(u"Zobaczymy na co Cię stać!", 1, WHITE), [50, 220])
        self.image.blit(self.font.render(u"Gotowy?  [ENTER]", 1, WHITE), [50, 330])

    def check_key(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RETURN]:
            self.closed = True
