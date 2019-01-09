import pygame
import time
import random


class Oil:
    def __init__(self, oil_startx, oil_starty, oil, oil_width, oil_height):
        self.oil_startx = oil_startx
        self.oil_starty = oil_starty
        self.oil = oil
        self.oil_width = oil_width
        self.oil_height = oil_height

    def move_oil_obstacle(self, oil_speed, gamedisplays):
        self.oil_starty += (oil_speed / 4)
        self.show_oil_obstacle(self.oil_startx, self.oil_starty, self.oil, gamedisplays)
        self.oil_starty += oil_speed

    def show_oil_obstacle(self, oil_startx, oil_starty, oil, gamedisplays):
        self.oil_startx = oil_startx
        self.oil_starty = oil_starty
        if oil == 0:
            self.oil_pic = pygame.image.load("oil.png")
        elif oil == 1:
            self.oil_pic = pygame.image.load("oill.png")
        gamedisplays.blit(self.oil_pic, (self.oil_startx, self.oil_starty))