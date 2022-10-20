from enemy import Enemy
import random as rd
class Tank_zombie(Enemy):
    def __init__(self, resolution):
        width, height = resolution[0] / 15 * 0.75, resolution[1] / 10 * 0.75
        super().__init__(resolution, 1, 0.1, 20, 20)

        self.__resolution = resolution
        self.__walk_distance = max(resolution) / 50 * 0.25

        self.__direction = 'right'
        self.__random = rd.randint(0, self.__walk_distance)

        self.rect.x = rd.randint(0, resolution[0] - self.rect.width)
        self.rect.y = rd.randint(0, resolution[1] - self.rect.height)





