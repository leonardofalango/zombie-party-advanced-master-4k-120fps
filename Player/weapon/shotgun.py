from . import weapon, bullet
import random as rd

class Shotgun(weapon.Weapon):
    def __init__(self, resolution, player):
        super().__init__(resolution, player, 1.3, 210, 126)
        super().create_sprites('E:/leonardo-falango/Sprites/Weapons/Shotgun', 3)

    def shoot(self, pos):
        if (self.canfire):
            self.canfire = False
            self.index += 1

            return [bullet.Bullet(self.rect.x, self.rect.y, pos[0] + rd.randint(-20, 20), pos[1] + rd.randint(-20, 20)) for i in range(5)]