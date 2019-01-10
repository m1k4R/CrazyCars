import pygame
import time
import random

from Car import Car
from ObstacleOil import Oil
from ObstacleCar import ObstacleCar
import keyboard

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
level_img = pygame.image.load('linelevel.png')
udlf = pygame.image.load('udlr.png')
wasd = pygame.image.load('wasd.png')
bright_blue = (0, 0, 255)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)
green = (0, 200, 0)
red = (255, 0, 0)
blue = (0, 0, 200)
gray2 = (186, 186, 186,0)
gray3 = (114, 114, 114)
yellow = (255,207,49)
image1 = pygame.image.load('image1.jpg')

def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        gamedisplays.fill(gray)
        largetext=pygame.font.Font('freesansbold.ttf',95)
        TextSurf,TextRect=text_objects("CRAZY CARS",largetext)
        TextRect.center=(400,100)
        gamedisplays.fill(gray3)
        imag = pygame.transform.scale(image1, (800,600))
        gamedisplays.blit(imag, (0, 100))
        gamedisplays.blit(TextSurf,TextRect)
        if keyboard.is_pressed('SPACE'):
            game_loop()
        button("START",390,234,70,40,red,yellow,"play")
        button("QUIT",430,630,200,50,gray2,gray3,"quit")
        button("INSTRUCTION",210,630,200,50,gray2,gray3,"intro")
        pygame.display.update()
        clock.tick(50)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()

    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gamedisplays,ac,(x,y,w,h))

        if click[0]==1 and action!=None:
            if action=="play":
                game_loop()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                introduction()
            elif action=="menu":
                intro_loop()
    else:
        pygame.draw.rect(gamedisplays,ic,(x,y,w,h))

    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gamedisplays.blit(textsurf,textrect)

def introduction():
    introduction=True

    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        gamedisplays.fill(gray)
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        TextSurf,TextRect=text_objects("INSTRUCTION",largetext)
        TextRect.center=((400),(100))
        gamedisplays.blit(TextSurf,TextRect)
        stextSurf,stextRect=text_objects("PLAYER 1",smalltext)
        stextRect.center=((210),(300))
        stextSurf2, stextRect2 = text_objects("PLAYER 2", smalltext)
        stextRect2.center = ((555), (300))
        sTextSurf,sTextRect=text_objects("CONTROLS",mediumtext)
        sTextRect.center=((400),(200))
        gamedisplays.blit(sTextSurf,sTextRect)

        gamedisplays.blit(stextSurf,stextRect)
        gamedisplays.blit(stextSurf2,stextRect2)
        control1 = pygame.transform.scale(udlf, (300,192))
        gamedisplays.blit(control1,(50,350))
        gamedisplays.blit(wasd,(420,350))
        button("BACK",320,600,100,50,gray2,gray,"menu")
        pygame.display.update()
        clock.tick(30)


def oil_obstacle(oil_startx, oil_starty, oil):
    if oil == 0:
        oil_pic = pygame.image.load("oil.png")
    elif oil == 1:
        oil_pic = pygame.image.load("oill.png")
    gamedisplays.blit(oil_pic, (oil_startx, oil_starty))

def score_level_system(passed, level):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Passed: " + str(passed), True, white)
    font_level = pygame.font.SysFont(None, 35)
    text_level = font_level.render("LEVEL", True, white)
    txt_level = font_level.render(str(level), True, white)
    gamedisplays.blit(text, (5, 680))
    gamedisplays.blit(text_level, (350, 7))
    gamedisplays.blit(level_img, (340, 35))
    gamedisplays.blit(txt_level, (380, 44))

def text_objects(text, font):
    textsurface = font.render(text, True, white)
    return  textsurface, textsurface.get_rect()


def message_life_player(text):
    largetext = pygame.font.Font("freesansbold.ttf", 20)
    textsurf1, textrect1 = text_objects("Player 2", largetext)
    textsurf2, textrect2 = text_objects("Player 1", largetext)
    gamedisplays.blit(textsurf1, (20, 10))
    gamedisplays.blit(textsurf2, (700, 10))

def message_display(text):
    largetext3 = pygame.font.Font("freesansbold.ttf", 80)
    textsurf3, textrect3 = text_objects(text, largetext3)
    textrect3.center = ((display_width / 2), (display_height / 2))
    gamedisplays.blit(textsurf3, textrect3)
    pygame.display.update()
    time.sleep(3)
    game_loop()

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


def background(rel_y):
    white_strip = pygame.image.load('line.png')
    x = [120, 240, 360, 480, 600, 720]
    y = [0, 150, 300, 450, 600, 750]
    for a in x:
        for b in y:
            gamedisplays.blit(white_strip, (a, rel_y + b))
        gamedisplays.blit(white_strip, (a, rel_y - 300))
        gamedisplays.blit(white_strip, (a, rel_y - 150))


def crash():
    message_display("GAME OVER")
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
    new_car = ObstacleCar(obs_startx, 0, 0, 32, 64)
    new_oil = Oil(oil_startx, oil_starty, oil, oil_width, oil_height)
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                #bumped = True
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

                if player1.up == False and player1.down == True:
                    player1.y_change = 5
                if player1.up == True and player1.down == False:
                    player1.y_change = -5
                if player2.up == False and player2.down == True:
                    player2.y_change = 5
                if player2.up == True and player2.down == False:
                    player2.y_change = -5

                if player1.left == False and player1.right == True:
                    player1.x_change = 5
                if player1.left == True and player1.right == False:
                    player1.x_change = -5
                if player2.left == False and player2.right == True:
                    player2.x_change = 5
                if player2.left == True and player2.right == False:
                    player2.x_change = -5

        player1.x += player1.x_change
        player1.y += player1.y_change
        player2.x += player2.x_change
        player2.y += player2.y_change
        gamedisplays.fill(gray)

        rel_y = pom % 300
        if rel_y < 800:
            background(rel_y)

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

        # Pomjeranje autica
        for obst_car in obstacles:
            obst_car.move_obstacle(obstacle_speed, gamedisplays)
        new_car.move_obstacle(obstacle_speed, gamedisplays)

        player1.show_car(gamedisplays)
        player2.show_car(gamedisplays)

        if player1.life > 1.5:
            player1.show_car(gamedisplays)
        if player2.life > 1.5:
            player2.show_car(gamedisplays)

        message_life_player("3")
        # message_life_player2()
        life_player1(player1.life)
        life_player2(player2.life)
        score_level_system(passed, level)

        if player1.life <= 1.5 and player2.life <= 1.5:
            crash()

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

                # Autici
            if new_car.obs_starty > new_car.obs_height:
                for obst_car in obstacles:
                    if obst_car.obs_starty > display_height:
                        obst_car.obs_starty = 0 - obst_car.obs_height
                        obst_car.obs_startx = random.randrange(0, display_width - obst_car.obs_width)
                        obst_car.obs = random.randrange(0, 5)
                        if len(obstacles) < 10:
                            if new_car.obs == 4:
                                obs_car = ObstacleCar(new_car.obs_startx, new_car.obs_starty, new_car.obs, 36, 102)
                            else:
                                obs_car = ObstacleCar(new_car.obs_startx, new_car.obs_starty, new_car.obs, 32, 64)
                            obstacles.append(obs_car)
                        new_car.obs_starty = obst_car.obs_starty
                        new_car.obs_startx = obst_car.obs_startx
                        new_car.obs = obst_car.obs
                        new_car.obs_height = obst_car.obs_height
                        obs_exist = True
                        passed = passed + 1
                        if int(passed) % 20 == 0:
                            level = level + 1
                            obstacle_speed += 1
                            oil_speed += 1
                        break
                if obs_exist == False:
                    if new_car.obs == 4:
                        obs_car = ObstacleCar(new_car.obs_startx, new_car.obs_starty, new_car.obs, 36, 102)
                    else:
                        obs_car = ObstacleCar(new_car.obs_startx, new_car.obs_starty, new_car.obs, 32, 64)
                    obstacles.append(obs_car)
                    new_car.obs_starty = 0 - obs_car.obs_height
                    new_car.obs_startx = random.randrange(0, display_width - obs_car.obs_width)
                    new_car.obs = random.randrange(0, 5)
                    new_car.obs_height = obs_car.obs_height

        for obst_car in obstacles:
            player1.check_obstacle_colision(obst_car, gamedisplays, bom)
            player2.check_obstacle_colision(obst_car, gamedisplays, bom)

        pygame.display.update()
        clock.tick(60)

intro_loop()
#game_loop()
pygame.quit()
quit()
