from .enemy import Enemy
class Normal_zombie(Enemy):
    def __init__(self, resolution, mundo):
        self.width, self.height = 120, 150
        super().__init__(resolution, 25, 20, (self.width, self.height), 1, mundo)
        self.__walk_distance = max(resolution) / 50 * 0.1
        super().create_sprites("./Sprites/Player/Skin_Zombie", 6)



