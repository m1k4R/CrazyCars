import pygame
import time
import random

from Car import Car
from ObstacleOil import Oil

pygame.init()
gray = (119, 118, 110)
white = (255, 255, 255)
display_width = 800
display_height = 700
gamedisplays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("crazy cars")
clock = pygame.time.Clock()
carimg_player1 = pygame.image.load('car1.png')
carimg_player1_left = pygame.image.load('car1l.png')
carimg_player1_right = pygame.image.load('car1r.png')
carimg_player2 = pygame.image.load('car2.png')
carimg_player2_left = pygame.image.load('car2l.png')
carimg_player2_right = pygame.image.load('car2r.png')
white_strip = pygame.image.load('line.png')
car_width = 32
car_height = 64
boom = pygame.image.load('boom.png')
bom = pygame.image.load('bom.png')


class Obstacle:
    def __init__(self, obs_startx, obs_starty, obs, obs_width, obs_height):
        self.obs_startx = obs_startx
        self.obs_starty = obs_starty
        self.obs = obs
        self.obs_width = obs_width
        self.obs_height = obs_height


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
    gamedisplays.blit(textsurf1, (20, 10))
    gamedisplays.blit(textsurf2, (700, 10))

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


def game_loop():
    player1 = Car(display_width * 0.65, display_height * 0.8, carimg_player1, carimg_player1_left, carimg_player1_right)
    player2 = Car(display_width * 0.30, display_height * 0.8, carimg_player2, carimg_player2_left, carimg_player2_right)
    obstacle_speed = 3
    obstacles = []
    obs = 0
    obs_width = 32
    obs_height = 64
    obs_startx = random.randrange(0, display_width - obs_width)
    obs_starty = 0
    obs_exist = False
    pom = 7
    oil_speed = 2.5
    oils = []
    oil = 0
    oil_width = 114
    oil_height = 107
    oil_startx = random.randrange(0, display_width)
    oil_starty = 0
    oil_exist = False
    bumped = False
    passed = 0
    level = 0
    new_oil = Oil(oil_startx, oil_starty, oil, oil_width, oil_height)
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.quit()
                #quit()
                bumped = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.x_change = -5
                player1.left = True
                player1.car_img = player1.images[1]
            if event.key == pygame.K_RIGHT:
                player1.x_change = 5
                player1.right = True
                player1.car_img = player1.images[2]
            if event.key == pygame.K_UP:
                player1.y_change = -5
                player1.up = True
            if event.key == pygame.K_DOWN:
                player1.y_change = 5
                player1.down = True
            if event.key == pygame.K_a:
                player2.x_change = -5
                player2.left = True
                player2.car_img = player2.images[1]
            if event.key == pygame.K_d:
                player2.x_change = 5
                player2.right = True
                player2.car_img = player2.images[2]
            if event.key == pygame.K_w:
                player2.y_change = -5
                player2.up = True
            if event.key == pygame.K_s:
                player2.y_change = 5
                player2.down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player1.left = False
                player1.car_img = player1.images[0]
            if event.key == pygame.K_RIGHT:
                player1.right = False
                player1.car_img = player1.images[0]
            if event.key == pygame.K_UP:
                player1.up = False
            if event.key == pygame.K_DOWN:
                player1.down = False
            if event.key == pygame.K_a:
                player2.left = False
                player2.car_img = player2.images[0]
            if event.key == pygame.K_d:
                player2.right = False
                player2.car_img = player2.images[0]
            if event.key == pygame.K_w:
                player2.up = False
            if event.key == pygame.K_s:
                player2.down = False

            if player1.left == False and player1.right == False:
                player1.x_change = 0
            if player1.up == False and player1.down == False:
                player1.y_change = 0
            if player2.left == False and player2.right == False:
                player2.x_change = 0
            if player2.up == False and player2.down == False:
                player2.y_change = 0

        player1.x += player1.x_change
        player1.y += player1.y_change
        player2.x += player2.x_change
        player2.y += player2.y_change
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

        player1.check_border(display_width, display_height)
        player2.check_border(display_width, display_height)

        player1.check_another_player_colision(player2)
        player2.check_another_player_colision(player1)

        for obst_oil in oils:
            player1.check_oil_colision(obst_oil)
            player2.check_oil_colision(obst_oil)

        # Pomjeranje nafte
        for obst_oil in oils:
            obst_oil.move_oil_obstacle(oil_speed, gamedisplays)

        new_oil.move_oil_obstacle(oil_speed, gamedisplays)

        # Pomjeri autice i liste
        for obst_car in obstacles:
            obst_car.obs_starty += (obstacle_speed / 4)
            obstacle(obst_car.obs_startx, obst_car.obs_starty, obst_car.obs)
            obst_car.obs_starty += obstacle_speed
        # Pomjeri trenutni autic koji je tek izasao i nije u listi
        obs_starty += (obstacle_speed / 4)
        obstacle(obs_startx, obs_starty, obs)
        obs_starty += obstacle_speed

        player1.show_car(gamedisplays)
        player2.show_car(gamedisplays)

        # Nafta
        if new_oil.oil_starty > new_oil.oil_height:
            for obst_oil in oils:
                if obst_oil.oil_starty > display_height:
                    obst_oil.oil_starty = 0 - obst_oil.oil_height
                    obst_oil.oil_startx = random.randrange(0, display_width)
                    obst_oil.oil = random.randrange(0, 2)
                    if len(oils) < 10:
                        if oil == 0:
                            obs_oil = Oil(new_oil.oil_startx, new_oil.oil_starty, new_oil.oil, 114, 107)
                        else:
                            obs_oil = Oil(new_oil.oil_startx, new_oil.oil_starty, new_oil.oil, 78, 62)
                        oils.append(obs_oil)
                    new_oil.oil_starty = obst_oil.oil_starty
                    new_oil.oil_startx = obst_oil.oil_startx
                    new_oil.oil = obst_oil.oil
                    oil_exist = True
                    break
            if oil_exist == False:
                if oil == 0:
                    obs_oil = Oil(new_oil.oil_startx, new_oil.oil_starty, new_oil.oil, 114, 107)
                else:
                    obs_oil = Oil(new_oil.oil_startx, new_oil.oil_starty, new_oil.oil, 78, 62)
                oils.append(obs_oil)
                new_oil.oil_starty = 0 - oil_height
                new_oil.oil_startx = random.randrange(0, display_width)
                new_oil.oil = random.randrange(0, 2)

        #Autici
        if obs_starty > obs_height:
            for obst_car in obstacles:
                if obst_car.obs_starty > display_height:
                    obst_car.obs_starty = 0 - obst_car.obs_height
                    obst_car.obs_startx = random.randrange(0, display_width - obst_car.obs_width)
                    obst_car.obs = random.randrange(0, 5)
                    if len(obstacles) < 10:
                        if obs == 4:
                            obs_car = Obstacle(obs_startx, obs_starty, obs, 36, 102)
                        else:
                            obs_car = Obstacle(obs_startx, obs_starty, obs, 32, 64)
                        obstacles.append(obs_car)
                    obs_starty = obst_car.obs_starty
                    obs_startx = obst_car.obs_startx
                    obs = obst_car.obs
                    obs_height = obst_car.obs_height
                    obs_exist = True
                    passed = passed + 1
                    if int(passed) % 20 == 0:
                        level = level + 1
                        obstacle_speed += 1
                        oil_speed += 1
                    break
            if obs_exist == False:
                if obs == 4:
                    obs_car = Obstacle(obs_startx, obs_starty, obs, 36, 102)
                else:
                    obs_car = Obstacle(obs_startx, obs_starty, obs, 32, 64)
                obstacles.append(obs_car)
                obs_starty = 0 - obs_car.obs_height
                obs_startx = random.randrange(0, display_width - obs_car.obs_width)
                obs = random.randrange(0, 5)
                obs_height = obs_car.obs_height

        for obst_car in obstacles:
            player1.check_obstacle_colision(obst_car, gamedisplays, bom)
            player2.check_obstacle_colision(obst_car, gamedisplays, bom)

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
