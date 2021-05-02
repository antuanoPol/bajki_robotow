import pygame
from statics import *
from explosion import Explosion
from player import Player
from block import Block
from levels import *

# iniclaizacja gry i utworzenie okna
pygame.init()  # inicjalizuje cała bibliotekę
pygame.mixer.init()  # inicjalizuje dzwięki
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bajki robotow")
clock = pygame.time.Clock()

# Inicjalizowanie grafiki
# background = pygame.image.load(path.join(img_dir, "hexagonal_background_1080p.png")).convert()
# background_rect = background.get_rect()

# Dodawanie muzyki
pygame.mixer.music.load(path.join(snd_dir, "CleytonRX - Battle RPG Theme Var.ogg"))
pygame.mixer.music.set_volume(0.4)

# Inicjalizacja tablicy eksplozji
explosion_anim = {}
explosion_anim["lg"] = []
explosion_anim["sm"] = []
for i in range(9):
    filename = "regularExplosion0{}.png".format(i)
    img = pygame.image.load(path.join(explosions_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim["lg"].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim["sm"].append(img_sm)

# Właczenie mixera
# pygame.mixer.music.play(loops=-1)

# Tworzymy grupy, spritów
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
players = pygame.sprite.Group()
blocks = pygame.sprite.Group()

# Tworzymy graczy
player = Player(True, True, all_sprites, bullets)
player_enemy = Player(False, False, all_sprites, bullets)

x = 0
y = 60
for rou in level1:
    if x == WIDTH:
        x = 0
        y += 60
    for block in rou:
        if block == "B":
            block = Block(x, y)
            blocks.add(block)
            all_sprites.add(block)
        x += 60



# Dodanie obiektow do tablic spritów
# all_sprites.add(player)
# all_sprites.add(player_enemy)
# players.add(player_enemy)
# players.add(player)

# Glowna petla programu
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill(BLACK)
    # screen.blit(background, background_rect)
    all_sprites.draw(screen)
    pygame.display.flip()

    hit_players = pygame.sprite.groupcollide(players, bullets, True, True)
    for hit_player in hit_players:
        death_explosion = Explosion(hit_player.rect.center, "lg", explosion_anim)
        all_sprites.add(death_explosion)
        if len(hit_players) > 0:
            PUNKTY = + 1

pygame.quit()
