from cgitb import reset
from email.headerregistry import Group
from telnetlib import GA
from turtle import goto
from Enemies.flying_zombie import Flying_zombie
from Enemies.normal_zombie import Normal_zombie
from Player import player as player1

import Menu
import pygame
import sys
import random as rd
from PIL import Image

class Game:
    def pil_to_game(img):
        data = img.tobytes("raw", "RGBA")
        return pygame.image.fromstring(data, img.size, "RGBA")

    def get_enemy_cap(self, t):
        return 4 + (t / 100)

    def between(self, value, min, max):
        return value >= min and value < max

    def create_enemy(self, index, resolution):
        if index == 0:
            return Normal_zombie(resolution, self)
        if index == 1:
            return Flying_zombie(resolution, self)

    def spawn(self, values):
        if sum(values) != 100:
            raise Exception()
        
        for i in range(len(values)):
            v = rd.randint(0,101)
            if self.between(v, 0 if i == 0 else values[i-1], values[i]):
                return self.create_enemy(i, self.resolution)
        return self.create_enemy(0, self.resolution)

    
    def __init__(self) -> None:
        width, heigth = 1200, 800
        self.resolution = (width, heigth)
        self.all_sprites = 0
        self.all_enemies = 0
        
        self.player_group = pygame.sprite.Group()
        

        self.player = player1.Player(self.resolution, 'Sprites/Player/Skin1 - ok/')
        self.player_group.add(self.player)

        self.money = 0
        self.reset()
        self.img = Image.open("Sprites/Maps/Yes.png")
    

    def reset(self):
        self.player.hp = 250
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.player.rect.x = self.player.posx
        self.player.rect.y = self.player.posy

        self.all_enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.timer = 0
        self.tempo_total = 0
        pygame.time.set_timer(pygame.USEREVENT, 10)

        self.all_sprites.add(self.player.weapon)
    
    
    def run(self):
        pygame.init()

        pygame.display.set_caption('ZOMB.IO')

        surface = pygame.display.set_mode(self.resolution)
        clock = pygame.time.Clock()


        #mostrar menu de primeira
        screen = pygame.display.set_mode((750, 500))
        Menu.menu(screen, self.player, self)

        
        while 1:
            if(self.player.hp <= 0):
                pygame.display.set_mode((750, 500))
                Menu.menu(screen, self.player, self)

            pygame.display.set_mode(self.resolution)
            mouse_pos = pygame.mouse.get_pos()
            self.player.att_facing(mouse_pos)
            clock.tick(60)
            self.player.update()
            surface.fill((255,255,255))
            surface.blit(Menu.pil_to_game(self.img.convert("RGBA")), (0,0))
            self.all_sprites.draw(surface)
            self.all_enemies.draw(surface)
            self.player_group.draw(surface)

            # self.player.sprite = pygame.transform.scale(self.player.sprite, (120, 150))

            if 'down' in self.player.facing:
                self.player_group.draw(surface)
                # surface.blit(, (self.player.rect.x, self.player.rect.y))
                surface.blit(self.player.weapon.blit[0], self.player.weapon.blit[1])
            else:
                surface.blit(self.player.weapon.blit[0], self.player.weapon.blit[1])
                self.player_group.draw(surface)

            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_m]:
                screen = pygame.display.set_mode((750, 500))
                Menu.menu(screen, self.player, self.all_sprites, self.all_enemies, self.timer, self.tempo_total)(screen, self.player, self.all_sprites, self.all_enemies, self.timer, self.tempo_total)

            if pressed[pygame.K_UP] or pressed[pygame.K_w]:
                self.player.walk('up')

            if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
                self.player.walk('down')

            if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
                self.player.walk('left')

            if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
                self.player.walk('right')
            self.player.att_sprite()
            
            # if pygame.sprite.collide_mask(self.player, weapon):
            #     weapon.kill()
            #     self.player.atk += 20

            collide = pygame.sprite.spritecollideany(self.player, self.all_enemies)
            if collide:
                self.player.take_damage(collide.atk)


            collide = pygame.sprite.groupcollide(self.all_enemies, self.bullets, False, True)
            if (collide):
                for z in collide:
                    z.damage(self.player)

            for e in self.all_enemies:
                e.walk(self.player)
                if (pygame.sprite.spritecollideany(e.hitbox, self.bullets)):
                    e.damage(self.player)
                    print("certou")

            for bala in self.bullets:
                bala.shoot()
            

            while (len(self.all_enemies) < self.get_enemy_cap(self.tempo_total)):
                e = self.spawn([50, 50])
                self.all_enemies.add(e)
                self.all_sprites.add(e)




            # Tomando dano:

            # Atirando / Dando dano
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.K_SPACE:
                    bala = self.player.shoot(mouse_pos)
                    try:
                        for i in bala:
                            self.all_sprites.add(i)
                            self.bullets.add(i)
                    except:
                        pass

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                if event.type == pygame.USEREVENT:
                    self.timer += 0.01
                    self.tempo_total += 0.01

            if (self.timer >= self.player.weapon.firerate):
                self.timer = 0
                self.player.weapon.canfire = True

game = Game()
game.run()