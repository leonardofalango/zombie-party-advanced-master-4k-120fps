import pygame
from Player.weapon import glock, shotgun, ak47
from math import atan2, pi
from os import listdir


class Player (pygame.sprite.Sprite):
    def __init__(self, resolution, skin) -> None:
        super().__init__()

        self.skin = skin
        self.skip_frames = 6
    
        self.__width = 120
        self.__height = 150
        self.__walk_distance = max(resolution) / 50 * 0.3

        self.posx = resolution[0]/2 - self.__width
        self.posy = resolution[1]/2 - self.__height
        
        self.image = pygame.Surface([self.__width, self.__height])
        # self.image.fill((0, 255, 0))

        self.rect = self.image.get_rect()
        
        self.weapon = ak47.Ak47(resolution, self)
        self.atk = 5
        self.__armour = 0
        self.hp = 1000
        self.__alive = 1

        self.facing = 'down'
        self.animation = 'walk'
        self.ant = self.facing
        self.antanimation = self.animation
        self.index = 0
        self.angle = 0

        self.iddle_images = self.create_images(self.skin + 'Idle/', self.skip_frames)
        self.walking_images = self.create_images(self.skin + 'Walking/', self.skip_frames)
        self.sprite = self.iddle_images['up-right'][0]

        

    def walk(self, direction):
        if direction == 'up':
            self.rect.y -= self.__walk_distance
        
        if direction == 'down':
            self.rect.y += self.__walk_distance

        if direction == 'left':
            self.rect.x -= self.__walk_distance
        
        if direction == 'right':
            self.rect.x += self.__walk_distance

        self.animation = 'walk'

        # self.sprite = self.get_sprite(self.walking_images)
    
    def shoot(self, pos):
        self.animation = 'shoot'
        return self.weapon.shoot(pos)
        
    
    def take_damage(self, value):
        value = value * (1-self.__armour)
        self.hp -= value
        if self.hp <= 0:
            self.kill()
            self.__alive = 0
    
    def att_facing(self, mouse_pos):
        self.animation = 'iddle'
        self.angle = atan2(mouse_pos[1] - self.rect.y, mouse_pos[0] - self.rect.x) * (180/pi)

        if -45 < self.angle < 0:
            self.facing = 'up-right'
        elif -135 < self.angle <= -45:
            self.facing = 'up-straight'
        elif -180 < self.angle <= -135:
            self.facing = 'up-left'


        elif 135 < self.angle <= 180:
            self.facing = 'down-left'
        elif 45 < self.angle <= 135:
            self.facing = 'down-straight'
        elif 0 <= self.angle <= 45:
            self.facing = 'down-right'

        self.weapon.att(self)
        # print(self.facing)


    def att_sprite(self):
        if self.animation == 'walk':
            self.sprite = self.get_sprite(self.walking_images)
        else:
            self.sprite = self.get_sprite(self.iddle_images)
    def get_sprite(self, dic):
        if (self.facing == self.ant and self.animation == self.antanimation):
            self.index += 1
        else:
            self.index = 0
            self.ant = self.facing
            self.antanimation = self.animation

        if self.index >= len(dic[self.facing]):
            self.index = 0

        return dic[self.facing][self.index]




    def create_images(self, sprites_path, frame_skip):
        out = {}
        path = sprites_path + 'Front/'
        sprite45, sprite = listdir(path)
        sprites_down = {'down': [x for x in listdir(path + sprite)],
                                  'down45': [x for x in listdir(path + sprite45)]}
        aux = []
        for x in sprites_down['down']:
            for j in range(frame_skip):
                aux.append(pygame.image.load(path + sprite + "/" + x))

        out['down-straight'] = aux

        aux = []

        for x in sprites_down['down45']:
            for j in range(frame_skip):
                aux.append(pygame.image.load(path + sprite45 + "/" + x))

        out['down-right'] = aux

        aux = []
        for x in out['down-right']:
            aux.append(pygame.transform.flip(x, True, False))
        out['down-left'] = aux
        
        path = sprites_path + "Down/"
        sprite_back45, sprite_back = listdir(path)
        sprites_down = {'back': [x for x in listdir(path + sprite_back)],
                                  'back45': [x for x in listdir(path + sprite_back45)]}

        aux = []
        for x in sprites_down['back']:
            for j in range(frame_skip):
                aux.append(pygame.image.load(path + sprite_back + "/" + x))

        out['up-straight'] = aux

        aux = []
        for x in sprites_down['back45']:
            for j in range(frame_skip):
                aux.append(pygame.image.load(path + sprite_back45 + "/" + x))

        out['up-right'] = aux

        aux = []
        for x in out['up-right']:
            aux.append(pygame.transform.flip(x, True, False))
        out['up-left'] = aux
        
        return out


