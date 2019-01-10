import pygame
import time
import random


class ObstacleCar:
    def __init__(self, obs_startx, obs_starty, obs, obs_width, obs_height):
        self.obs_startx = obs_startx
        self.obs_starty = obs_starty
        self.obs = obs
        self.obs_width = obs_width
        self.obs_height = obs_height

    def move_obstacle(self, obstacle_speed, gamedisplays):
        self.obs_starty += (obstacle_speed / 4)
        self.show_obstacle(self.obs_startx, self.obs_starty, self.obs, gamedisplays)
        self.obs_starty += obstacle_speed

    def show_obstacle(self, obs_startx, obs_starty, obs, gamedisplays):
        self.obs_startx = obs_startx
        self.obs_starty = obs_starty
        if obs == 0:
            self.obs_pic = pygame.image.load("car3.png")
        elif obs == 1:
            self.obs_pic = pygame.image.load("car4.png")
        elif obs == 2:
            self.obs_pic = pygame.image.load("car5.png")
        elif obs == 3:
            self.obs_pic = pygame.image.load("car6.png")
        elif obs == 4:
            self.obs_pic = pygame.image.load("car7.png")
        gamedisplays.blit(self.obs_pic, (self.obs_startx, self.obs_starty))
