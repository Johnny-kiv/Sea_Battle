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
enemy_img = pygame.image.load(os.path.join(img_folder, 'gm_ship.png'))
player_img = pygame.image.load(os.path.join(img_folder, 'player.png'))
good_img = pygame.image.load(os.path.join(img_folder, 'good.png'))
bad_img = pygame.image.load(os.path.join(img_folder, 'bad.png'))
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (1000 / 6, 600 / 2)
    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.rect.y -= 1
        if keystate[pygame.K_DOWN]:
            self.rect.y += 1
        self.rect.x += self.speedy
        if self.rect.bottom > 600:
            self.rect.bottom = 600
        if self.rect.top < 0:
            self.rect.top = 0
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (1000 / 6, 600 / 2)
    def update(self):
        self.rect.x -= 1
        if self.rect.left> 0:
            self.rect.left = 500
screen = pygame.display.set_mode((1000, 600))
FPS = 60
flRunning = True
pygame.display.set_caption("Sea Battle")
pygame.display.set_icon(pygame.image.load("./images/icon.jpg"))
background_image = pygame.image.load('images/Sea.jpg')


sprite_player = pygame.sprite.Group()
player=Player()
sprite_player.add(player)

sprite_enemy = pygame.sprite.Group()
enemy=Enemy()
sprite_enemy.add(enemy)

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False
    screen.blit(background_image, (0, 0))

    sprite_player.update()
    sprite_enemy.update()
    sprite_player.draw(screen)
    sprite_enemy.draw(screen)
    pygame.display.flip()
pygame.quit()
