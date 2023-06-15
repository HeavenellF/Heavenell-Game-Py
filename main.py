import pygame
from sys import exit

width = 800
height = 400
fps = 60

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Game Name Here')    # Window Name here
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

surface_background = pygame.image.load('image/background1.jpg')
surface_gameTitle = test_font.render('Robot Assistant', True, 'White')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(surface_background,(100,0))
    screen.blit(surface_gameTitle,(275, 30))

    pygame.display.update()
    clock.tick(fps)