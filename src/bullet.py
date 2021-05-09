import pygame
from src.statics import *
from src.functions import rotate

bullet_img = pygame.image.load(path.join(img_dir, "laserRed05.png"))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, parent, boss):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img.convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = parent.rect.centery
        self.rect.centerx = parent.rect.centerx
        self.speed = 25
        self.direction = parent.bullet_direction
        if self.direction == LEFT or self.direction == RIGHT:
            self.image = rotate(90, self.image)
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.centerx = parent.rect.centerx
            self.rect.bottom = parent.rect.centery
        if boss == True:
            if self.direction == UP:
                self.rect.centerx = parent.rect.centerx - 20
        if self.direction == UP:
            self.rect.bottom = parent.rect.top - 20
        if boss == True:
            if self.direction == DOWN:
                self.rect.centerx += 20
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
