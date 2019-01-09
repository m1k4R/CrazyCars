import pygame
import time
import random

pygame.init()
gray = (119, 118, 110)
white = (255, 255, 255)
display_width = 800
display_height = 700
gamedisplays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("crazy cars")
clock = pygame.time.Clock()
carimg_player1 = pygame.image.load('car1.png')
carimg_player2 = pygame.image.load('car2.png')
white_strip = pygame.image.load('line.png')
car_width = 32
car_height = 64

def obstacle(obs_startx, obs_starty, obs):
    if obs == 0:
        obs_pic = pygame.image.load("car3.png")
    elif obs == 1:
        obs_pic = pygame.image.load("car4.png")
    elif obs == 2:
        obs_pic = pygame.image.load("car5.png")
    elif obs == 3:
        obs_pic = pygame.image.load("car6.png")
    elif obs == 4:
        obs_pic = pygame.image.load("car7.png")
    gamedisplays.blit(obs_pic, (obs_startx, obs_starty))


def oil_obstacle(oil_startx, oil_starty, oil):
    if oil == 0:
        oil_pic = pygame.image.load("oil.png")
    elif oil == 1:
        oil_pic = pygame.image.load("oill.png")
    gamedisplays.blit(oil_pic, (oil_startx, oil_starty))


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

def life_player1(number):
    if number == 3:
        life_pic = pygame.image.load("r3.png")
    elif number >= 2.0 and number < 3:
        life_pic = pygame.image.load("r2.png")
    elif number >= 1.5 and number < 2.0:
        life_pic = pygame.image.load("r1.png")
    elif number < 1.5:
        life_pic = pygame.image.load("g.png")
    else:
        life_pic = pygame.image.load("r3.png")
    gamedisplays.blit(life_pic, (695, 40))


def life_player2(number):
    if number == 3:
        life_pic = pygame.image.load("y3.png")
    elif number >= 2.0 and number < 3:
        life_pic = pygame.image.load("y2.png")
    elif number >= 1.5 and number < 2.0:
        life_pic = pygame.image.load("y1.png")
    elif number < 1.5:
        life_pic = pygame.image.load("g.png")
    else:
        life_pic = pygame.image.load("y3.png")
    gamedisplays.blit(life_pic, (15, 40))


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

def car_player1(x, y):
    gamedisplays.blit(carimg_player1, (x, y))


def car_player2(x, y):
    gamedisplays.blit(carimg_player2, (x, y))


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0
    left = False
    right = False
    up = False
    down = False
    x2 = (display_width * 0.30)
    y2 = (display_height * 0.8)
    x2_change = 0
    y2_change = 0
    left2 = False
    right2 = False
    up2 = False
    down2 = False
    obstacle_speed = 3
    pom = 7
    player1_life = 3
    player2_life = 3
    global carimg_player1
    global carimg_player2
    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
                left = True
                carimg_player1 = pygame.image.load('car1l.png')
            if event.key == pygame.K_RIGHT:
                x_change = 5
                right = True
                carimg_player1 = pygame.image.load('car1r.png')
            if event.key == pygame.K_UP:
                y_change = -5
                up = True
            if event.key == pygame.K_DOWN:
                y_change = 5
                down = True
            if event.key == pygame.K_a:
                x2_change = -5
                left2 = True
                carimg_player2 = pygame.image.load('car2l.png')
            if event.key == pygame.K_d:
                x2_change = 5
                right2 = True
                carimg_player2 = pygame.image.load('car2r.png')
            if event.key == pygame.K_w:
                y2_change = -5
                up2 = True
            if event.key == pygame.K_s:
                y2_change = 5
                down2 = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
                carimg_player1 = pygame.image.load('car1.png')
            if event.key == pygame.K_RIGHT:
                right = False
                carimg_player1 = pygame.image.load('car1.png')
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False
            if event.key == pygame.K_a:
                left2 = False
                carimg_player2 = pygame.image.load('car2.png')
            if event.key == pygame.K_d:
                right2 = False
                carimg_player2 = pygame.image.load('car2.png')
            if event.key == pygame.K_w:
                up2 = False
            if event.key == pygame.K_s:
                down2 = False

            if left == False and right == False:
                x_change = 0
            if up == False and down == False:
                y_change = 0
            if left2 == False and right2 == False:
                x2_change = 0
            if up2 == False and down2 == False:
                y2_change = 0

        x += x_change
        y += y_change
        x2 += x2_change
        y2 += y2_change
        gamedisplays.fill(gray)

        rel_y = pom % 300
        if rel_y < 800:
            gamedisplays.blit(white_strip, (120, rel_y + 0))
            gamedisplays.blit(white_strip, (120, rel_y + 150))
            gamedisplays.blit(white_strip, (120, rel_y + 300))
            gamedisplays.blit(white_strip, (120, rel_y + 450))
            gamedisplays.blit(white_strip, (120, rel_y + 600))
            gamedisplays.blit(white_strip, (120, rel_y + 750))
            gamedisplays.blit(white_strip, (120, rel_y - 300))
            gamedisplays.blit(white_strip, (120, rel_y - 150))
            gamedisplays.blit(white_strip, (240, rel_y + 0))
            gamedisplays.blit(white_strip, (240, rel_y + 150))
            gamedisplays.blit(white_strip, (240, rel_y + 300))
            gamedisplays.blit(white_strip, (240, rel_y + 450))
            gamedisplays.blit(white_strip, (240, rel_y + 600))
            gamedisplays.blit(white_strip, (240, rel_y + 750))
            gamedisplays.blit(white_strip, (240, rel_y - 300))
            gamedisplays.blit(white_strip, (240, rel_y - 150))
            gamedisplays.blit(white_strip, (360, rel_y + 0))
            gamedisplays.blit(white_strip, (360, rel_y + 150))
            gamedisplays.blit(white_strip, (360, rel_y + 300))
            gamedisplays.blit(white_strip, (360, rel_y + 450))
            gamedisplays.blit(white_strip, (360, rel_y + 600))
            gamedisplays.blit(white_strip, (360, rel_y + 750))
            gamedisplays.blit(white_strip, (360, rel_y - 300))
            gamedisplays.blit(white_strip, (360, rel_y - 150))
            gamedisplays.blit(white_strip, (480, rel_y + 0))
            gamedisplays.blit(white_strip, (480, rel_y + 150))
            gamedisplays.blit(white_strip, (480, rel_y + 300))
            gamedisplays.blit(white_strip, (480, rel_y + 450))
            gamedisplays.blit(white_strip, (480, rel_y + 600))
            gamedisplays.blit(white_strip, (480, rel_y + 750))
            gamedisplays.blit(white_strip, (480, rel_y - 300))
            gamedisplays.blit(white_strip, (480, rel_y - 150))
            gamedisplays.blit(white_strip, (600, rel_y + 0))
            gamedisplays.blit(white_strip, (600, rel_y + 150))
            gamedisplays.blit(white_strip, (600, rel_y + 300))
            gamedisplays.blit(white_strip, (600, rel_y + 450))
            gamedisplays.blit(white_strip, (600, rel_y + 600))
            gamedisplays.blit(white_strip, (600, rel_y + 750))
            gamedisplays.blit(white_strip, (600, rel_y - 300))
            gamedisplays.blit(white_strip, (600, rel_y - 150))
            gamedisplays.blit(white_strip, (720, rel_y + 0))
            gamedisplays.blit(white_strip, (720, rel_y + 150))
            gamedisplays.blit(white_strip, (720, rel_y + 300))
            gamedisplays.blit(white_strip, (720, rel_y + 450))
            gamedisplays.blit(white_strip, (720, rel_y + 600))
            gamedisplays.blit(white_strip, (720, rel_y + 750))
            gamedisplays.blit(white_strip, (720, rel_y - 300))
            gamedisplays.blit(white_strip, (720, rel_y - 150))

        pom += obstacle_speed
        #background()
        message_life_player("3")
        #message_life_player2()
        if x <= 1 or x >= display_width - car_width:
            x -= x_change
        if y <= 60 or y >= display_height - car_height:
            y -= y_change
        if x2 <= 1 or x2 >= display_width - car_width:
            x2 -= x2_change
        if y2 <= 60 or y2 >= display_height - car_height:
            y2 -= y2_change

        if y >= y2 and y <= y2 + car_height or y + car_height >= y2 and y + car_height <= y2 + car_height:
            if x >= x2 and x <= x2 + car_width or x + car_width >= x2 and x + car_width <= x2 + car_width:
                x -= x_change
                y -= y_change
        if y2 >= y and y2 <= y + car_height or y2 + car_height >= y and y2 + car_height <= y + car_height:
            if x2 >= x and x2 <= x + car_width or x2 + car_width >= x and x2 + car_width <= x + car_width:
                x2 -= x2_change
                y2 -= y2_change

        car_player1(x, y)
        car_player2(x2, y2)
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
