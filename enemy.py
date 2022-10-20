from abc import abstractclassmethod
import pygame
import random as rd

# @abstract_class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, resolution, hp, atk, width, height):
        super().__init__()
        self.__width = width
        self.__height = height
        self.__resolution = resolution
        
        self.__hp = hp
        self.atk = atk

        self.alive = 1
        
        self.image = pygame.Surface([self.__width, self.__height])
        self.image.fill((255,0,0))

        self.rect = self.image.get_rect()
        
        self.rect.x = 50
        self.rect.y = 50

        # self.rect.x = rd.randint(0 - resolution[0] * 0.3, resolution[0] + resolution[0] * 0.3)
        # self.rect.y = rd.randint(0 - resolution[1] * 0.3, resolution[1] + resolution[1] * 0.3)
        # print(self.rect.x, self.rect.y)
    
    def is_alive(self):
        if self.__hp <= 0 or self.rect.x < -10 or (
                self.rect.x > self.__resolution[0] + self.rect.width or
                self.rect.y < -10 or
                self.rect.y > (self.__resolution[1] + self.rect.height)):
            
            self.alive = 0
            self.kill()
            # print('dead')
        else: self.alive = 1

    @abstractclassmethod
    def walk(self):
        pass

        
    
    def damage(self, damage):
        self.__hp -= damage
        self.is_alive


