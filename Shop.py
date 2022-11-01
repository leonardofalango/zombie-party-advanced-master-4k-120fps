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
    def __init__(self, x, text, img, img_x, img_y) -> None:
        self.x = x
        self.text = text
        self.img = img
        self.img_x = img_x
        self.img_y = img_y

def pil_to_game(img):
    data = img.tobytes("raw", "RGBA")
    return pygame.image.fromstring(data, img.size, "RGBA")

def get_gif_frame(img, frame):
    img.seek(frame)
    return  img.convert("RGBA")


def shop(screen):
    gif_img = Image.open("gifundo.gif")
    current_frame = 0
    clock = pygame.time.Clock()

    game = False
    shopping = True
    while shopping:
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
                if mouse[0] in range(38, 138) and mouse[1] in range(10, 45):
                    shopping = False

        print(f"x: {mouse[0]} - y: {mouse[1]}")

        # botao voltar
        if mouse[0] in range(38, 138) and mouse[1] in range(10, 45):
            pygame.draw.rect(screen, color_dark, [38, 10, 100, 40], border_radius=10)
        else:
            pygame.draw.rect(screen, (29, 0, 57), [38, 10, 100, 40], border_radius=10)

        screen.blit(minimalfont.render("Voltar", True, color, None), (38 + 20, 15))

        coins = 25
        screen.blit(minimalfont.render(f"{coins} coins", True, color, None), (610, 15))

        cards = [Card(40, 'AK47', pygame.image.load("Sprites/Guns/sprite_ak471.png"), 70, 100), Card(270, 'USP-S', pygame.image.load("Sprites/Guns/sprite_ak471.png"), 200, 150), Card(500, 'SHOTGUN', pygame.image.load("Sprites/Guns/sprite_Shotgun3.png"), 200, 100)]



        for card in cards:
            image = pygame.transform.scale(card.img, (150, 150))
            screen.blit(image, (card.img_x, card.img_y))
            pygame.draw.rect(screen, color_light, [card.x, 60, 200, 250], border_radius=10)
            card.text = shopfont.render(card.text, True, color, None)


        screen.blit(cards[0].text, (cards[0].x + 55, 70))
        screen.blit(cards[1].text, (cards[1].x + 45, 70))
        screen.blit(cards[2].text, (cards[2].x + 20, 70))

        btn_x = [65, 295, 525]
        hover_range = [(65, 212), (294, 444), (526, 672)]
        for i in range(3):
            if mouse[0] in range(hover_range[i][0], hover_range[i][1]) and mouse[1] in range(260, 298):
                pygame.draw.rect(screen, (29, 0, 57), [btn_x[i], 260, 150, 40], border_radius=10)
            else:
                pygame.draw.rect(screen, color_dark, [btn_x[i], 260, 150, 40], border_radius=10)

        text = minimalfont.render("BUY!", True, color, None)
        screen.blit(text, (btn_x[0] + 50, 265))
        screen.blit(text, (btn_x[1] + 50, 265))
        screen.blit(text, (btn_x[2] + 50, 265))

        pygame.draw.rect(screen, (29, 0, 57), [39, 330, 320, 150], border_radius=10)
        text = minimalfont.render("Oclin", True, color, None)
        screen.blit(text, (175, 340))

        pygame.draw.rect(screen, (29, 0, 57), [382, 330, 320, 150], border_radius=10)
        text = minimalfont.render("Ota skin", True, color, None)
        screen.blit(text, (495, 340))

        pygame.display.update()


shop(screen)
