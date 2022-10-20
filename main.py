from player import Player
from enemy import Normal_zombie, Flying_zombie

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
normal_zombie = Normal_zombie(resolution)
all_sprites.add(normal_zombie)
all_enemies.add(normal_zombie)

flying_zombies = pygame.sprite.Group()
for i in range(12):
    enemy = Flying_zombie(resolution)
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
    
    
    

    for inimigo in flying_zombies:
        inimigo.walk()
        if inimigo.is_alive() == 0:
            all_sprites.remove(inimigo)
            flying_zombies.remove(inimigo)
            all_sprites.remove(inimigo)

    if len(all_enemies) < 4:
        print('spawn')
        enemy = Flying_zombie(resolution)
        all_sprites.add(enemy)
        all_enemies.add(enemy)
        flying_zombies.add(enemy)
    
    
    

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mousex, mousey = pygame.mouse.get_pos()
            clicked_sprites = [s for s in all_enemies if s.rect.collidepoint((mousex, mousey))]
            # print(clicked_sprites)
            for died_enemy in player.shoot(mousex, mousey, clicked_sprites):
                all_sprites.remove(died_enemy)
                all_enemies.remove(died_enemy)

            
        
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)


