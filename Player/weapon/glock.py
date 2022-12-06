from Player import weapon
from . import bullet, weapon


class Glock(weapon.Weapon):
    def __init__(self, resolution, player):
        super().__init__(resolution, player, 0.7, 210, 70)
        super().create_sprites('././Sprites/Weapons/Glock-Rajada', 5)

    

    def shoot(self, pos):
        if (self.canfire):
            self.canfire = False
            self.index += 1

            return [bullet.Bullet(self.rect.x, self.rect.y, pos[0], pos[1])]
