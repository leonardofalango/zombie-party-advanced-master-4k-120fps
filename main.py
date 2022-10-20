from player import Player
from normal_zombie import Normal_zombie
from Tank_zombie import Tank_zombie
from flying_zombie import Flying_zombie


import pygame
import sys
import random as rd

width, heigth = 1200, 800
resolution = (width, heigth)
pygame.init()

pygame.display.set_caption('ZOMB.IO')

surface = pygame.display.set_mode(resolution)
player = Player(resolution, None)

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
player.rect.x = player.posx
player.rect.y = player.posy

all_enemies = pygame.sprite.Group()

flying_zombies = pygame.sprite.Group()
tank_zombies = pygame.sprite.Group()
normal_zombies = pygame.sprite.Group()

fundo = pygame.image.load("Centro RPG Maker.png")
#window.blit(fundo, (8, 8))

for i in range(5):
    enemy = Flying_zombie(resolution)
    all_sprites.add(enemy)
    all_enemies.add(enemy)
    flying_zombies.add(enemy)

for i in range(5):
    enemy = Tank_zombie(resolution)
    all_sprites.add(enemy)
    all_enemies.add(enemy)
    flying_zombies.add(enemy)

for i in range(5):
    enemy = Normal_zombie(resolution)
    all_sprites.add(enemy)
    all_enemies.add(enemy)
    flying_zombies.add(enemy)

while 1:    
    clock.tick(60)
    player.update()
    surface.fill((0,0,0))
    all_sprites.draw(surface)


    pressed = pygame.key.get_pressed()
    
    
    if pressed[pygame.K_UP] or pressed[pygame.K_w]:
        player.walk('up')

    if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
        player.walk('down')

    if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
        player.walk('left')

    if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
        player.walk('right')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    for inimigo in flying_zombies:
        inimigo.walk()
        if inimigo.is_alive() == 0:
            pass

    for inimigo in tank_zombies:
        inimigo.walk()
        if inimigo.is_alive() == 0:
            pass

    for inimigo in normal_zombies:
        inimigo.walk()
        if inimigo.is_alive() == 0:
            pass

    if len(all_enemies) < 5:
        # print('spawn')
        enemy = Flying_zombie(resolution)
        all_sprites.add(enemy)
        all_enemies.add(enemy)
        flying_zombies.add(enemy)

    if len(all_enemies) < 5:
        # print('spawn')
        enemy = Tank_zombie(resolution)
        all_sprites.add(enemy)
        all_enemies.add(enemy)
        flying_zombies.add(enemy)

    if len(all_enemies) < 5:
        # print('spawn')
        enemy = Normal_zombie(resolution)
        all_sprites.add(enemy)
        all_enemies.add(enemy)
        normal_zombie.add(enemy)

    pygame.display.update()

