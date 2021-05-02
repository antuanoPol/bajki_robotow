import pygame
from statics import *

block_img = pygame.image.load(path.join(img_dir, "metal.png"))
block_orig_img = pygame.transform.scale(block_img, (60, 60))

class Block (pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = block_orig_img.convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.bottom = y

