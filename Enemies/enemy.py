from os import listdir

import pygame
import random as rd

# @abstract_class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, resolution, hp, atk, size, vel):
        super().__init__()
        self.__width = size[0]
        self.__height = size[1]
        self.__resolution = resolution
        
        self.hp = hp
        self.atk = atk

        self.alive = 1

        self.image = pygame.Surface([self.__width, self.__height])
        self.sprites = []
        # self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()

        self.rect.x = rd.randint(0, resolution[0] - self.rect.width)
        self.rect.y = rd.randint(0, resolution[1] - self.rect.height)

        self.__vel = vel
        self.index = 0
        self.pos = 'front'
        self.dead = 0

        # self.rect.x = rd.randint(0 - resolution[0] * 0.3, resolution[0] + resolution[0] * 0.3)
        # self.rect.y = rd.randint(0 - resolution[1] * 0.3, resolution[1] + resolution[1] * 0.3)
        # print(self.rect.x, self.rect.y)
    
    def is_alive(self, player):
        if self.hp <= 0 or (
                self.rect.x < -10 or
                self.rect.x > self.__resolution[0] + self.rect.width or
                self.rect.y < -10 or
                self.rect.y > (self.__resolution[1] + self.rect.height)):
            self.alive = 0
            if self.dead == len(self.sprites[2]) -1:
                player.money += 1
                self.kill()

    def walk(self, player):
        if self.alive == 1:
            destx = player.rect.x
            desty = player.rect.y
            if (desty < self.rect.y): self.pos = 'front'
            else: self.pos = 'back'
            # print(self.rect.x, self.rect.y,"|",destx, desty)
            if (destx < self.rect.x):
                self.rect.x -= self.__vel
            elif (destx > self.rect.x):
                self.rect.x += self.__vel

            if (desty < self.rect.y):
                self.rect.y -= self.__vel
            else:
                self.rect.y += self.__vel
    
    def damage(self, player):
        self.hp -= player.atk
        

    def create_sprites(self, path, frame_skip):
        dir = listdir(path)
        front = []
        back = []
        dead = []

        for frontback in listdir(path + '/' + dir[0]):
            for i in range(frame_skip):
                back.append(pygame.image.load(path + "/" + dir[0] + '/' + frontback))
        
        esc = rd.choice(listdir(path + '/' + dir[1]))
        for frontback in listdir(path + '/' + dir[1] + '/' + esc):
            for i in range(frame_skip):
                dead.append(pygame.image.load(path + "/" + dir[1] + "/" + esc + "/" + frontback))

        for frontback in listdir(path + '/' + dir[2]):
            for i in range(frame_skip):
                front.append(pygame.image.load(path + "/" + dir[2] + '/' + frontback))

        self.sprites.append(front)
        self.sprites.append(back)
        self.sprites.append(dead)


    def att(self, player):
        self.is_alive(player)
        if self.alive == 1:
            self.index += 1

            if (self.index >= len(self.sprites[0])):
                self.index = 0
            if (self.pos == 'front'):
                return self.sprites[1][self.index]
            else:
                return self.sprites[0][self.index]
        x = self.sprites[2][self.dead]
        self.dead +=1
        return x

            

         