import pygame
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

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False        

pygame.quit()
