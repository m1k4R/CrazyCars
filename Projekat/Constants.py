import  pygame

display_width = 800
display_height = 700
car_width = 32
car_height = 64
gamedisplays = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
white = (255, 255, 255)
gray = (119, 118, 110)
bright_blue = (0, 0, 255)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)
green = (0, 200, 0)
red = (255, 0, 0)
blue = (0, 0, 200)
gray2 = (186, 186, 186,0)
gray3 = (114, 114, 114)
yellow = (255, 207, 49)
image1 = pygame.image.load('image1.jpg')
pygame.display.set_caption("crazy cars")
carimg_player1 = pygame.image.load('car1.png')
carimg_player1_left = pygame.image.load('car1l.png')
carimg_player1_right = pygame.image.load('car1r.png')
carimg_player2 = pygame.image.load('car2.png')
carimg_player2_left = pygame.image.load('car2l.png')
carimg_player2_right = pygame.image.load('car2r.png')
white_strip = pygame.image.load('line.png')
boom = pygame.image.load('boom.png')
bom = pygame.image.load('bom.png')
level_img = pygame.image.load('linelevel.png')
udlf = pygame.image.load('udlr.png')
wasd = pygame.image.load('wasd.png')