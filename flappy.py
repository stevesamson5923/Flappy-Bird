import pygame
import random
pygame.init()

WIDTH = 500
HEIGHT = 600

win = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('FLAPPY BIRD' )
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
myfont2 = pygame.font.SysFont('Comic Sans MS', 48)

clock = pygame.time.Clock()

WIDTH_BIRD = 50
HEIGHT_BIRD = 50


bird = [pygame.image.load('fly1.png'), pygame.image.load('fly2.png'), pygame.image.load('fly3.png'),
              pygame.image.load('fly4.png'),pygame.image.load('fly5.png'), pygame.image.load('fly6.png'), 
             pygame.image.load('fly7.png'),pygame.image.load('fly8.png')]

bird_fly = [pygame.transform.scale(bird[0], (WIDTH_BIRD, HEIGHT_BIRD)),pygame.transform.scale(bird[1], (WIDTH_BIRD, HEIGHT_BIRD)),pygame.transform.scale(bird[2], (WIDTH_BIRD, HEIGHT_BIRD)),
            pygame.transform.scale(bird[3], (WIDTH_BIRD, HEIGHT_BIRD)),pygame.transform.scale(bird[4], (WIDTH_BIRD, HEIGHT_BIRD)),pygame.transform.scale(bird[5], (WIDTH_BIRD, HEIGHT_BIRD)),
            pygame.transform.scale(bird[6], (WIDTH_BIRD, HEIGHT_BIRD)),pygame.transform.scale(bird[7], (WIDTH_BIRD, HEIGHT_BIRD))]

pipes = [pygame.image.load('images/bottom pipe.png'),pygame.image.load('images/top pipe.png')]

class Bird:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.count = -1
        self.hit = False
        self.score = 0
    def update(self,win,space):        
        self.count = self.count + 1
        self.y = self.y + 4
        if space:
            self.y = self.y - 20
        if self.count == 8:
            self.count = 0
        self.draw(win)
    def draw(self,win):
        #pygame.draw.rect(win, (0, 0, 255), pygame.Rect(self.x, self.y, self.width, self.height),3)
        win.blit(bird_fly[self.count],(self.x,self.y))
    
class BG:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y        
        self.width = width
        self.height = height
        self.bg = pygame.transform.scale(pygame.image.load('bg.jpg'), (self.width, self.height))
        self.velx = 4
    def draw(self,win):
        win.blit(self.bg, (self.x,self.y))
    def update(self,win):
        self.x = self.x - self.velx
        self.draw(win)

class Pipes:
    def __init__(self,x,y,width,height,velx,vely,pos):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = pos #1 for top and 0 for bottom
        self.pipe = pipes[self.pos]
        self.velx = velx
        self.vely = vely
    def draw(self,win):
        win.blit(self.pipe,(self.x,self.y)) 
    def update(self,win,prevpipe,dx,bird):
        
        if bird.x + bird.width>=self.x+5 and bird.x + bird.width<=self.x+self.width and \
        ((bird.y>=self.y and bird.y <= self.y+self.height-5) or \
         (bird.y+bird.height>=self.y+5 and bird.y+bird.height<=self.y+self.height)):
            bird.hit = True
        elif bird.y > self.y+self.height and bird.y+bird.height < self.y+self.height+154 and\
            bird.x > self.x+self.width and bird.x < self.x+self.width + 3: #154 is distance between pipes
            bird.score = bird.score + 1
        if self.x < 0:
            self.x = prevpipe.x + 200
            if self.pos == 0:
                self.y = 350 - dx
            else:
                self.y = -40 - dx
        self.x = self.x - self.velx
        self.draw(win)        

bird = Bird(int(WIDTH*0.2),int(HEIGHT*0.4),WIDTH_BIRD,HEIGHT_BIRD)

bg_x=0
bg_y=0
bg2_x = WIDTH+1
bg2_y = 0

bg1 = BG(bg_x,bg_y,WIDTH,HEIGHT)
bg2 = BG(bg2_x,bg2_y,WIDTH,HEIGHT)

top_list =[]
bot_list =[]

dx = random.randint(-40,180)    
toppipe = Pipes(300,-40-dx,pipes[1].get_width(),pipes[1].get_height(),2,0,1)
botpipe = Pipes(300,350-dx,pipes[0].get_width(),pipes[0].get_height(),2,0,0)
#print(dx)

top_list.insert(0,toppipe)
bot_list.insert(0,botpipe)
run=True
space = False
textsurface2 =None
def redrawWindow():
    global space
    #print(space)
   
    if not bird.hit:
        textsurface2 = myfont2.render("", False, (11,77,112))
        win.blit(textsurface2,(WIDTH/2-130,HEIGHT/2-50))
        
        if bg1.x <= -WIDTH:
            bg1.x = bg2.x + WIDTH
        if bg2.x <= -WIDTH:
            bg2.x = bg1.x + WIDTH
        
        bg1.update(win)
        bg2.update(win)
        bird.update(win,space)  
    
        dx = random.randint(-40,180)   
        
        if len(top_list) < 3:
            toppipe = Pipes(top_list[len(top_list)-1].x+200,-40-dx,pipes[1].get_width(),pipes[1].get_height(),2,0,1)
            botpipe = Pipes(bot_list[len(bot_list)-1].x+200,350-dx,pipes[0].get_width(),pipes[0].get_height(),2,0,0)
            top_list.insert(len(top_list),toppipe)
            bot_list.insert(len(bot_list),botpipe)
    
        for index,pipe in enumerate(top_list):
            dx1 = random.randint(-40,180)  
            if index == 0:
                top_list[index].update(win,top_list[len(top_list)-1],dx1,bird)
                bot_list[index].update(win,bot_list[len(top_list)-1],dx1,bird)
            else:
                top_list[index].update(win,top_list[index-1],dx1,bird)
                bot_list[index].update(win,bot_list[index-1],dx1,bird)
            #toppipe.update(win)
            #botpipe.update(win)
        count = 'Score: ' + str(bird.score)
        textsurface1 = myfont.render(count, False, (219, 214, 213))
        win.blit(textsurface1,(30,HEIGHT-50))
        pygame.display.update()
    else:
        textsurface2 = myfont2.render("GAME OVER", False, (11,77,112))
        win.blit(textsurface2,(WIDTH/2-130,HEIGHT/2-50))
        pygame.display.update()
        #print(bird.score)
        #print(bird_fly[0].get_width())
        #screen.fill((255, 255, 255))
        #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        #pygame.display.flip()


while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #elif event.type == pygame.MOUSEMOTION:
            #x,y  = pygame.mouse.get_pos()            
        #    rel_x,rel_y = pygame.mouse.get_rel()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        pass
    if keys[pygame.K_SPACE]:        
        space = True
    if keys[pygame.K_r]:        
        top_list.clear()
        bot_list.clear()
        
        dx = random.randint(-40,180)    
        toppipe = Pipes(300,-40-dx,pipes[1].get_width(),pipes[1].get_height(),2,0,1)
        botpipe = Pipes(300,350-dx,pipes[0].get_width(),pipes[0].get_height(),2,0,0)
        #print(dx)
        top_list.insert(0,toppipe)
        bot_list.insert(0,botpipe)
        
        bird = Bird(int(WIDTH*0.2),int(HEIGHT*0.4),WIDTH_BIRD,HEIGHT_BIRD)
        bird.count = -1
        bird.hit = False
        bird.score = 0
        
    redrawWindow()
    space = False
pygame.quit()
