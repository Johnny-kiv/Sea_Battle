import pygame
import os
import time
import random
WIDTH=1161
HEIGHT=650
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
apple_img = pygame.image.load(os.path.join(img_folder, 'gm_ship.png'))
buscet_img = pygame.image.load(os.path.join(img_folder, 'player.png'))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        a=random.randint(1,9)
        b=random.randint(6,9)

        pygame.sprite.Sprite.__init__(self)
        self.image = apple_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / b, HEIGHT / a)
    def update(self):
        y=random.randint(10,600)
        x = random.randint(10, 1150)
        self.rect.y = y
        self.rect.x = x

class Player(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = buscet_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 10, HEIGHT / 1.300 )

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_DOWN]:
            self.rect.y += 50
        if keystate[pygame.K_UP]:
            self.rect.y += -50
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 650:
            self.rect.bottom = 650
class Torpedo(pygame.sprite.Sprite):
    def __init__(self):
        xp=player.rect.x
        yp=player.rect.y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (xp, yp)
    def update(self):
        self.rect.x +=900
def touch():
    xa1=apple.rect.x
    xa2=apple.rect.x-51
    xk1=player.rect.x-76.5
    xk2=player.rect.x+76.5
    ya=apple.rect.y-52
    yk=player.rect.y-47.5
    if ya<=yk and  xa1>=xk1  and xa1<=xk2:
        return True
    else:
        return False
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basket")
clock = pygame.time.Clock()
background_image = pygame.image.load('images/Sea.png')
all_sprites = pygame.sprite.Group()
running = True
FPS=2
all_sprites = pygame.sprite.Group()
ship = Ship()
all_sprites.add(ship)
all_sprites2= pygame.sprite.Group()
player = Player()
all_sprites2.add(player)

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
    all_sprites.update()
    keystate = pygame.key.get_pressed()



    if keystate[pygame.K_SPACE]:
        all_sprites3 = pygame.sprite.Group()
        torpedo = Torpedo()
        all_sprites3.add(torpedo)
        all_sprites3.update()
        all_sprites3.draw(screen)
        if touch():
            print("Есть касание")
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
pygame.quit()