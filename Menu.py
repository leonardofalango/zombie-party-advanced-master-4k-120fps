import pygame
import sys

pygame.init()
res = (750, 500)
screen = pygame.display.set_mode(res)
color = (255, 255, 255)
color_light = (138, 43, 226)
color_dark = (111, 26, 189)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.Font('Grand9K Pixel.ttf', 40)

from PIL import Image

def pil_to_game(img):
    data = img.tobytes("raw", "RGBA")
    return pygame.image.fromstring(data, img.size, "RGBA")

def get_gif_frame(img, frame):
    img.seek(frame)
    return  img.convert("RGBA")

def menu(screen):
    gif_img = Image.open("gifundo.gif")
    current_frame = 0
    clock = pygame.time.Clock()

    game = False
    while not game:
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

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] in range(299, 449) and mouse[1] in range(335, 404):
                    game = True

        # print(f"x: {mouse[0]} - y: {mouse[1]}")
        if mouse[0] in range(299, 449) and mouse[1] in range(335, 404):
            text = smallfont.render('Jogar', True, color, color_light)
            pygame.draw.rect(screen, color_light, [width / 2 - 75, height / 2 + 85, 150, 70], border_radius=10)

        else:
            text = smallfont.render('Jogar', True, color, color_dark)
            pygame.draw.rect(screen, color_dark, [width / 2 - 75, height / 2 + 85, 150, 70], border_radius=10)

        screen.blit(text, (width / 2 - 65, height / 2 + 90))

        pygame.display.update()


menu(screen)

