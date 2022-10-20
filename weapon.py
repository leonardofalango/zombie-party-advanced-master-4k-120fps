import pygame
from random import randint


class Weapon(pygame.sprite.Sprite):
    def __init__(self, resolution):
        super().__init__()
        # Não tem hitbox

        self.__width = resolution[0] / 50
        self.__height = resolution[1] / 50

        self.posx = randint(0, resolution[0])
        self.posy = randint(0, resolution[1])

        self.image = pygame.Surface([self.__width, self.__height])
        self.image.fill((0, 0, 255))

        self.rect = self.image.get_rect()


