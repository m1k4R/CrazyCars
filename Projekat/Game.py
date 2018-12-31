import pygame
import time

pygame.init()
gray = (119, 118, 110)
white = (255, 255, 255)
display_width = 800
display_height = 700
gamedisplays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("crazy cars")
clock = pygame.time.Clock()
carimg = pygame.image.load('car1.png')
white_strip = pygame.image.load('line.png')
car_width = 32
car_height = 64

def text_objects(text, font):
    textsurface = font.render(text, True, white)
    return  textsurface, textsurface.get_rect()

def message_life_player(text):
    largetext = pygame.font.Font("freesansbold.ttf", 20)
    textsurf1, textrect1 = text_objects("Player 2", largetext)
    textsurf2, textrect2 = text_objects("Player 1", largetext)
    #textrect = ((display_width/2), (display_height/2))
    gamedisplays.blit(textsurf1, (20, 10))
    gamedisplays.blit(textsurf2, (700, 10))
    #pygame.display.update()
    #time.sleep(3)
    #game_loop()

def background():
    gamedisplays.blit(white_strip, (120, 0))
    gamedisplays.blit(white_strip, (120, 150))
    gamedisplays.blit(white_strip, (120, 300))
    gamedisplays.blit(white_strip, (120, 450))
    gamedisplays.blit(white_strip, (120, 600))
    gamedisplays.blit(white_strip, (120, 750))
    gamedisplays.blit(white_strip, (240, 0))
    gamedisplays.blit(white_strip, (240, 150))
    gamedisplays.blit(white_strip, (240, 300))
    gamedisplays.blit(white_strip, (240, 450))
    gamedisplays.blit(white_strip, (240, 600))
    gamedisplays.blit(white_strip, (240, 750))
    gamedisplays.blit(white_strip, (360, 0))
    gamedisplays.blit(white_strip, (360, 150))
    gamedisplays.blit(white_strip, (360, 300))
    gamedisplays.blit(white_strip, (360, 450))
    gamedisplays.blit(white_strip, (360, 600))
    gamedisplays.blit(white_strip, (360, 750))
    gamedisplays.blit(white_strip, (480, 0))
    gamedisplays.blit(white_strip, (480, 150))
    gamedisplays.blit(white_strip, (480, 300))
    gamedisplays.blit(white_strip, (480, 450))
    gamedisplays.blit(white_strip, (480, 600))
    gamedisplays.blit(white_strip, (480, 750))
    gamedisplays.blit(white_strip, (600, 0))
    gamedisplays.blit(white_strip, (600, 150))
    gamedisplays.blit(white_strip, (600, 300))
    gamedisplays.blit(white_strip, (600, 450))
    gamedisplays.blit(white_strip, (600, 600))
    gamedisplays.blit(white_strip, (600, 750))
    gamedisplays.blit(white_strip, (720, 0))
    gamedisplays.blit(white_strip, (720, 150))
    gamedisplays.blit(white_strip, (720, 300))
    gamedisplays.blit(white_strip, (720, 450))
    gamedisplays.blit(white_strip, (720, 600))
    gamedisplays.blit(white_strip, (720, 750))

def car(x, y):
    gamedisplays.blit(carimg, (x, y))


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0
    left = False
    right = False
    up = False
    down = False

    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
                left = True
            if event.key == pygame.K_RIGHT:
                x_change = 5
                right = True
            if event.key == pygame.K_UP:
                y_change = -5
                up = True
            if event.key == pygame.K_DOWN:
                y_change = 5
                down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False

            if left == False and right == False:
                x_change = 0
            if up == False and down == False:
                y_change = 0

        x += x_change
        y += y_change
        gamedisplays.fill(gray)
        background()
        message_life_player("3")
        #message_life_player2()
        if x <= 1 or x >= display_width - car_width:
            x -= x_change
        if y <= 60 or y >= display_height - car_height:
            y -= y_change
        car(x, y)
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
