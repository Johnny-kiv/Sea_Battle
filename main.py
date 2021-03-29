import pygame
import random
import os
import time
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
        a=random.randint(0,600)
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (1000 / 6, 600 / a)
    def update(self):
        b=random.randint(0,600)
        self.rect.x -= 1
        if self.rect.x<0 or touch_t():
            self.rect.x=1000
            self.rect.y=b
class  Torpedo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (player.rect.x+175, player.rect.y+15)
    def update(self):
        self.rect.x += 1
        if self.rect.x > 1000:
            torpedo.rect.center = (player.rect.x + 175, player.rect.y + 15)

def touch_t():
    xe1=enemy.rect.y
    xe2=enemy.rect.y-34.5
    xt1=torpedo.rect.y-10
    xt2=torpedo.rect.y+10
    ye=enemy.rect.x-50
    yt=torpedo.rect.x+175-25
    if ye<=yt and  xe1>=xt1  and xe1<=xt2:
        return True
    else:
        return False
def touch_p():
    xe1=enemy.rect.y
    xe2=enemy.rect.y-34.5
    xp1=player.rect.y-13.5
    xp2=player.rect.y+13.5
    ye=enemy.rect.x-50
    yp=player.rect.x+175-75
    if ye<=yp and  xe1>=xp1  and xe1<=xp2:
        return True
    else:
        return False

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
torpedo_sprite = pygame.sprite.Group()
torpedo = Torpedo()
torpedo_sprite.add(torpedo)
victory=0
bad=0
fontObj = pygame.font.Font('freesansbold.ttf',26)
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False
    screen.blit(background_image, (0, 0))

    sprite_player.update()
    sprite_enemy.update()
    keydown = pygame.key.get_pressed()
    if touch_t():
        victory=victory+1
        torpedo.rect.center = (player.rect.x + 175, player.rect.y + 15)

    if torpedo.rect.right > 1000:
        bad=bad+1
        torpedo.rect.center = (player.rect.x + 175, player.rect.y + 15)
    if touch_p():
        flRunning=False
    if keydown[pygame.K_SPACE]:

        torpedo_sprite.update()

        torpedo_sprite.draw(screen)
    sprite_player.draw(screen)
    sprite_enemy.draw(screen)

    textSurfaceObj = fontObj.render(str(victory), True, BLACK, GREEN)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (50, 50)
    screen.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = fontObj.render(str(bad), True, BLACK,RED )
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (980, 50)
    screen.blit(textSurfaceObj, textRectObj)
    pygame.display.flip()
pygame.quit()
