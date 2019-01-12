import sys
import keyboard
import pygame
from Game import Game
from Constants import *
from Car import Car

pygame.init()

class CrazyCars:
    def __init__(self, game):
        self.game = game

    def intro_loop(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()

            gamedisplays.fill(gray)
            largetext = pygame.font.Font('freesansbold.ttf', 95)
            TextSurf, TextRect = self.text_objects("CRAZY CARS", largetext)
            TextRect.center = (400, 100)
            gamedisplays.fill(gray3)
            imag = pygame.transform.scale(image1, (800, 600))
            gamedisplays.blit(imag, (0, 100))
            gamedisplays.blit(TextSurf, TextRect)
            if keyboard.is_pressed('SPACE'):
                self.game.game_loop()
            self.button("START", 390, 234, 70, 40, red, yellow, "play")
            self.button("TOURNAMENT", 330, 280, 190, 40, yellow, red, "tournament")
            self.button("QUIT", 430, 630, 200, 50, gray2, gray3, "quit")
            self.button("INSTRUCTION", 210, 630, 200, 50, gray2, gray3, "intro")
            pygame.display.update()
            clock.tick(50)

    def button(self, msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(gamedisplays, ac, (x, y, w, h))

            if click[0] == 1 and action != None:
                if action == "play":
                    player1 = Car(display_width * 0.65, display_height * 0.8, carimg_player1, carimg_player1_left,
                                  carimg_player1_right, carspeed_player1, carspeed_player1_left, carspeed_player1_right,
                                  "Player 1")
                    player2 = Car(display_width * 0.30, display_height * 0.8, carimg_player2, carimg_player2_left,
                                  carimg_player2_right, carspeed_player2, carspeed_player2_left, carspeed_player2_right,
                                  "Player 2")
                    self.game.game_loop(player1, player2)
                elif action == "tournament":
                    final_player1 = None
                    final_player2 = None
                    player1 = Car(display_width * 0.65, display_height * 0.8, carimg_player1, carimg_player1_left,
                                  carimg_player1_right, carspeed_player1, carspeed_player1_left, carspeed_player1_right,
                                  "Ime 1")
                    player2 = Car(display_width * 0.30, display_height * 0.8, carimg_player2, carimg_player2_left,
                                  carimg_player2_right, carspeed_player2, carspeed_player2_left, carspeed_player2_right,
                                  "Ime 2")
                    winner1 = self.game.game_loop(player1, player2)
                    player3 = Car(display_width * 0.65, display_height * 0.8, carimg_player1, carimg_player1_left,
                                  carimg_player1_right, carspeed_player1, carspeed_player1_left, carspeed_player1_right,
                                  "Ime 3")
                    player4 = Car(display_width * 0.30, display_height * 0.8, carimg_player2, carimg_player2_left,
                                  carimg_player2_right, carspeed_player2, carspeed_player2_left, carspeed_player2_right,
                                  "Ime 4")
                    winner2 = self.game.game_loop(player3, player4)

                    if winner1 is player1.name:
                        final_player1 = player1
                    else:
                        final_player1 = player2

                    if winner2 is player3.name:
                        final_player2 = player3
                    else:
                        final_player2 = player4

                    final_player1.reset_values(display_width * 0.65, display_height * 0.8, carimg_player1, carimg_player1_left,
                                  carimg_player1_right, carspeed_player1, carspeed_player1_left, carspeed_player1_right)
                    final_player2.reset_values(display_width * 0.30, display_height * 0.8, carimg_player2, carimg_player2_left,
                                  carimg_player2_right, carspeed_player2, carspeed_player2_left, carspeed_player2_right)
                    self.game.game_loop(final_player1, final_player2)
                elif action == "quit":
                    pygame.quit()
                    quit()
                    sys.exit()
                elif action == "intro":
                    self.introduction()
                elif action == "menu":
                    self.intro_loop()
        else:
            pygame.draw.rect(gamedisplays, ic, (x, y, w, h))

        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        textsurf, textrect = self.text_objects(msg, smalltext)
        textrect.center = ((x + (w / 2)), (y + (h / 2)))
        gamedisplays.blit(textsurf, textrect)

    def introduction(self):
        introduction = True

        while introduction:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()

            gamedisplays.fill(gray)
            largetext = pygame.font.Font('freesansbold.ttf', 80)
            smalltext = pygame.font.Font('freesansbold.ttf', 20)
            mediumtext = pygame.font.Font('freesansbold.ttf', 40)
            TextSurf, TextRect = self.text_objects("INSTRUCTION", largetext)
            TextRect.center = ((400), (100))
            gamedisplays.blit(TextSurf, TextRect)
            stextSurf, stextRect = self.text_objects("PLAYER 1", smalltext)
            stextRect.center = ((210), (300))
            stextSurf2, stextRect2 = self.text_objects("PLAYER 2", smalltext)
            stextRect2.center = ((555), (300))
            sTextSurf, sTextRect = self.text_objects("CONTROLS", mediumtext)
            sTextRect.center = ((400), (200))
            gamedisplays.blit(sTextSurf, sTextRect)

            gamedisplays.blit(stextSurf, stextRect)
            gamedisplays.blit(stextSurf2, stextRect2)
            control1 = pygame.transform.scale(udlf, (300, 192))
            gamedisplays.blit(control1, (50, 350))
            gamedisplays.blit(wasd, (420, 350))
            self.button("BACK", 320, 600, 100, 50, gray2, gray, "menu")
            pygame.display.update()
            clock.tick(30)

    def text_objects(self, text, font):
        textsurface = font.render(text, True, white)
        return  textsurface, textsurface.get_rect()


if __name__ == '__main__':

    game = Game(800, 700)
    new_game = CrazyCars(game)

    new_game.intro_loop()
    pygame.quit()
    quit()
