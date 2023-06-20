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

background_surf = pygame.image.load('image/background1.jpg').convert()
gameTitle_surf = test_font.render('Robot Assistant', True, 'White')

player_surf = pygame.image.load('image/player.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom= (400,350))
#pygame.transform.flip(surface_background, True, False)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(background_surf,(100,0))
    screen.blit(gameTitle_surf,(275, 30))

    screen.blit(player_surf,player_rect)

    pygame.display.update()
    clock.tick(fps)