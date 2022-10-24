from abc import abstractclassmethod
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
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()

        self.rect.x = rd.randint(0, resolution[0] - self.rect.width)
        self.rect.y = rd.randint(0, resolution[1] - self.rect.height)

        self.__vel = vel

        # self.rect.x = rd.randint(0 - resolution[0] * 0.3, resolution[0] + resolution[0] * 0.3)
        # self.rect.y = rd.randint(0 - resolution[1] * 0.3, resolution[1] + resolution[1] * 0.3)
        # print(self.rect.x, self.rect.y)
    
    def is_alive(self):
        if self.hp <= 0 or (
                self.rect.x < -10 or
                self.rect.x > self.__resolution[0] + self.rect.width or
                self.rect.y < -10 or
                self.rect.y > (self.__resolution[1] + self.rect.height)):
            self.alive = 0
            self.kill()
            print('dead')

    def walk(self, player):
        destx = player.rect.x
        desty = player.rect.y
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
        print(self.hp)
        self.is_alive()


