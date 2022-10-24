from enemy import Enemy
import random as rd


class Flying_zombie(Enemy):
    def __init__(self, resolution):

        super().__init__(resolution, 5, 1, (20, 20), 0.5)

        self.__resolution = resolution
        self.__walk_distance = max(resolution) / 50 * 0.25

        self.__direction = 'right'
        self.__random = rd.randint(0, self.__walk_distance)




