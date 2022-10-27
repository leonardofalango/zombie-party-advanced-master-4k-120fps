from abc import abstractclassmethod
import pygame
# from random import randint

# @abstractclass
class Weapon(pygame.sprite.Sprite):
    def __init__(self, resolution, player, firerate):
        super(Weapon, self).__init__()

        self.__width = 5
        self.__height = 5

        self.image = pygame.Surface([self.__width, self.__height])
        self.image.fill((0, 0, 255))

        self.rect = self.image.get_rect()

        self.rect.x = player.rect.x
        self.rect.y = player.rect.y

        self.canfire = False;
        self.firerate = firerate

    
    def att(self, player):
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
    
    # @abstractclassmethod
    def shoot(self, playerx, playery, x, y):
        pass



