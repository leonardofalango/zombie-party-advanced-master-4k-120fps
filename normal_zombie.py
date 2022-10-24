from enemy import Enemy
import random as rd
class Normal_zombie(Enemy):
    def __init__(self, resolution):
        width, height = resolution[0] / 15 * 0.75, resolution[1] / 10 * 0.75
        super().__init__(resolution, 100, 20, (width, height), 1)
        self.__walk_distance = max(resolution) / 50 * 0.1


