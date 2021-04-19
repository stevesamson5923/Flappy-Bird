import pygame
import random
pygame.init()

WIDTH = 500
HEIGHT = 600

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('FALPPY BIRD')
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS',30)

WIDTH_BIRD = 50
HEIGHT_BIRD = 50

bird = [pygame.image.load('fly1.png'),pygame.image.load('fly2.png'),pygame.image.load('fly3.png'),pygame.image.load('fly4.png'),
pygame.image.load('fly5.png'),pygame.image.load('fly6.png'),pygame.image.load('fly7.png'),pygame.image.load('fly8.png')]

bird_fly = [pygame.transform.scale(bird[0],(WIDTH_BIRD,HEIGHT_BIRD)),pygame.transform.scale(bird[1],(WIDTH_BIRD,HEIGHT_BIRD)),pygame.transform.scale(bird[2],(WIDTH_BIRD,HEIGHT_BIRD)),pygame.transform.scale(bird[3],(WIDTH_BIRD,HEIGHT_BIRD)),
pygame.transform.scale(bird[4],(WIDTH_BIRD,HEIGHT_BIRD)),pygame.transform.scale(bird[5],(WIDTH_BIRD,HEIGHT_BIRD)),pygame.transform.scale(bird[6],(WIDTH_BIRD,HEIGHT_BIRD)),
pygame.transform.scale(bird[7],(WIDTH_BIRD,HEIGHT_BIRD))]

pipes = [pygame.image.load('images/bottom pipe.png'),pygame.image.load('images/top pipe.png')]

class Bird:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.count = 0 
        self.hit = False
        self.score = 0
    def draw(self,win):
        win.blit(bird_fly[self.count],(self.x,self.y))
    def update(self,win): 
        self.count = self.count + 1
        if self.count == 8:
            self.count = 0
        self.draw(win)

class BG:
    def __init__(self,x,y,width,height):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.bg = pygame.transform.scale(pygame.image.load('bg.jpg'),(self.width,self.height))
        self.velx = 4
    def draw(self,win):
        win.blit(self.bg,(self.x,self.y))
    def update(self,win):
        self.x = self.x - self.velx
        self.draw(win)

class Pipes:
    def __init__(self,x,y,width,height,velx,vely,pos):
        self.x = x
        self.y = y
        self.width = width
        self.height =height
        self.pos = pos # 1 for top and 0 for bottom
        self.pipe = pipes[self.pos]
        self.velx = velx
        self.vely = vely
    def draw(self,win):
        win.blit(self.pipe,(self.x,self.y))
    def update(self,win):
        self.x = self.x - self.velx
        self.draw(win)

bird = Bird(int(WIDTH*0.2),int(HEIGHT*0.2),WIDTH_BIRD,HEIGHT_BIRD)

bg1 = BG(0,0,WIDTH,HEIGHT)
bg2 = BG(bg1.x+WIDTH+1,0,WIDTH,HEIGHT)

run = True

top_list=[]
bot_list=[]

dy = random.randint(-40,180)
toppipe = Pipes(300,-40-dy,pipes[1].get_width(),pipes[1].get_height(),2,0,1)
botpipe = Pipes(300,-350-dy,pipes[1].get_width(),pipes[1].get_height(),2,0,0)

top_list.insert(0,toppipe)
bot_list.insert(0,botpipe)

while run:
    bg1.update(win)
    bg2.update(win)
    bird.update(win)
    if bg1.x <= -WIDTH:
        bg1.x = bg2.x + 500
    if bg2.x <= -WIDTH:
        bg2.x = bg1.x + WIDTH
    
    dy = random.randint(-40,180)

    #create new pipes
    if len(top_list) < 3:
        toppipe = Pipes(top_list[len(top_list)-1].x+200,-40-dy,pipes[1].get_width(),pipes[1].get_height(),2,0,1)
        botpipe = Pipes(bot_list[len(bot_list)-1].x+200,-350-dy,pipes[0].get_width(),pipes[0].get_height(),2,0,0)
        top_list.append(toppipe)
        bot_list.append(botpipe)

    for index,pipe in enumerate(top_list):
        top_list[index].update(win)
        bot_list[index].update(win)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False        
    pygame.display.update()
pygame.quit()
