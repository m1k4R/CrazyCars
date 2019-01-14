import pygame
import time
import random
import keyboard
import threading

from Car import Car
from ObstacleOil import Oil
from ObstacleCar import ObstacleCar
from Bonus import Bonus
from Constants import *
from multiprocessing import Process
import multiprocessing

pygame.init()


class Game:
    def __init__(self, display_width, display_height):
        self.display_width = display_width
        self.display_height = display_height
        self.obstacle_speed = 3
        self.obstacles = []
        self.oil_speed = 2.5
        self.bonus_speed = 2.5
        self.oils = []
        self.bumped = False
        self.passed = 0
        self.level = 0
        self.game = 1
        self.oil_height = 107
        self.obs_width = 32
        self.obs_exist = False
        self.oil_exist = False
        self.lines = []
        self.queue = multiprocessing.Queue()
        self.p = Process(target=GetLinesCoordinates, args=(self.queue,))
        self.p.start()

    def score_level_system(self, passed, level):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Passed: " + str(passed), True, white)
        font_level = pygame.font.SysFont(None, 35)
        text_level = font_level.render("LEVEL", True, white)
        txt_level = font_level.render(str(level), True, white)
        gamedisplays.blit(text, (5, 680))
        gamedisplays.blit(text_level, (350, 7))
        gamedisplays.blit(level_img, (340, 35))
        gamedisplays.blit(txt_level, (380, 44))

    def text_objects(self, text, font):
        textsurface = font.render(text, True, white)
        return  textsurface, textsurface.get_rect()

    def message_life_player(self, player1, player2):
        largetext = pygame.font.Font("freesansbold.ttf", 20)
        textsurf1, textrect1 = self.text_objects(player2, largetext)
        textsurf2, textrect2 = self.text_objects(player1, largetext)
        gamedisplays.blit(textsurf1, (20, 10))
        gamedisplays.blit(textsurf2, (700, 10))

    def message_display(self, text):
        largetext3 = pygame.font.Font("freesansbold.ttf", 64)
        textsurf3, textrect3 = self.text_objects(text, largetext3)
        textrect3.center = ((display_width / 2), (display_height / 2))
        gamedisplays.blit(textsurf3, textrect3)
        pygame.display.update()
        time.sleep(3)

    def life_player1(self, number):
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

    def life_player2(self, number):
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

    def background(self, rel_y):
        white_strip = pygame.image.load('line.png')
        counter1 = 0
        counter2 = 1
        if len((self.lines)) > 48:
            self.p.terminate()
            for x in range(48):
                gamedisplays.blit(white_strip, (self.lines[counter1], rel_y + self.lines[counter2]))
                counter1 += 2
                counter2 += 2

    def update_background(self):
        while not self.queue.empty():
            a = self.queue.get()
            self.lines.append(a)
            b = self.queue.get()
            self.lines.append(b)

    def crash(self, winner):
        self.message_display("WINNER IS: " + winner)
        return True

    def reset_game(self):
        self.oils[:] = []
        self.obstacles[:] = []
        self.level = 0
        self.passed = 0
        self.obstacle_speed = 3
        self.oil_speed = 2.5
        self.bonus_speed = 2.5
        self.oil_exist = False
        self.obs_exist = False

    def game_loop(self, pl1, pl2):
        player1 = pl1
        player2 = pl2
        self.reset_game()
        obs_width = 32
        pom = 7
        obs_startx = random.randrange(0, display_width - obs_width)
        oil_startx = random.randrange(0, display_width)
        bonus_startx = random.randrange(31, display_width - 31)
        new_car = ObstacleCar(obs_startx, 0, 0, 32, 64)
        new_oil = Oil(oil_startx, 0, 0, 114, 107)
        bonus = Bonus(bonus_img, 30, 31, bonus_startx, 0)
        t = threading.Thread(target=self.update_background)
        t.start()
        bumped = False
        time.sleep(1)
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
                        if player1.bonus is True:
                            player1.car_img = player1.images[3]
                        else:
                            player1.car_img = player1.images[0]
                    if event.key == pygame.K_RIGHT:
                        player1.right = False
                        if player1.bonus is True:
                            player1.car_img = player1.images[3]
                        else:
                            player1.car_img = player1.images[0]
                    if event.key == pygame.K_UP:
                        player1.up = False
                    if event.key == pygame.K_DOWN:
                        player1.down = False
                    if event.key == pygame.K_a:
                        player2.left = False
                        if player2.bonus is True:
                            player2.car_img = player2.images[3]
                        else:
                            player2.car_img = player2.images[0]
                    if event.key == pygame.K_d:
                        player2.right = False
                        if player2.bonus is True:
                            player2.car_img = player2.images[3]
                        else:
                            player2.car_img = player2.images[0]
                    if event.key == pygame.K_w:
                        player2.up = False
                    if event.key == pygame.K_s:
                        player2.down = False

                    player1.move_control()
                    player2.move_control()

            player1.check_bonus(bonus)
            player2.check_bonus(bonus)
            player1.start_bonus()
            player2.start_bonus()

            for obst_oil in self.oils:
                player1.check_oil_colision(obst_oil)
                player2.check_oil_colision(obst_oil)

            player1.apply_oil()
            player2.apply_oil()

            player1.x += player1.x_change
            player1.y += player1.y_change
            player2.x += player2.x_change
            player2.y += player2.y_change

            gamedisplays.fill(gray)
            rel_y = pom % 300
            if rel_y < 800:
                self.background(rel_y)
            pom += self.obstacle_speed

            # Pomjeranje nafte
            for obst_oil in self.oils:
                obst_oil.move_oil_obstacle(self.oil_speed, gamedisplays)
            new_oil.move_oil_obstacle(self.oil_speed, gamedisplays)

            # pomjeranje bonusa
            if bonus.bonus_starty > display_height:
                bonus.bonus_startx = random.randrange(31, display_width - 31)
                bonus.bonus_starty = 0 - 350
            bonus.move_bonus(self.bonus_speed, gamedisplays)

            # Pomjeranje autica
            for obst_car in self.obstacles:
                obst_car.move_obstacle(self.obstacle_speed, gamedisplays)
            new_car.move_obstacle(self.obstacle_speed, gamedisplays)

            self.t_start_game(player1, player2, self.oils, self.obstacles)

            self.draw_display(player1, player2)

            if player1.life <= 1.5 or player2.life <= 1.5:
                if player1.life <= 1.5:
                    bumped = self.crash(player2.name)
                else:
                    bumped = self.crash(player1.name)

            self.t_create_obstacles(new_oil, self.oils, new_car, self.obstacles, self.passed, self.level,self.obstacle_speed, self.oil_speed, self.obs_exist, self.oil_exist)

            pygame.display.update()
            clock.tick(60)

        if player1.life <= 1.5:
            return player2.name
        else:
            return player1.name

    def t_start_game(self, player1, player2, oils, obstacles):
        t = threading.Thread(target=self.start_player, args=(player1, player2, oils, obstacles))
        t1 = threading.Thread(target=self.start_player, args=(player2, player1, oils, obstacles))
        t.start()
        t1.start()

    def t_create_obstacles(self, new_oil, oils, new_car, obstacles, passed, level, obstacle_speed, oil_speed, obs_exist,oil_exist):
        t = threading.Thread(target=self.create_oil_obstacles, args=(new_oil, oils, oil_exist))
        t1 = threading.Thread(target=self.create_car_obstacles,args=(new_car, obstacles, passed, level, obstacle_speed, oil_speed, obs_exist))
        t.start()
        t1.start()

    def start_player(self, player, player2, oils, obstacles):
        if player.life > 1.5:
            player.show_car(gamedisplays)
        player.check_border(display_width, display_height)
        player.check_another_player_colision(player2)
        for obst_car in obstacles:
            player.check_obstacle_colision(obst_car, gamedisplays, bom)

    def create_oil_obstacles(self, new_oil, oils, oil_exist):
        if new_oil.oil_starty > new_oil.oil_height:
            for obst_oil in oils:
                if obst_oil.oil_starty > display_height:
                    obst_oil.oil_starty = 0 - obst_oil.oil_height
                    obst_oil.oil_startx = random.randrange(0, display_width)
                    obst_oil.oil = random.randrange(0, 2)
                    if len(self.oils) < 10:
                        if new_oil.oil == 0:
                            obs_oil = Oil(new_oil.oil_startx, new_oil.oil_starty, new_oil.oil, 114, 107)
                        else:
                            obs_oil = Oil(new_oil.oil_startx, new_oil.oil_starty, new_oil.oil, 78, 62)
                        self.oils.append(obs_oil)
                    new_oil.oil_starty = obst_oil.oil_starty
                    new_oil.oil_startx = obst_oil.oil_startx
                    new_oil.oil = obst_oil.oil
                    self.oil_exist = True
                    break
            if self.oil_exist == False:
                if new_oil.oil == 0:
                    obs_oil = Oil(new_oil.oil_startx, new_oil.oil_starty, new_oil.oil, 114, 107)
                else:
                    obs_oil = Oil(new_oil.oil_startx, new_oil.oil_starty, new_oil.oil, 78, 62)
                self.oils.append(obs_oil)
                new_oil.oil_starty = 0 - new_oil.oil_height
                new_oil.oil_startx = random.randrange(0, display_width)
                new_oil.oil = random.randrange(0, 2)

    def create_car_obstacles(self, new_car, obstacles, passed, level, obstacle_speed, oil_speed, obs_exist):
        if new_car.obs_starty > new_car.obs_height:
            for obst_car in obstacles:
                if obst_car.obs_starty > display_height:
                    obst_car.obs_starty = 0 - obst_car.obs_height
                    obst_car.obs_startx = random.randrange(0, display_width - obst_car.obs_width)
                    obst_car.obs = random.randrange(0, 5)
                    if len(self.obstacles) < 10:
                        if new_car.obs == 4:
                            obs_car = ObstacleCar(new_car.obs_startx, new_car.obs_starty, new_car.obs, 36, 102)
                        else:
                            obs_car = ObstacleCar(new_car.obs_startx, new_car.obs_starty, new_car.obs, 32, 64)
                        self.obstacles.append(obs_car)
                    new_car.obs_starty = obst_car.obs_starty
                    new_car.obs_startx = obst_car.obs_startx
                    new_car.obs = obst_car.obs
                    new_car.obs_height = obst_car.obs_height
                    self.obs_exist = True
                    self.passed = self.passed + 1
                    if int(self.passed) % 20 == 0:
                        self.level = self.level + 1
                        self.obstacle_speed += 1
                        self.oil_speed += 1
                        self.bonus_speed += 1
                    break
            if self.obs_exist == False:
                if new_car.obs == 4:
                    obs_car = ObstacleCar(new_car.obs_startx, new_car.obs_starty, new_car.obs, 36, 102)
                else:
                    obs_car = ObstacleCar(new_car.obs_startx, new_car.obs_starty, new_car.obs, 32, 64)
                self.obstacles.append(obs_car)
                new_car.obs_starty = 0 - obs_car.obs_height
                new_car.obs_startx = random.randrange(0, display_width - obs_car.obs_width)
                new_car.obs = random.randrange(0, 5)
                new_car.obs_height = obs_car.obs_height

    def draw_display(self, player1, player2):
        self.message_life_player(player1.name, player2.name)
        self.life_player1(player1.life)
        self.life_player2(player2.life)
        self.score_level_system(self.passed, self.level)


def GetLinesCoordinates(queue):
    x = 120
    y = 0
    count = 0
    while 1:
        count += 1
        queue.put(x)
        queue.put(y)

        if count == 6:
            y -= 1050
        elif count == 7:
            y += 150
        elif count == 8:
            x += 120
            y = 0
            count = 0
        else:
            y += 150