from src.block import Block
from src.door import Door
from src.explosion import Explosion
from src.functions import *
from src.levels import *
from src.player import Boss
from src.player import Player
from src.sand import Sand

# iniclaizacja gry i utworzenie okna
pygame.init()  # inicjalizuje cała bibliotekę
pygame.mixer.init()  # inicjalizuje dzwięki
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bajki robotow")
clock = pygame.time.Clock()

player_mini_image = None
boss_mini_image = None


def get_player_mini_image(image):
    global player_mini_image
    if player_mini_image is None:
        player_mini_image = pygame.transform.scale(image, (40, 40))
    return player_mini_image


def get_boss_mini_image(image):
    global boss_mini_image
    if boss_mini_image is None:
        boss_mini_image = pygame.transform.scale(image, (40, 40))
    return boss_mini_image


# Inicjalizowanie grafiki
background = pygame.image.load(path.join(img_dir, "background-scifi.png")).convert()

# Dodawanie muzyki
pygame.mixer.music.load(path.join(snd_dir, "CleytonRX - Battle RPG Theme Var.ogg"))
pygame.mixer.music.set_volume(0.3)
explosion_sound = pygame.mixer.Sound(path.join(snd_dir, "explosion.wav"))

# Inicjalizacja tablicy eksplozji
explosion_anim = {}
explosion_anim["lg"] = []
explosion_anim["sm"] = []
explosion_anim["player"] = []
for kierunek in range(9):
    filename = "regularExplosion0{}.png".format(kierunek)
    img = pygame.image.load(path.join(explosions_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (120, 120))
    explosion_anim["lg"].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim["sm"].append(img_sm)
    filename = "sonicExplosion0{}.png".format(kierunek)
    img = pygame.image.load(path.join(explosions_dir, filename)).convert()
    img.set_colorkey(BLACK)
    explosion_anim["player"].append(img)

# Właczenie mixera
pygame.mixer.music.play(loops=-1)

# Tworzymy grupy, spritów
all_sprites = pygame.sprite.LayeredUpdates()
bullets = pygame.sprite.LayeredUpdates()
players = pygame.sprite.LayeredUpdates()
blocks = pygame.sprite.LayeredUpdates()
inner_blocks = pygame.sprite.LayeredUpdates()
doors = pygame.sprite.LayeredUpdates()
sands = pygame.sprite.LayeredUpdates()
questions = pygame.sprite.LayeredUpdates()

# Glowna petla programu
boss_fight = False
running = True
game_over = True
while running:
    if game_over:
        show_go_screen()
        game_over = False
        question_counter = 0
        x = 0
        y = 60
        for row in level1:
            if x == WIDTH:
                x = 0
                y += 60
            for block_name in row:
                if block_name == "B" or block_name == "F":
                    block = Block(x, y, 1)
                    blocks.add(block)
                    all_sprites.add(block)
                    sand = Sand(x, y)
                    all_sprites.add(sand)
                    if block_name != "F":
                        inner_blocks.add(block)
                if block_name == " ":
                    sand = Sand(x, y)
                    all_sprites.add(sand)
                if block_name == "D" or block_name == "E":
                    exit_door = False
                    if block_name == "E":
                        exit_door = True
                    sand = Sand(x, y)
                    all_sprites.add(sand)
                    door = Door(x, y, players, question_counter, exit_door)
                    question_counter += 1
                    all_sprites.add(door)
                    questions.add(door.question)
                    all_sprites.add(door.question)
                    doors.add(door)
                if block_name == "W":
                    block = Block(x, y, 2)
                    blocks.add(block)
                    all_sprites.add(block)
                if block_name == "S":
                    block = Block(x, y, 3)
                    blocks.add(block)
                    all_sprites.add(block)

                x += 60

        player = Player(all_sprites, bullets, blocks, False)
        all_sprites.add(player)
        players.add(player)
        death = False
        win = False
        colission = False
        boss_fight = False

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for player in players:
        player.can_move = not question_asked(questions)

    if exit_door_opened(doors) and not boss_fight:
        for block in inner_blocks:
            block.kill()
        for door in doors:
            door.kill()
        boss = Boss(all_sprites, bullets, blocks, True, player)
        all_sprites.add(boss)
        boss_fight = True
    all_sprites.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)

    if boss_fight:
        draw_lives(screen, 80, 10, player.lives_player, get_player_mini_image(player.def_image))
        draw_lives(screen, 1630, 10, boss.lives_boss, get_boss_mini_image(boss.def_image))
        hits_player = pygame.sprite.spritecollide(player, bullets, True)
        for hit_player in hits_player:
            player.lives_player = player.lives_player - 1
            explosion_sound.play()
            if player.lives_player == 0 or player.lives_player < 0:
                death_explosion = Explosion(player.rect.center, "player", explosion_anim)
                all_sprites.add(death_explosion)
                player.kill()
                boss.kill()
                death = True
            else:
                death_explosion_sm = Explosion(player.rect.center, "sm", explosion_anim)
                all_sprites.add(death_explosion_sm)

        hits_boss = pygame.sprite.spritecollide(boss, bullets, True)
        for hit_boss in hits_boss:
            boss.lives_boss = boss.lives_boss - 1
            explosion_sound.play()
            if boss.lives_boss == 0 or boss.lives_boss < 0:
                death_explosion_boss = Explosion(boss.rect.center, "lg", explosion_anim)
                boss.kill()
                player.kill()
                win = True
            else:
                death_explosion_boss = Explosion(boss.rect.center, "sm", explosion_anim)
            all_sprites.add(death_explosion_boss)

        hits_boss_player = pygame.sprite.spritecollide(boss, players, False)
        for hit_boss_player in hits_boss_player:
            player.lives_player = 0
            boss.kill()
            player.kill()
            explosion_sound.play()
            death_explosion_player_hit = Explosion(player.rect.center, "player", explosion_anim)
            all_sprites.add(death_explosion_player_hit)
            colission = True

        if death:
            if not death_explosion.alive():
                show_die_screen()
                game_over = True

        if win:
            if not death_explosion_boss.alive():
                show_win_screen()
                game_over = True

        if colission:
            if not death_explosion_player_hit.alive():
                show_die_screen()
                game_over = True

    pygame.display.flip()
    hit_walls = pygame.sprite.groupcollide(bullets, blocks, True, False)
    hit_walls2 = pygame.sprite.groupcollide(bullets, doors, True, False)
pygame.quit()
