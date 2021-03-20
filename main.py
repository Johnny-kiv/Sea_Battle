import pygame
import os
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
apple_img = pygame.image.load(os.path.join(img_folder, 'gm_ship.png'))
player_img = pygame.image.load(os.path.join(img_folder, 'player.png'))
good_img = pygame.image.load(os.path.join(img_folder, 'good.png'))
bad_img = pygame.image.load(os.path.join(img_folder, 'bad.png'))
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (1000 / 2, 600 / 2)

screen = pygame.display.set_mode((1000, 600))
FPS = 60
flRunning = True
pygame.display.set_caption("Sea Battle")
pygame.display.set_icon(pygame.image.load("./images/icon.jpg"))
background_image = pygame.image.load('images/Sea.jpg')

sprite_player = pygame.sprite.Group()
player=Player()
sprite_player.add(player)
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False
    screen.blit(background_image, (0, 0))


    sprite_player.draw(screen)
    pygame.display.flip()
pygame.quit()
