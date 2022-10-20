from player import Player
from normal_zombie import Normal_zombie
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

enemy = Normal_zombie(resolution)
all_enemies = pygame.sprite.Group()
all_sprites.add(enemy)
all_enemies.add(enemy)

while 1:
    clock.tick(60)
    player.update()
    surface.fill((0, 0, 0))
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

    for i in all_enemies:
        i.walk(player)


    # Tomando dano:
    damages = [s for s in all_enemies if s.rect.collidepoint((player.rect.x, player.rect.y))]
    if len(damages) >= 1:
        for i in all_enemies:
            player.take_damage(i.atk)

    # Atirando / Dando dano
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
            mousex, mousey = pygame.mouse.get_pos()
            player.shoot((mousex,mousey))

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)


