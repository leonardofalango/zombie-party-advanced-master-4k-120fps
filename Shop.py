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
shopfont = pygame.font.Font('Grand9K Pixel.ttf', 30)
minimalfont = pygame.font.Font('Grand9K Pixel.ttf', 20)

from PIL import Image

class Card:
    def __init__(self, x, text) -> None:
        self.x = x
        self.text = text
        self.img = ''

def pil_to_game(img):
    data = img.tobytes("raw", "RGBA")
    return pygame.image.fromstring(data, img.size, "RGBA")

def get_gif_frame(img, frame):
    img.seek(frame)
    return  img.convert("RGBA")

def shop():
    pass

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

        print(f"x: {mouse[0]} - y: {mouse[1]}")
        
        
        cards = [Card(40, 'AK47'), Card(270, 'USP-S'), Card(500, 'SHOTGUN')]
        for card in cards:
            pygame.draw.rect(screen, color_light, [card.x, 30, 200, 250], border_radius=10)
            card.text = shopfont.render(card.text, True, color, None)

        screen.blit(cards[0].text, (cards[0].x + 55, 40))
        screen.blit(cards[1].text, (cards[1].x + 45, 40))
        screen.blit(cards[2].text, (cards[2].x + 20, 40))

        btn_x = [65, 295, 525]
        hover_range = [(65, 212), (294, 444), (526, 672)]
        for i in range(3):
            if mouse[0] in range(hover_range[i][0], hover_range[i][1]) and mouse[1] in range(230, 268):
                pygame.draw.rect(screen, (29, 0, 57), [btn_x[i], 230, 150, 40], border_radius=10)


            else:
                pygame.draw.rect(screen, color_dark, [btn_x[i], 230, 150, 40], border_radius=10)

        text = minimalfont.render("BUY!", True, color, None)
        screen.blit(text, (btn_x[0] + 50, 235))
        screen.blit(text, (btn_x[1] + 50, 235))
        screen.blit(text, (btn_x[2] + 50, 235))

        pygame.draw.rect(screen, (29, 0, 57), [39, 300, 320, 180], border_radius=10)
        text = minimalfont.render("Oclin", True, color, None)
        screen.blit(text, (175, 310))

        pygame.draw.rect(screen, (29, 0, 57), [382, 300, 320, 180], border_radius=10)
        text = minimalfont.render("Ota skin", True, color, None)
        screen.blit(text, (495, 310))

        pygame.display.update()


menu(screen)
