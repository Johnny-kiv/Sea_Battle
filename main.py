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
good_img = pygame.image.load(os.path.join(img_folder, 'good.png'))
bad_img = pygame.image.load(os.path.join(img_folder, 'bad.png'))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY=(160,160,160)
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
        global xp
        xp=player.rect.x+130
        global yp
        yp=player.rect.y+15
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 10))
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.center = (xp, yp)
    def update(self):
        self.rect.x +=distance


class Good(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        a1 = random.randint(1, 9)
        self.image = good_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)

class Bad(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        a1 = random.randint(1, 9)
        self.image = bad_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (1100, 50)
def touch():
    xa1=torpedo.rect.y
    xa2=torpedo.rect.y-5
    xk1=ship.rect.y-34.5
    xk2=ship.rect.y+34.5
    ya=torpedo.rect.x-50
    yk=ship.rect.x-25
    if ya<=yk and  xa2>=xk1  and xa2<=xk2:
        return True
    else:
        return False
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basket")
clock = pygame.time.Clock()
background_image = pygame.image.load('images/Sea.png')
all_sprites = pygame.sprite.Group()
running = True
FPS=10
all_sprites = pygame.sprite.Group()
ship = Ship()
all_sprites.add(ship)
all_sprites2= pygame.sprite.Group()
player = Player()
all_sprites2.add(player)
all_sprites4= pygame.sprite.Group()
good = Good()
all_sprites4.add(good)
all_sprites5= pygame.sprite.Group()
bad = Bad()
all_sprites5.add(bad)
distance=0
victory=0
miss=0

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
    all_sprites4.draw(screen)
    all_sprites5.draw(screen)
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_SPACE]:
        distance = distance + 50
        all_sprites3 = pygame.sprite.Group()
        torpedo = Torpedo()
        all_sprites3.add(torpedo)
        all_sprites3.update()
        if torpedo.rect.x>WIDTH:
            distance=0
            miss=miss+1

        all_sprites3.draw(screen)
        if touch():
            distance=0
            victory=victory+1
            print(victory)
    """fontObj = pygame.font.Font('freesansbold.ttf', 26)
    textSurfaceObj = fontObj.render(str(miss), True, BLACK, RED)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (50, 50)
    screen.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = fontObj.render(str(victory), True, BLACK, GREEN)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (1150, 50)
    screen.blit(textSurfaceObj, textRectObj)"""
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
pygame.quit()