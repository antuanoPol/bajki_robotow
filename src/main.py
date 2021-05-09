import pygame
from statics import *
from explosion import Explosion
from player import Player
from player import Boss
from block import Block
from levels import *
from sand import Sand
from door import Door
from functions import *

# iniclaizacja gry i utworzenie okna
pygame.init()  # inicjalizuje cała bibliotekę
pygame.mixer.init()  # inicjalizuje dzwięki
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bajki robotow")
clock = pygame.time.Clock()
background = pygame.image.load(path.join(img_dir, "background-scifi.png")).convert()

# Inicjalizowanie grafiki


# Dodawanie muzyki
pygame.mixer.music.load(path.join(snd_dir, "CleytonRX - Battle RPG Theme Var.ogg"))
pygame.mixer.music.set_volume(0.3)
explosion_sound =  pygame.mixer.Sound(path.join(snd_dir, "explosion.wav"))


# Inicjalizacja tablicy eksplozji
explosion_anim = {}
explosion_anim["lg"] = []
explosion_anim["sm"] = []
for kierunek in range(9):
    filename = "regularExplosion0{}.png".format(kierunek)
    img = pygame.image.load(path.join(explosions_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim["lg"].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim["sm"].append(img_sm)

# Właczenie mixera
pygame.mixer.music.play(loops=-1)

# Tworzymy grupy, spritów
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
players = pygame.sprite.Group()
blocks = pygame.sprite.Group()
doors = pygame.sprite.Group()
sands = pygame.sprite.Group()
# Tworzymy graczy




# Dodanie obiektow do tablic spritów

# Glowna petla programu
running = True
game_over = True
while running:
    if game_over == True:
        show_go_screen()
        game_over = False

        x = 0
        y = 60
        for rou in level1:
            if x == WIDTH:
                x = 0
                y += 60
            for block in rou:
                if block == "B":
                    block = Block(x, y, 1)
                    blocks.add(block)
                    all_sprites.add(block)
                if block == " ":
                    sand = Sand(x, y)
                    all_sprites.add(sand)
                if block == "D":
                    sand = Sand(x, y)
                    all_sprites.add(sand)
                    door = Door(x, y, players)
                    all_sprites.add(door)
                    doors.add(door)
                if block == "W":
                    block = Block(x, y, 2)
                    blocks.add(block)
                    all_sprites.add(block)
                if block == "S":
                    block = Block(x, y, 3)
                    blocks.add(block)
                    all_sprites.add(block)

                x += 60
        player = Player(all_sprites, bullets, blocks, False)
        boss = Boss(all_sprites, bullets, blocks, True)
        all_sprites.add(player)
        all_sprites.add(boss)
        players.add(player)
        SMERC = 0
        WYGRANA = 0
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()

    hits_player = pygame.sprite.spritecollide(player, bullets, True)
    for hit_player in hits_player:
        boss.kill()
        player.kill()
        death_explosion = Explosion(hit_player.rect.center, "lg", explosion_anim)
        explosion_sound.play()
        all_sprites.add(death_explosion)
        SMERC = SMERC + 1

    hits_boss = pygame.sprite.spritecollide(boss, bullets, True)
    for hit_boss in hits_boss:
        player.kill()
        boss.kill()
        death_explosion = Explosion(hit_boss.rect.center, "lg", explosion_anim)
        explosion_sound.play()
        all_sprites.add(death_explosion)
        WYGRANA = WYGRANA +1

    if SMERC == 1 or SMERC > 1 and not death_explosion.alive():
        game_over = True


    if WYGRANA == 1 and not death_explosion.alive():
        show_win_screen()
        game_over = True

    hit_walls = pygame.sprite.groupcollide(bullets, blocks, True, False)
    hit_walls2 = pygame.sprite.groupcollide(bullets, doors, True, False)

pygame.quit()
