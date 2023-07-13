import pygame
from sys import exit

width = 600
height = 400
fps = 60

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Game Name Here')    # Window Name here
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

background_surf = pygame.image.load('image/background1.jpg').convert()

gameTitle_surf = test_font.render('Robot Assistant', True, 'White')
gameTitle_rect = gameTitle_surf.get_rect(midtop=(width/2,30))

player_surf = pygame.image.load('image/player.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom= (width/2,350))

#pygame.transform.flip(surface_background, True, False)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # click to get the Cord of the Cursor
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('Jump')
    
    screen.blit(background_surf,(0,0))
    screen.blit(gameTitle_surf,gameTitle_rect)

    screen.blit(player_surf,player_rect)


    pygame.display.update()
    clock.tick(fps)