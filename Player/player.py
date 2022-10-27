import pygame
from Player.weapon import shotgun
from math import atan2, pi
from os import listdir


class Player (pygame.sprite.Sprite):
    def __init__(self, resolution, skin) -> None:
        super().__init__()

        self.skin = skin
        self.skip_frames = 6
    
        self.__width = (resolution[0]/20 * 0.75) - 30
        self.__height = resolution[1]/20 * 0.75
        self.__walk_distance = max(resolution) / 50 * 0.3

        self.posx = resolution[0]/2 - self.__width
        self.posy = resolution[1]/2 - self.__height
        
        self.image = pygame.Surface([self.__width, self.__height])
        self.image.fill((0, 255, 0))

        self.rect = self.image.get_rect()
        
        self.weapon = shotgun.Shotgun(resolution, self)
        self.atk = 20
        self.__armour = 0
        self.hp = 1000
        self.__alive = 1

        self.facing = None
        self.ant = self.facing
        self.index = 0

        self.iddle_images = {}


        self.create_images()


    def walk(self, direction):
        if direction == 'up':
            self.rect.y -= self.__walk_distance
        
        if direction == 'down':
            self.rect.y += self.__walk_distance

        if direction == 'left':
            self.rect.x -= self.__walk_distance
        
        if direction == 'right':
            self.rect.x += self.__walk_distance
        
        self.weapon.att(self)
    
    def shoot(self, pos):
        return self.weapon.shoot(pos)
        
    
    def take_damage(self, value):
        value = value * (1-self.__armour)
        self.hp -= value
        if self.hp <= 0:
            self.kill()
            self.__alive = 0
    
    def att_facing(self, mouse_pos):
        angle = atan2(mouse_pos[1] - self.rect.y, mouse_pos[0] - self.rect.x) * (180/pi)

        if -45 < angle < 0:
            self.facing = 'up-right'
        elif -135 < angle <= -45:
            self.facing = 'up-straight'
        elif -180 < angle <= -135:
            self.facing = 'up-left'


        elif 135 < angle <= 180:
            self.facing = 'down-left'
        elif 45 < angle <= 135:
            self.facing = 'down-straight'
        elif 0 <= angle <= 45:
            self.facing = 'down-right'

        print(self.facing)

    def get_sprite(self):
        if (self.facing == self.ant):
            self.index += 1
        else:
            self.index = 0
            self.ant = self.facing
        if self.index >= len(self.iddle_images[self.facing]):
            self.index = 0
        return self.iddle_images[self.facing][self.index]



    def create_images(self):
        self.iddle45, self.iddle = listdir(self.skin + 'Front/')
        self.iddle_images_down = {'down': [x for x in listdir(self.skin + 'Front/' + self.iddle)],
                                  'down45': [x for x in listdir(self.skin + 'Front/' + self.iddle45)]}
        aux = []
        for x in self.iddle_images_down['down']:
            for j in range(self.skip_frames):
                aux.append(pygame.image.load(self.skin + 'Front/' + self.iddle + "/" + x))

        self.iddle_images['down-straight'] = aux

        aux = []

        for x in self.iddle_images_down['down45']:
            for j in range(self.skip_frames):
                aux.append(pygame.image.load(self.skin + 'Front/' + self.iddle45 + "/" + x))

        self.iddle_images['down-right'] = aux

        aux = []
        for x in self.iddle_images['down-right']:
            aux.append(pygame.transform.flip(x, True, False))
        self.iddle_images['down-left'] = aux

        self.backiddle45, self.backiddle = listdir(self.skin + 'Down/')
        self.iddle_images_back = {'back': [x for x in listdir(self.skin + 'Down/' + self.backiddle)],
                                  'back45': [x for x in listdir(self.skin + 'Down/' + self.backiddle45)]}

        aux = []
        for x in self.iddle_images_back['back']:
            for j in range(self.skip_frames):
                aux.append(pygame.image.load(self.skin + 'Down/' + self.backiddle + "/" + x))

        self.iddle_images['up-straight'] = aux

        aux = []
        for x in self.iddle_images_back['back45']:
            for j in range(self.skip_frames):
                aux.append(pygame.image.load(self.skin + 'Down/' + self.backiddle45 + "/" + x))

        self.iddle_images['up-right'] = aux

        aux = []
        for x in self.iddle_images['up-right']:
            aux.append(pygame.transform.flip(x, True, False))
        self.iddle_images['up-left'] = aux



