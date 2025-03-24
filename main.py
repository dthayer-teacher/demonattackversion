# Pygame template - skeleton for a new pygame project
import pygame
import random
from pygame import mixer

WIDTH = 600
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (238,130,238)
ORANGE = (255,165,0)
NEON_RED = (255, 87, 51)
NEON_BLUE = (31, 81, 255)
NEON_YELLOW = (207, 255, 4)

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)




def draw_shield_bar(surf,x,y,pct,color):
    if pct<0:
        pct=0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct/100)*BAR_LENGTH
    outline_rect = pygame.Rect(x,y,BAR_LENGTH,BAR_HEIGHT)
    fill_rect = pygame.Rect(x,y,fill,BAR_HEIGHT)
    pygame.draw.rect(surf,color,fill_rect)
    pygame.draw.rect(surf,WHITE,outline_rect,2)




font_name = pygame.font.match_font('arial')
def draw_text(surf,text,size,x,y,color):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True,color)
    text_rect = text_surface.get_rect()
    text_rect.midtop=(x,y)
    surf.blit(text_surface,text_rect)


def newmob():
    rock = Mob()
    mobs.add(rock)
    all_sprites.add(rock)

class Power(pygame.sprite.Sprite):
    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)
        #size
        self.width = 10
        self.height = 20
        #shape
        self.type = random.choice(['health','gun'])
        #self.image = pygame.Surface((self.width,self.height))
        self.image = pygame.image.load("shield_bronze.png")
        #self.image.fill(ORANGE)
        if self.type == 'gun':
            self.image = pygame.image.load("bolt_gold.png")
        # self.image = pygame.image.load("laserBlue03.png")
        # self.image = pygame.transform.scale(self.image, (self.width, self.height))
        #rectangle
        self.rect = self.image.get_rect()
        #location on screen
        self.rect.center = center

        #set up move

        self.speedy = 5
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top>HEIGHT:
            self.kill()
class Bullet2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        #size
        self.width = 5
        self.height = 20
        #shape
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(NEON_RED)
        # self.image = pygame.image.load("laserBlue03.png")
        # self.image = pygame.transform.scale(self.image, (self.width, self.height))
        #rectangle
        self.rect = self.image.get_rect()
        #location on screen
        self.rect.centerx = x
        self.rect.bottom = y
        #set up move
        self.speedx =0
        self.speedy = -10
    def update(self):
        # if self.rect.top >= HEIGHT:
        #     self.rect.x = random.randrange(0, WIDTH - self.width)
        #     self.rect.centery = random.randrange(-200, -100)
        #     self.speedy = random.randrange(5, 20)

        self.rect.y -= self.speedy

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        #size
        self.width = 5
        self.height = 20
        #shape
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(NEON_BLUE)
        # self.image = pygame.image.load("laserBlue03.png")
        # self.image = pygame.transform.scale(self.image, (self.width, self.height))
        #rectangle
        self.rect = self.image.get_rect()
        #location on screen
        self.rect.centerx = x
        self.rect.bottom = y
        #set up move
        self.speedx =0
        self.speedy = 10
    def update(self):
        # if self.rect.top >= HEIGHT:
        #     self.rect.x = random.randrange(0, WIDTH - self.width)
        #     self.rect.centery = random.randrange(-200, -100)
        #     self.speedy = random.randrange(5, 20)
        self.rect.y -= self.speedy


class Mob(pygame.sprite.Sprite):
    def __init__(self,side,x,y):
        pygame.sprite.Sprite.__init__(self)
        #size
        self.width = 60
        self.height = 48
        self.meteor_list = []
        #self.load_images()
        #shape
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(RED)
        # self.pick = random.choice(self.meteor_list)
        # self.image = self.pick
        #self.image = pygame.transform.scale(self.image, (self.width, self.height))
        #rectangle
        self.rect = self.image.get_rect()
        #location on screen
        #self.rect.x = random.randrange(0,WIDTH-self.width)
        #self.rect.centery = random.randrange(-200,-100)
        self.x = x
        self.y = y
        self.bound_amt = random.randrange(75,200)
        self.bound_left = self.x - self.bound_amt
        self.bound_right = self.x + self.bound_amt
        if self.bound_left<0:
            self.bound_left +=10
            self.bound_right +=10
        if self.bound_right>WIDTH:
            self.bound_left -=10
            self.bound_right -=10

        self.side = side
        self.rect.x = self.x
        self.speedx = 20
        if self.side == l:
            self.rect.x = x-800
            self.image = pygame.image.load("particles.png")

        if self.side == r:
            self.rect.x = x+800
            self.image = pygame.image.load("particles.png")
        if self.side ==n:
            self.rect.x = self.x
            self.image = pygame.image.load("ship.png")
            self.speedx = 5
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect.y = self.y

        #set up move

        self.speedy = random.randrange(5,20)
        self.speedy = 2
        #self.speedx = random.randrange(5,20)
        self.windowxl = 50
        self.windowxr = 50
        self.hit_right= False
        self.hit_left = False
        self.mob_playing = False
        self.wait = pygame.time.get_ticks()
        self.wait_time = random.randrange(500,1001)
        self.start_direction = random.randint(1,2)
        if self.start_direction==1 and self.side==n:
            self.speedx *=-1
    def load_images(self):
        for i in range(1,11):
            filename = 'meteor_img/meteor{}.png'.format(i)
            img = pygame.image.load(filename)
            self.meteor_list.append(img)
    def update(self):

        # if self.rect.top >= HEIGHT:
        #     self.rect.x = random.randrange(0, WIDTH - self.width)
        #     self.rect.centery = random.randrange(-200, -100)
        #     self.speedy = random.randrange(5, 20)
        if self.side == r:
            self.rect.x -= self.speedx
            if self.rect.x <= self.x:

                ship.create_mob=True
                self.kill()
        if self.side == l:
            self.rect.x += self.speedx
            if self.rect.x >= self.x:
                self.kill()
        if self.side == n:
            self.mob_playing=True
        if self.mob_playing:

            if self.rect.right>=WIDTH-20:
                self.speedx *=-1
            elif self.rect.left<=20:
                self.speedx *=-1
            else:
                #up / down
                if self.rect.y > self.y +50:
                    self.speedy *=-1
                if self.rect.y < self.y - 50:
                    self.speedy *=-1
                #left / right
                if self.rect.right >self.bound_right:
                    self.speedx *=-1
                if self.rect.left<self.bound_left:
                    self.speedx *=-1
                #     if self.hit_left:
                #         self.windowxl -= 25
                #         self.hit_left=False
                #     self.hit_right = True
                #     # self.windowxr += 25
                #     # self.windowxl -=25
                # if self.rect.x <self.x -self.windowxl:
                #     self.speedx *=-1
                #     if self.hit_right:
                #         self.windowxr += 25
                #         self.hit_right=False
                #     self.hit_left = True
                #     # self.windowxr -= 25
                #     # self.windowxl += 25

            self.rect.y += self.speedy
            self.rect.x += self.speedx
            now = pygame.time.get_ticks()
            if now - self.wait > self.wait_time:
                self.wait = now
                b2 = Bullet2(self.rect.centerx,self.rect.bottom)
                all_sprites.add(b2)
                bullets2.add(b2)
class Star(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 3
        self.height = 3
        scale = random.randrange(50,101)
        scale = scale/100
        self.image = pygame.Surface((self.width*scale,self.height*scale))
        self.image.fill(WHITE)
        self.rect=self.image.get_rect()
        self.rect.x = random.randrange(WIDTH)
        self.rect.y = random.randrange(-200,HEIGHT)
        self.twinkly = random.randint(1,10)
        self.flash = pygame.time.get_ticks()
        self.flash_time = random.randrange(2000,5001)
        self.speedy = random.randrange(1,4)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > HEIGHT:
            self.rect.x = random.randrange(WIDTH)
            self.rect.y = random.randrange(-500,-200)
        if self.twinkly <3:
            now = pygame.time.get_ticks()
            if now-self.flash>self.flash_time:
                self.flash = now
                self.image.fill(BLACK)
            else:
                self.image.fill(WHITE)
class Expolosion(pygame.sprite.Sprite):
    def __init__(self,center,size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.width = 40
        self.height = 40
        # Need shooting
        self.expl_anim = {}
        self.expl_anim['sm'] = []
        self.expl_anim['lg'] = []
        self.expl_anim['xl'] = []
        self.load_image()
        # self.image = pygame.Surface((self.width, self.height))
        # self.image.fill(BLUE)
        self.image = self.expl_anim[self.size][0]
        # self.player_img = pygame.image.load('club2.PNG')
        # self.player_img =pygame.transform.scale(self.player_img,(self.width,self.height))
        # self.image=self.player_img
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame=0
        self.frame_rate = 75
        self.last_update = pygame.time.get_ticks()

    def load_image(self):
        for i in range(1,9):
            filename = 'regularExplosion0{}.png'.format(i)
            img = pygame.image.load(filename)
            img_lg = pygame.transform.scale(img,(150,150))
            self.expl_anim['lg'].append(img_lg)
            img_sm = pygame.transform.scale(img, (32, 32))
            self.expl_anim['sm'].append(img_sm)
            img_xl = pygame.transform.scale(img, (300, 300))
            self.expl_anim['xl'].append(img_xl)



    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame +=1
            if self.frame == len(self.expl_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.expl_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class Water(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #size
        self.width = 60
        self.height = 48
        self.water_list = []

        self.load_images()
        #shape
        # self.image = pygame.Surface((self.width,self.height))
        # self.image.fill(RED)
        self.image = self.water_list[0]
        # self.pick = random.choice(self.meteor_list)
        # self.image = self.pick
        #self.image = pygame.transform.scale(self.image, (self.width, self.height))
        #rectangle
        self.rect = self.image.get_rect()
        #location on screen
        #self.rect.x = random.randrange(0,WIDTH-self.width)
        #self.rect.centery = random.randrange(-200,-100)
        self.rect.x = WIDTH-150
        self.rect.y =HEIGHT-200
        self.last_update = 0
        self.current_frame = 0
        self.up = True
        self.speedx = 1
        self.speedy = 1
        self.last_delay = pygame.time.get_ticks()
        self.moving=True
        self.wait = False
        self.time=False
        self.test = True
        #set up move

    def load_images(self):
        for i in range(1,9):
            filename = 'plan{}.png'.format(i)
            img = pygame.image.load(filename)
            #img = pygame.transform.scale(img,(WIDTH,HEIGHT))
            self.water_list.append(img)
    def update(self):
        self.animate()
        if ship.boss_dead:
            self.rect.x -= self.speedx
            self.rect.y -= self.speedy
            if self.rect.centerx <= WIDTH//2 and self.time==False:
                self.speedx = 0
                self.moving=False
                self.time = True
                print("test")
            if self.time==True and self.test==True:
                self.last_delay=pygame.time.get_ticks()
                self.time=False
                print(self.last_delay)
                self.test = False

            if self.rect.centery<=HEIGHT//2:
                self.speedy = 0
            if self.moving == False:

                now = pygame.time.get_ticks()
                if now - self.last_delay > 2000:
                    self.last_update = now
                    self.wait=True
            # if self.wait == True:
                    expl = Expolosion(self.rect.center,'xl')
                    all_sprites.add(expl)
                    self.kill()

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update>500:
            self.last_update=now
            self.current_frame = (self.current_frame+1)%len(self.water_list)
            self.image = self.water_list[self.current_frame]
            #self.rect = self.image.get_rect()
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 50
        self.height = 38

        # shape
        #self.image = pygame.Surface((self.width, self.height))
        # self.image.fill(BLUE)
        self.image_orig = pygame.image.load("boss1.png")
        self.image = self.image_orig
        # self.image = pygame.transform.scale(self.image, (self.width,self.height))
        # rectangle
        self.rect = self.image.get_rect()
        # location on screen
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = -50
        # set up move
        self.speedx = 0
        self.speedy = 3
        self.shoot_delay = 500
        self.last_shot = pygame.time.get_ticks()
        self.health = 100
        self.move = True
        self.rot = 0
        self.rot_speed = 5
        self.rotation = pygame.time.get_ticks()
        self.angle=10
        self.orig_image = self.image
        self.movex = 0
        self.last_update = pygame.time.get_ticks()

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.y >= 50 and self.move==True:
            self.move = False
            self.speedy = 0
            self.speedx = 5
        if self.move == False:
            # self.rotate()

            if self.rect.right>WIDTH-20:
                self.speedx *=-1
            if self.rect.left<20:
                self.speedx *=-1
            self.shoot()
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
        # rotated_image = pygame.transform.rotate(self.orig_image, self.angle)
        # self.image = rotated_image
        # self.rect = rotated_image.get_rect(center=self.image.get_rect(center=(x, y)).center)
        # self.angle+=1
        # self.rect.centerx +=self.speedx

        # now = pygame.time.get_ticks()
        # if now - self.rotation > 50:
        #     self.rotation = now
        #     # self.rot = (self.rot+self.rot_speed)%360
        #     # self.image = pygame.transform.rotate(self.image,self.rot)
        #     self.rot = (self.rot + self.rot_speed) % 360
        #     new_image = pygame.transform.rotate(self.image, self.rot)
        #     old_center = self.rect.center
        #     self.image = new_image
        #     self.rect = self.image.get_rect()
        #     self.rect.center = old_center
    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.health>=70:
                b = Bullet2(self.rect.centerx, self.rect.bottom)
                all_sprites.add(b)
                bullets2.add(b)
            else:
                b1 = Bullet2(self.rect.left, self.rect.bottom)
                b2 = Bullet2(self.rect.right, self.rect.bottom)
                all_sprites.add(b1)
                bullets2.add(b1)
                all_sprites.add(b2)
                bullets2.add(b2)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #size
        self.width = 50
        self.height = 38
        self.create_mob = False
        #shape
        # self.image = pygame.Surface((self.width,self.height))
        # self.image.fill(BLUE)
        self.image = pygame.image.load("player_ship.png")
        self.image = pygame.transform.scale(self.image, (self.width,self.height))
        self.mini_img = pygame.transform.scale(self.image, (20, 20))
        #rectangle
        self.rect = self.image.get_rect()
        #location on screen
        self.rect.centerx = WIDTH//2
        self.rect.bottom = HEIGHT
        #set up move
        self.speedx =0
        self.speedy = 3
        self.shoot_delay = 500
        self.last_shot = pygame.time.get_ticks()
        self.score = 0
        self.lives = 3
        self.health = 100
        self.spawn = True
        self.mob_count=0
        self.power = 1
        self.power_time = pygame.time.get_ticks()
        self.boss_dead = False
    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power==1:
                b = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(b)
                bullets.add(b)
            if self.power>=2:
                b1 = Bullet(self.rect.left, self.rect.top)
                b2 = Bullet(self.rect.right, self.rect.top)
                all_sprites.add(b1)
                bullets.add(b1)
                all_sprites.add(b2)
                bullets.add(b2)

    def powerup(self):
        self.power+=1
        self.power_time=pygame.time.get_ticks()
    def update(self):
        if self.power>=2 and pygame.time.get_ticks()-self.power_time>5000:
            self.power -=1
            self.power_time=pygame.time.get_ticks()
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT]:
            self.speedx =10
        if keystate[pygame.K_LEFT]:
            self.speedx =-10
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0
        if keystate[pygame.K_SPACE]:
            self.shoot()

        self.rect.x += self.speedx

        #self.rect.y += self.speedy
def start_screen():
    screen.fill(BLUE)
    time = pygame.time.get_ticks()
    #draw_text(screen,'Demon Attack',64,WIDTH/2,HEIGHT/4,WHITE)
    draw_text(screen,'Arrow Keys to Move',22,WIDTH/2,HEIGHT/2,NEON_YELLOW)
    draw_text(screen,'Press A to Begin',18,WIDTH/2,HEIGHT *3/4,RED)
    for i in range(230):
        screen.fill(BLUE)
        # now = pygame.time.get_ticks()
        # if now - time >1000:
        #     time = now
        draw_text(screen, 'Demon ', 64, 0 + i, HEIGHT / 4, WHITE)
        draw_text(screen, 'Attack', 64, WIDTH - i, HEIGHT / 4, WHITE)
        pygame.display.flip()
    pygame.display.flip()
    waiting = True
    while waiting:


        color = random.choice([RED,WHITE])
        draw_text(screen, 'Press A to Begin', 18, WIDTH / 2, HEIGHT * 3 / 4, color)
        pygame.display.flip()
        clock.tick(FPS)
        for event in pygame.event.get():
            keystate =pygame.key.get_pressed()
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if keystate[pygame.K_a]:
                    waiting=False
def level_up(lev):
    screen.fill(BLUE)
    draw_text(screen, 'Level '+str(lev)+' Completed', 64, WIDTH / 2, HEIGHT / 4, WHITE)
    draw_text(screen, 'Arrow Keys to Move', 22, WIDTH / 2, HEIGHT / 2, NEON_YELLOW)
    draw_text(screen, 'Press A to Begin', 18, WIDTH / 2, HEIGHT * 3 / 4, RED)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            keystate = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if keystate[pygame.K_a]:
                    waiting = False

def lose_screen(score):
    screen.fill(BLUE)
    draw_text(screen, 'Sorry You Lost', 64, WIDTH / 2, HEIGHT / 4, WHITE)
    draw_text(screen, 'Arrow Keys to Move', 22, WIDTH / 2, HEIGHT / 2, NEON_YELLOW)
    draw_text(screen, 'Press A to Begin', 18, WIDTH / 2, HEIGHT * 3 / 4, RED)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            keystate = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if keystate[pygame.K_a]:
                    waiting = False


def win_screen(score):
    screen.fill(BLUE)
    draw_text(screen,'You Won',64,WIDTH/2,HEIGHT/4,WHITE)
    draw_text(screen,'Arrow Keys to Move',22,WIDTH/2,HEIGHT/2,NEON_YELLOW)
    draw_text(screen,'Press A to Begin',18,WIDTH/2,HEIGHT *3/4,RED)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            keystate =pygame.key.get_pressed()
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if keystate[pygame.K_a]:
                    waiting=False
# initialize pygame and create window
pygame.init()
pygame.mixer.init()
# mixer.music.load('Space Music.mp3')
# mixer.music.play()
# crash_sound = pygame.mixer.Sound("explosion_somewhere_far.mp3")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
bullets2 = pygame.sprite.Group()
bosss = pygame.sprite.Group()
powers = pygame.sprite.Group()
r="r"
l="l"
n ="n"


# for i in range(8):
#     newmob()
#newmob()


for i in range(200):
    star = Star()
    all_sprites.add(star)

water = Water()
all_sprites.add(water)

ship = Player()
all_sprites.add(ship)
# background_img = pygame.image.load("starfield.png")
# background_img = pygame.transform.scale(background_img,(WIDTH,HEIGHT))
# background_rect = background_img.get_rect()
boss = Boss()
# Game loop
new_game = True
running = True
win_game = False
boss_alive=False
last_move = pygame.time.get_ticks()
last_spawn = pygame.time.get_ticks()
delay = 2000
while running:
    if new_game:
        start_screen()
        new_game = False
        count = 0
        mob_count = 0
        level = 5
        lvl_comp=False
        boss_level = False
        game_reset=False
        game_done=False





    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    hit_mobs = pygame.sprite.groupcollide(mobs,bullets, True,True)
    if hit_mobs:
        for hit in hit_mobs:
            expl = Expolosion(hit.rect.center, 'lg')
            all_sprites.add(expl)
            if random.random()>.9:
                pow = Power(hit.rect.center)
                all_sprites.add(pow)
                powers.add(pow)
        #add score to player
        ship.score += 10
        ship.mob_count -= 1
        mob_count+=1
        # pygame.mixer.Sound.play(crash_sound)
        # newmob()
    hit_boss = pygame.sprite.spritecollide(boss, bullets, True)
    if hit_boss and boss_alive==True:
        boss.health -=10
        expl = Expolosion(boss.rect.midbottom, 'sm')
        all_sprites.add(expl)
        if boss.health <=0:
            expl = Expolosion(boss.rect.center,'xl')
            all_sprites.add(expl)

            boss.kill()
            ship.boss_dead=True
            last_move = pygame.time.get_ticks()
            game_done =True
    if ship.boss_dead == True:
        now = pygame.time.get_ticks()
        if now - last_move > 2000:
            last_move = now
            ship.boss_dead=False


            game_done = True
    if game_done:
        now = pygame.time.get_ticks()
        if now - last_move > 7000:
            last_move = now

            win_game=True
            game_done=False
    hit_power =pygame.sprite.spritecollide(ship,powers,True)
    for hit in hit_power:
        if hit.type=='health':
            ship.health += random.randrange(10,30)
            if ship.health >=100:
                ship.health = 100
        if hit.type=="gun":
            ship.powerup()
    hit_player = pygame.sprite.spritecollide(ship,mobs,True)
    if hit_player:
        #damage to player(ship)
        ship.health -= 25
        ship.mob_count-=1
        #newmob()
    if ship.health <= 0:
        ship.health = 100
        ship.lives -= 1
    if ship.lives <=0:
        running = False
    if mob_count == 5 and boss_alive==False:
        level_up(level)
        level+=1
        ship.spawn=False
        game_reset=True

        mob_count=0
        lvl_comp = True
    if game_reset:
        for h in mobs:
            h.kill()
        for b in bullets:
            b.kill()
        for b2 in bullets2:
            b2.kill()
        for pow in powers:
            pow.kill()
        game_reset=False
    if win_game:
        win_screen(ship.score)
    if lvl_comp:
        lvl_comp = False
        if level<6:
            ship.create_mob = True
    # now = pygame.time.get_ticks()
    # if now - last_spawn < delay:
    #     print("Check")
    #     for i in range(3):
    #         last_spawn = now
    if ship.spawn == True:
            x = random.randrange(100,WIDTH-ship.width-40)
            y = random.randrange(100,300)
            m = Mob(r,x,y)
            all_sprites.add(m)
            mobs.add(m)
            m1 = Mob(l,x,y)
            all_sprites.add(m1)
            mobs.add(m1)
            ship.spawn = False
    # if ship.spawn:
    if ship.create_mob == True:
        m2 = Mob(n,x,y)
        all_sprites.add(m2)
        mobs.add(m2)
        ship.create_mob = False

        ship.mob_count +=1
    if level<6:
        if ship.mob_count <3:
            now = pygame.time.get_ticks()
            if now - last_spawn > delay:
                ship.spawn = True
                last_spawn = now
    if level==5:
        level +=1
        boss_level = True
        ship.boss_dead == True
    if boss_level:
        game_reset=True
        ship.create_mob = False
        boss_alive = True
        all_sprites.add(boss)
        bosss.add(boss)
        boss_level=False

    # Update
    all_sprites.update()
    # Draw / render
    screen.fill(BLACK)

    #screen.blit(background_img,background_rect)
    all_sprites.draw(screen)
    draw_text(screen,str(ship.score),32,WIDTH//2,10,WHITE)
    #draw_text(screen, str(ship.lives), 32, 3*WIDTH // 4, 10, WHITE)
    #draw_text(screen, str(ship.health), 32, WIDTH // 4, 10, WHITE)
    draw_shield_bar(screen, 5, 5, ship.health, GREEN)
    draw_lives(screen, WIDTH - 100, 5, ship.lives, ship.mini_img)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()