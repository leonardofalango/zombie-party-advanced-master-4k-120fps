
from enemy import Enemy
import random as rd

class Flying_zombie(Enemy):
    def __init__(self, resolution):
        width, height = resolution[0] / 15 * 0.75, resolution[1] / 10 * 0.75
        super().__init__(resolution, 1, 0.1, 20, 20)

        self.__resolution = resolution
        self.__walk_distance = max(resolution) / 50 * 0.25

        self.__direction = 'right'
        self.__random = rd.randint(0, self.__walk_distance)

        self.rect.x = rd.randint(0, resolution[0] - self.rect.width)
        self.rect.y = rd.randint(0, resolution[1] - self.rect.height)

    def __str__(self):
        return f'Nome: Flying Zombie\bHo: {self.__hp}\nEstá vivo: {self.alive}\nPos X: {self.rect.x}\nPos Y: {self.rect.y}'

    def walk(self):
        if self.rect.y == 0:
            self.__direction = 'down'
            self.__random = self.__random * -1
        if self.rect.y == self.__resolution[1]:
            self.__direction = 'up'
            self.__random = self.__random * -1
        if self.rect.x == 0:
            self.__direction = 'right'
            self.__random = self.__random * -1
        if self.rect.x == self.__resolution[0]:
            self.__direction = 'left'
            self.__random = self.__random * -1

        if self.__direction == 'up':
            self.rect.y -= self.__walk_distance
            self.rect.x += self.__random

        if self.__direction == 'down':
            self.rect.y += self.__walk_distance
            self.rect.x += self.__random

        if self.__direction == 'left':
            self.rect.x -= self.__walk_distance
            self.rect.y += self.__random

        if self.__direction == 'right':
            self.rect.x += self.__walk_distance
            self.rect.y += self.__random