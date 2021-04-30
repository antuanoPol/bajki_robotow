import pygame
from statics import *
from bullet import Bullet

player_img = pygame.image.load(path.join(img_dir, "guardbot3.png"))
player_orig_img = player_img = pygame.transform.scale(player_img, (120, 120))

class Player(pygame.sprite.Sprite):
    def __init__(self, main_player, respawn, all_sprites, bullets):
        pygame.sprite.Sprite.__init__(self)
        self.all_sprites = all_sprites
        self.bullets = bullets
        self.main_player = main_player
        self.image = player_img.convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        if respawn == True:
            self.rect.centerx = WIDTH
            self.rect.bottom = HEIGHT
        else:
            self.rect.centerx = 0
            self.rect.bottom = 0
        self.last_shoot = pygame.time.get_ticks()
        self.shoot_delay = 350
        self.direction = None

    def update(self):
        self.setDirection()
        self.move()
        if self.main_player:
            if self.keystate[pygame.K_SPACE]:
                self.shoot()
        else:
            if self.keystate[pygame.K_LSHIFT]:
                self.shoot()
        self.direction = None

    def setDirection(self):
        self.keystate = pygame.key.get_pressed()
        if self.main_player:
            if self.keystate[pygame.K_LEFT]:
                self.direction = LEFT
            if self.keystate[pygame.K_RIGHT]:
                self.direction = RIGHT
            if self.keystate[pygame.K_UP]:
                self.direction = UP
            if self.keystate[pygame.K_DOWN]:
                self.direction = DOWN
        else:
            if self.keystate[pygame.K_a]:
                self.direction = LEFT
            if self.keystate[pygame.K_d]:
                self.direction = RIGHT
            if self.keystate[pygame.K_w]:
                self.direction = UP
            if self.keystate[pygame.K_s]:
                self.direction = DOWN

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
