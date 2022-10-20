from weapon import Weapon

class Ak_47(Weapon):
    def __init__(self, resolution):
        super(Ak_47, self).__init__(resolution)
        self.damage = 20
        self.fire_rate = 10

class Glock(Weapon):
    def __init__(self, resolution):
        super(Glock, self).__init__(resolution)
        self.damage = 5
        self.fire_rate = 5