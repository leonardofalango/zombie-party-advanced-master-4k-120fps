from abc import abstractclassmethod
import pygame
from os import listdir
# from random import randint

# @abstractclass
class Weapon(pygame.sprite.Sprite):
    def __init__(self, resolution, player, firerate, width, height):
        super(Weapon, self).__init__()

        self.__width = width
        self.__height = height

        self.image = pygame.Surface([0,0])


        self.rect = self.image.get_rect()

        self.rect.x = player.rect.x
        self.rect.y = player.rect.y

        self.canfire = False;
        self.firerate = firerate

        self.sprite = None
        self.sprites = []
        self.index = 0
        self.esq = False


    def eq(self, player, x,y):
        raio = player.rect.width
        pcentro = player.rect.x, player.rect.y
        
    
    def att(self, player):
        self.angle = -player.angle
        sprites = []
        if self.angle < 90 and self.angle > -90:
            self.rect.x = player.rect.x + 50
            sprites = self.sprites[0]

        else:
            self.rect.x = player.rect.x - 50
            sprites = self.sprites[1]



        self.rect.y = player.rect.y + 60
        if (self.index != 0):
            self.index += 1
        if (self.index >= len(self.sprites[0])):
            self.index = 0

        self.sprite = pygame.transform.scale(sprites[self.index], (self.__width, self.__height))
        rotated_image = pygame.transform.rotate(self.sprite, self.angle)
        new_rect = rotated_image.get_rect(center=self.sprite.get_rect(center=(self.rect.x, self.rect.y)).center)
        self.blit = [rotated_image, new_rect]




    # @abstractclassmethod
    def shoot(self, playerx, playery, x, y):
        self.index += 1

    def create_sprites(self, path, frame_skip):
        sprites = listdir(path)
        x = []
        for file in sprites:
            for i in range(frame_skip):
                x.append(pygame.image.load(path + "/" + file))
        self.sprites.append(x)

        aux = []
        for file in x:
            aux.append(pygame.transform.flip(file, False, True))

        self.sprites.append(aux)
        self.sprite = self.sprites[0][0]


