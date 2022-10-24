import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self, playerx, playery, x, y):
        super(Bullet, self).__init__()
        self.__width, self.__height = 10,10
        self.image = pygame.Surface([self.__width, self.__height])
        self.image.fill((255, 255, 255))

        self.rect = self.image.get_rect()
        self.rect.x = playerx
        self.rect.y = playery

        self.__xinicial = playerx
        self.__yinicial = playery


        self.__xfinal = x
        self.__yfinal = y



        self.__vel = 0.1

        self.__incre_x = -((self.__xinicial - self.__xfinal) * self.__vel)
        self.__incre_y = -((self.__yinicial - self.__yfinal) * self.__vel)

    def shoot(self):
        self.rect.x += self.__incre_x
        self.rect.y += self.__incre_y

