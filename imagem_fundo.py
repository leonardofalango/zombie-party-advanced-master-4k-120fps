import pygame

pygame.init()

window = pygame.display.set_mode([548, 466])
pygame.display.set_caption("Jogo")

fundo = pygame.image.load("Centro RPG Maker.png")
window.blit(fundo, (8, 8))
loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
    pygame.display.update()