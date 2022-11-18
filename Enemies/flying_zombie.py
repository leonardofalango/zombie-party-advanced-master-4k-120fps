from .enemy import Enemy
import random as rd



class Flying_zombie(Enemy):
    def __init__(self, resolution):

        super().__init__(resolution, 5, 1, (60, 80), 4)
        self.width = 70
        self.height = 130
        super().create_sprites("E:/leonardo-falango/Sprites/Player/Skin_Zombie_Fast", 3)

        self.__resolution = resolution
        self.__walk_distance = max(resolution) / 50 * 0.25

        self.__direction = 'right'
        self.__random = rd.randint(0, self.__walk_distance)





