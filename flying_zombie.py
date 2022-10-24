from enemy import Enemy
import random as rd


class Flying_zombie(Enemy):
    def __init__(self, resolution):

        super().__init__(resolution, 5, 1, (20, 20), 0.5)

        self.__resolution = resolution
        self.__walk_distance = max(resolution) / 50 * 0.25

        self.__direction = 'right'
        self.__random = rd.randint(0, self.__walk_distance)

        self.rect.x = rd.randint(0, resolution[0] - self.rect.width)
        self.rect.y = rd.randint(0, resolution[1] - self.rect.height)

    def __str__(self):
        return f'Nome: Flying Zombie\bHo: {self.__hp}\nEstá vivo: {self.alive}\nPos X: {self.rect.x}\nPos Y: {self.rect.y}'

