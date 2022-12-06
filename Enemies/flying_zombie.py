from .enemy import Enemy
import random as rd



class Flying_zombie(Enemy):
    def __init__(self, resolution):
            
        super().__init__(resolution, 5, 1, (100, 70), 4)
        self.width = 70
        self.height = 130
        super().create_sprites("Sprites/Player/Skin_Zombie_Fast", 3)

        self.__resolution = resolution
        self.__walk_distance = max(resolution) / 50 * 0.25
        self.image.fill((255,255,255))

        self.__direction = 'right'
        self.__random = rd.randint(0, self.__walk_distance)





