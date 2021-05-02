import pygame
from statics import *
from functions import calculate_direction
from bullet import Bullet

player_img = pygame.image.load(path.join(img_dir, "guardbot3.png"))
player_orig_img = player_img = pygame.transform.scale(player_img, (50, 50))

class Player(pygame.sprite.Sprite):
    def __init__(self,  all_sprites, bullets, blocks):
        pygame.sprite.Sprite.__init__(self)
        self.blocks = blocks
        self.all_sprites = all_sprites
        self.bullets = bullets
        self.image = player_img.convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 100
        self.rect.bottom = HEIGHT - 70
        self.last_shoot = pygame.time.get_ticks()
        self.shoot_delay = 350
        self.direction = None
        self.bullet_direction = UP

    def update(self):
        keystate = pygame.key.get_pressed()
        self.set_direction(keystate)
        self.move()
        self.detect_colison()
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.direction = None

    def set_direction(self, keystate):
        direction = calculate_direction(keystate)
        if direction is not None:
            self.direction = direction
            self.bullet_direction = self.direction

    def move(self):
        self.speedx = 0
        self.speedy = 0
        if self.direction == LEFT:
            self.speedx = -8
        if self.direction == RIGHT:
            self.speedx = 8
        if self.direction == UP:
            self.speedy = -8
        if self.direction == DOWN:
            self.speedy = 8

        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top <= 0:
            self.rect.top = 0

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_delay:
            bullet = Bullet(self)
            self.all_sprites.add(bullet)
            self.bullets.add(bullet)
            # shoot_sound.play()
            self.last_shoot = now

    def detect_colison(self):
        walls_you_hit = pygame.sprite.spritecollide(self, self.blocks, False)
        if len(walls_you_hit) > 0:
            if self.direction == LEFT and walls_you_hit[0].rect.left < self.rect.centerx:
                self.rect.left = walls_you_hit[0].rect.right + 5
            if self.direction == RIGHT and walls_you_hit[0].rect.right > self.rect.centerx:
                self.rect.right = walls_you_hit[0].rect.left - 5
            if self.direction == UP and walls_you_hit[0].rect.bottom < self.rect.centery:
                self.rect.top = walls_you_hit[0].rect.bottom + 5
            if self.direction == DOWN and walls_you_hit[0].rect.top > self.rect.centery:
                self.rect.bottom = walls_you_hit[0].rect.top - 5
