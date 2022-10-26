from . import weapon
from . import bullet



class Glock(weapon.Weapon):
    def __init__(self, resolution, player):
        super().__init__(resolution, player)
    

    def shoot(self, pos):
        return bullet.Bullet(self.rect.x, self.rect.y, pos[0], pos[1])