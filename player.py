import pygame
from bullet import Bullet

class Player (pygame.sprite.Sprite):
    def __init__(self, resolution, skin) -> None:
        super().__init__()

        self.__skin = skin
    
        self.__width = (resolution[0]/20 * 0.75) - 30
        self.__height = resolution[1]/20 * 0.75
        self.__walk_distance = max(resolution) / 50 * 0.3

        self.posx = resolution[0]/2 - self.__width
        self.posy = resolution[1]/2 - self.__height
        
        self.image = pygame.Surface([self.__width, self.__height])
        self.image.fill((0, 255, 0))

        self.rect = self.image.get_rect()
        
        self.__cooldown = False
        self.atk = 20
        self.__armour = 0
        self.hp = 1000
        self.__alive = 1
        
    
    def walk(self, direction):
        if direction == 'up':
            self.rect.y -= self.__walk_distance
        
        if direction == 'down':
            self.rect.y += self.__walk_distance

        if direction == 'left':
            self.rect.x -= self.__walk_distance
        
        if direction == 'right':
            self.rect.x += self.__walk_distance
    
    def shoot(self, pos):
        x = pos[0]
        y = pos[1]
        x0 = self.rect.x
        y0 = self.rect.y

        return Bullet(x0, y0, x, y)
        
    
    def take_damage(self, value):
        value = value * (1-self.__armour)
        self.hp -= value
        if self.hp <= 0:
            self.kill()
            self.__alive = 0


