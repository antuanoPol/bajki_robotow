import pygame

from bullet import Bullet
from functions import calculate_direction
from statics import *

PLAYER_POSITION_X = 340
PLAYER_POSITION_Y = HEIGHT - 240

player_img = pygame.image.load(path.join(img_dir, "guardbot3.png"))
player_orig_img = player_img = pygame.transform.scale(player_img, (50, 50))


boss_animation = {}
boss_animation[LEFT] = []
boss_animation[DOWN] = []
boss_animation[UP] = []
boss_animation[RIGHT] = []

player_animation = {}
player_animation[LEFT] = []
player_animation[DOWN] = []
player_animation[UP] = []
player_animation[RIGHT] = []

for direction in [LEFT, RIGHT, UP, DOWN]:
    for i in range(4):
        file_name = direction.lower() + "_" + str(i + 1) + ".png"
        file = pygame.image.load(path.join(robot_animation_dir, file_name))
        file = pygame.transform.scale(file, (50, 50))
        image = file
        image.set_colorkey(BLACK)
        player_animation[direction].append(image)

    for i in range(8):
        file_name = direction.lower() + "_" + str(i + 1) + ".png"
        file = pygame.image.load(path.join(boss_animation_dir, file_name))
        file = pygame.transform.scale(file, (110, 110))
        image = file
        image.set_colorkey(BLACK)
        boss_animation[direction].append(image)


class Player(pygame.sprite.Sprite):
    def __init__(self, all_sprites, bullets, blocks):
        pygame.sprite.Sprite.__init__(self)
        self.def_image = player_animation[UP][0]
        self.image = self.def_image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.position()
        self.blocks = blocks
        self.all_sprites = all_sprites
        self.bullets = bullets
        self.last_shoot = pygame.time.get_ticks()
        self.shoot_delay = 350
        self.direction = None
        self.bullet_direction = UP
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def position(self):
        self.rect.centerx = PLAYER_POSITION_X
        self.rect.bottom = PLAYER_POSITION_Y

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
            self.speedx = -6
        if self.direction == RIGHT:
            self.speedx = 6
        if self.direction == UP:
            self.speedy = -6
        if self.direction == DOWN:
            self.speedy = 6
        self.animated()

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
            bullet = Bullet(self, True)
            self.all_sprites.add(bullet)
            self.bullets.add(bullet)
            # shoot_sound.play()
            self.last_shoot = now

    def detect_colison(self):
        walls_you_hit = pygame.sprite.spritecollide(self, self.blocks, False)
        if len(walls_you_hit) > 0:
            if self.direction == LEFT and walls_you_hit[0].rect.left < self.rect.centerx:
                self.rect.left = walls_you_hit[0].rect.right + 4
            if self.direction == RIGHT and walls_you_hit[0].rect.right > self.rect.centerx:
                self.rect.right = walls_you_hit[0].rect.left - 4
            if self.direction == UP and walls_you_hit[0].rect.bottom < self.rect.centery:
                self.rect.top = walls_you_hit[0].rect.bottom + 4
            if self.direction == DOWN and walls_you_hit[0].rect.top > self.rect.centery:
                self.rect.bottom = walls_you_hit[0].rect.top - 4

    def animated(self):
        now = pygame.time.get_ticks()
        if self.direction == None:
            self.image = self.def_image
            return
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
        if self.frame == 3:
            self.frame = 0
        else:
            center = self.rect.center
            self.image = player_animation[self.direction][self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = center


class Boss(Player):
    def __init__(self, all_sprites, bullets, blocks):
        super().__init__(all_sprites, bullets, blocks)
        self.def_image = boss_animation[UP][0]

    def position(self):
        self.rect.centerx = 1440
        self.rect.bottom = 400


    def animated(self):
        now = pygame.time.get_ticks()
        if self.direction == None:
            self.image = self.def_image
            return
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
        if self.frame == 3:
            self.frame = 0
        else:
            center = self.rect.center
            self.image = boss_animation[self.direction][self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = center

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_delay:
            bullet = Bullet(self, True)
            self.all_sprites.add(bullet)
            self.bullets.add(bullet)
            # shoot_sound.play()
            self.last_shoot = now
