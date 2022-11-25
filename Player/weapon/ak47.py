from Player import weapon
from . import bullet, weapon


class Ak47(weapon.Weapon):
    def __init__(self, resolution, player):
        super().__init__(resolution, player, 0.05, 210, 180)
        super().create_sprites("/Sprites/Weapons/AK-47", 3)

    def shoot(self, pos):
        if (self.canfire):
            self.canfire = False
            return [bullet.Bullet(self.rect.x, self.rect.y, pos[0], pos[1])]