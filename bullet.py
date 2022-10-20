import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super(Bullet, self).__init__()
        self.image = pygame.Surface([self.__width, self.__height])
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y