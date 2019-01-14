import sys
import keyboard
import pygame
from Game import Game
from Constants import *
from Car import Car
from InputBox import InputBox

pygame.init()

class CrazyCars:
    def __init__(self, game):
        self.game = game
        self.input_boxes = []

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
                player1 = Car(display_width * 0.65, display_height * 0.8, carimg_player1, carimg_player1_left,
                              carimg_player1_right, carspeed_player1, carspeed_player1_left, carspeed_player1_right,
                              "Player 1")
                player2 = Car(display_width * 0.30, display_height * 0.8, carimg_player2, carimg_player2_left,
                              carimg_player2_right, carspeed_player2, carspeed_player2_left, carspeed_player2_right,
                              "Player 2")
                self.game.game_loop(player1, player2)
            self.button("START", 390, 234, 70, 40, red, yellow, "play")
            self.button("TOURNAMENT", 330, 280, 190, 40, red, yellow, "tournament")
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
                    self.get_names()
                elif action == "play2":
                    final_player1 = None
                    final_player2 = None
                    ime1 = self.input_boxes[0]
                    ime2 = self.input_boxes[1]
                    ime3 = self.input_boxes[2]
                    ime4 = self.input_boxes[3]
                    player1 = Car(display_width * 0.65, display_height * 0.8, carimg_player1, carimg_player1_left,
                                  carimg_player1_right, carspeed_player1, carspeed_player1_left, carspeed_player1_right,
                                  ime1.text)
                    player2 = Car(display_width * 0.30, display_height * 0.8, carimg_player2, carimg_player2_left,
                                  carimg_player2_right, carspeed_player2, carspeed_player2_left, carspeed_player2_right,
                                  ime2.text)
                    winner1 = self.game.game_loop(player1, player2)
                    player3 = Car(display_width * 0.65, display_height * 0.8, carimg_player1, carimg_player1_left,
                                  carimg_player1_right, carspeed_player1, carspeed_player1_left, carspeed_player1_right,
                                  ime3.text)
                    player4 = Car(display_width * 0.30, display_height * 0.8, carimg_player2, carimg_player2_left,
                                  carimg_player2_right, carspeed_player2, carspeed_player2_left, carspeed_player2_right,
                                  ime4.text)
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
                    self.intro_loop()
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

    def get_names(self):
        get_names = True
        input_box1 = InputBox(100, 250, 140, 32)
        input_box2 = InputBox(500, 250, 140, 32)
        input_box3 = InputBox(100, 500, 140, 32)
        input_box4 = InputBox(500, 500, 140, 32)

        self.input_boxes = [input_box1, input_box2, input_box3, input_box4]

        while get_names:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
                for box in self.input_boxes:
                    box.handle_event(event)
            gamedisplays.fill(gray)

            for box in self.input_boxes:
                box.update()

            gamedisplays.fill((30, 30, 30))
            for box in self.input_boxes:
                box.draw(gamedisplays)

            #pygame.display.flip()
            gamedisplays.blit(p1, (70, 50))
            gamedisplays.blit(p3, (460, 50))
            gamedisplays.blit(p2, (70, 300))
            gamedisplays.blit(p4, (460, 300))

            largetext = pygame.font.Font('freesansbold.ttf', 40)
            TextSurf, TextRect = self.text_objects("VS", largetext)
            TextRect.center = ((400), (200))
            gamedisplays.blit(TextSurf, TextRect)

            largetext = pygame.font.Font('freesansbold.ttf', 40)
            TextSurf, TextRect = self.text_objects("VS", largetext)
            TextRect.center = ((400), (450))
            gamedisplays.blit(TextSurf, TextRect)

            self.button("PLAY", 300, 630, 200, 50, gray2, gray3, "play2")
            pygame.display.update()
            clock.tick(30)

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
