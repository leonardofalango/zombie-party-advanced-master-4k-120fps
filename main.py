from player import Player
from normal_zombie import Normal_zombie
from flying_zombie import Flying_zombie
from weapon import Weapon

import Menu
import Shop

import pygame
import sys
import random as rd

width, heigth = 1200, 800
resolution = (width, heigth)

def mainGame():
    pygame.display.set_caption('ZOMB.IO')

    surface = pygame.display.set_mode(resolution)
    player = Player(resolution, None)

    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    player.rect.x = player.posx
    player.rect.y = player.posy

    all_enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    weapon = Weapon(resolution)
    all_sprites.add(weapon)

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

        if pygame.sprite.collide_mask(player, weapon):
            weapon.kill()
            player.atk += 20

        collide = pygame.sprite.spritecollideany(player, all_enemies)
        if collide:
            player.take_damage(collide.atk)


        collide = pygame.sprite.groupcollide(all_enemies, bullets, False, True)
        if (collide):
            for z in collide:
                z.damage(player)

        for e in all_enemies:
            e.walk(player)
            if (pygame.sprite.spritecollideany(e, bullets)):
                e.damage(player)

        for bala in bullets:
            bala.shoot()
        # print(len(all_sprites))
        # print(len(all_sprites))
        while (len(all_enemies) < 15):
            num =   rd.randint(0,100)
            if num > 75:
                e = Flying_zombie(resolution)
                all_sprites.add(e)
                all_enemies.add(e)
            else:
                e = Normal_zombie(resolution)
                all_sprites.add(e)
                all_enemies.add(e)


        # Tomando dano:

        # Atirando / Dando dano
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.K_SPACE:
                bala = player.shoot(pygame.mouse.get_pos())
                all_sprites.add(bala)
                bullets.add(bala)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

pygame.init()
screen = pygame.display.set_mode((750, 500))
Menu.menu(screen)
mainGame()

