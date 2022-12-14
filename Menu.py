from msilib import MSICOLINFO_TYPES
import pygame
import sys
from time import sleep


pygame.init()
res = (750, 500)
screen = pygame.display.set_mode(res)
color = (255, 255, 255)
color_light = (138, 43, 226)
color_dark = (111, 26, 189)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.Font('Grand9K Pixel.ttf', 40)
shopfont = pygame.font.Font('Grand9K Pixel.ttf', 30)

from PIL import Image

def pil_to_game(img):
    data = img.tobytes("raw", "RGBA")
    return pygame.image.fromstring(data, img.size, "RGBA")

def get_gif_frame(img, frame):
    img.seek(frame)
    return  img.convert("RGBA")

global shopping


def menu(screen, player, mundo):
    gif_img = Image.open("gifundo.gif")
    current_frame = 0
    clock = pygame.time.Clock()


    game = False
    while not game:
        shopping = False
        frame = pil_to_game(get_gif_frame(gif_img, current_frame))
        screen.blit(frame, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        current_frame = (current_frame + 1) % gif_img.n_frames

        # pygame.display.flip()
        clock.tick(30)

        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            
            if ev.type == pygame.MOUSEBUTTONDOWN or ev.type == pygame.MOUSEBUTTONUP:
                if mouse[0] in range(299, 449) and mouse[1] in range(335, 404):
                    game = True
                    mundo.reset()
                
                if mouse[0] in range(29, 160) and mouse[1] in range(29, 79):
                    shopping = True
                    from Shop import shop
                    shop(screen, player, mundo)

        # print(f"x: {mouse[0]} - y: {mouse[1]}")

        # game button
        if mouse[0] in range(299, 449) and mouse[1] in range(335, 404):
            text = smallfont.render('Jogar', True, color, color_light)
            pygame.draw.rect(screen, color_light, [width / 2 - 75, height / 2 + 85, 150, 70], border_radius=10)

        else:
            text = smallfont.render('Jogar', True, color, color_dark)
            pygame.draw.rect(screen, color_dark, [width / 2 - 75, height / 2 + 85, 150, 70], border_radius=10)

        screen.blit(text, (width / 2 - 65, height / 2 + 90))

        # shop button
        if mouse[0] in range(30, 160) and mouse[1] in range(29, 78):
            text = shopfont.render('Loja', True, color, color_light)
            pygame.draw.rect(screen, color_light, [30, 30, 130, 50], border_radius=10)

        else:
            text = shopfont.render('Loja', True, color, color_dark)
            pygame.draw.rect(screen, color_dark, [30, 30, 130, 50], border_radius=10)
        
        screen.blit(text, (60, 30))

        pygame.display.update()



