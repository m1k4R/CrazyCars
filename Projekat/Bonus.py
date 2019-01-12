import pygame

class Bonus:

    def __init__(self, image, height, width, bonus_startx, bonus_starty):
        self.image = image
        self.height = height
        self.width = width
        self.bonus_startx = bonus_startx
        self.bonus_starty = bonus_starty


    def move_bonus(self, bonus_speed, gamedisplays):
        self.bonus_starty += (bonus_speed / 4)
        gamedisplays.blit(self.image, (self.bonus_startx, self.bonus_starty))
        self.bonus_starty += bonus_speed