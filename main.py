import pygame
import os
import random
import time
WIDTH=1161
HEIGHT=650
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
apple_img = pygame.image.load(os.path.join(img_folder, 'USA.png'))
buscet_img = pygame.image.load(os.path.join(img_folder, 'player.png'))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
class USA(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = apple_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 28, HEIGHT / 4)
    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            self.rect.x += 100
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = buscet_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 1.300 )

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -150
        if keystate[pygame.K_RIGHT]:
            self.speedx = 150
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
class TORPEDO(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 1.300 )
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basket")
clock = pygame.time.Clock()
background_image = pygame.image.load('images/Sea.png')
all_sprites = pygame.sprite.Group()
running = True
FPS=10
all_sprites = pygame.sprite.Group()
apple = USA()
all_sprites.add(apple)
all_sprites2= pygame.sprite.Group()
player = Player()
all_sprites2.add(player)
all_sprites3= pygame.sprite.Group()
torpedo = TORPEDO()
all_sprites3.add(torpedo)
while running:

    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background_image, (0, 0))
    all_sprites2.update()
    all_sprites.draw(screen)
    all_sprites2.draw(screen)
    all_sprites3.draw(screen)
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_SPACE]:
        all_sprites.update()

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
pygame.quit()