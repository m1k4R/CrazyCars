import pygame
import time
import random


class Car:
    def __init__(self, x, y, car_img, car_img_left, car_img_right):
        self.x = x
        self.y = y
        self.car_img = car_img
        self.x_change = 0
        self.y_change = 0
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.life = 3
        self.images = [car_img, car_img_left, car_img_right]
        self.width = 32
        self.height = 64

    def show_car(self, gamedisplays):
        gamedisplays.blit(self.car_img, (self.x, self.y))

    def move_control(self):
        if self.left == False and self.right == False:
            self.x_change = 0
        if self.up == False and self.down == False:
            self.y_change = 0
        if self.up == False and self.down == True:
            self.y_change = 5
        if self.up == True and self.down == False:
            self.y_change = -5
        if self.left == False and self.right == True:
            self.x_change = 5
        if self.left == True and self.right == False:
            self.x_change = -5

    def check_border(self, display_width, display_height):
        if self.x <= 1 or self.x >= display_width - self.width:
            self.x -= self.x_change
        if self.y <= 60 or self.y >= display_height - self.height:
            self.y -= self.y_change

    def check_another_player_colision(self, player2):
        if self.y >= player2.y and self.y <= player2.y + player2.height or self.y + self.height >= player2.y and self.y + self.height <= player2.y + player2.height:
            if self.x >= player2.x and self.x <= player2.x + player2.width or self.x + self.width >= player2.x and self.x + self.width <= player2.x + player2.width:
                self.x -= self.x_change
                self.y -= self.y_change

    def check_oil_colision(self, obst_oil):
        if self.y > obst_oil.oil_starty and self.y < obst_oil.oil_starty + obst_oil.oil_height or self.y + self.height > obst_oil.oil_starty and self.y + self.height < obst_oil.oil_starty + obst_oil.oil_height:
            if self.x > obst_oil.oil_startx and self.x < obst_oil.oil_startx + obst_oil.oil_width or self.x + self.width > obst_oil.oil_startx and self.x + self.width < obst_oil.oil_startx + obst_oil.oil_width:
                self.x -= self.x_change
                self.y -= self.y_change

    def check_obstacle_colision(self, obst_car, gamedisplays, bom):
        if self.y > obst_car.obs_starty and self.y < obst_car.obs_starty + obst_car.obs_height or self.y + self.height > obst_car.obs_starty and self.y + self.height < obst_car.obs_starty + obst_car.obs_height:
            if self.x > obst_car.obs_startx and self.x < obst_car.obs_startx + obst_car.obs_width or self.x + self.width > obst_car.obs_startx and self.x + self.width < obst_car.obs_startx + obst_car.obs_width:
                if self.life <= 1.5:
                    self.x = -500
                    self.y = -500
                else:
                    self.life -= 0.1
                    gamedisplays.blit(bom, (self.x - 10, self.y - 10))