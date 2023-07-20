import pygame
from sys import exit

def display_time():
    current_time = pygame.time.get_ticks()
    time_surf = font2.render(f'{current_time}',False,'White')
    time_rect = time_surf.get_rect(center = (550,25))
    screen.blit(time_surf,time_rect)

width = 600
height = 400
fps = 60

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Game Name Here')    # Window Name here
clock = pygame.time.Clock()
font1 = pygame.font.Font('font/pandabakery.ttf', 50)
font2 = pygame.font.Font('font/pandabakery.ttf', 20)

game_active = False

background_surf = pygame.image.load('image/background1.jpg').convert()

gameTitle_surf = font1.render('Agent J', True, 'White')
gameTitle_rect = gameTitle_surf.get_rect(midtop=(width/2,30))

player_surf = pygame.image.load('image/player.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom= (width/2,350))
player_gravity = 0
player_direction = 0

#pygame.transform.flip(surface_background, True, False)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            # click to get the Cord of the Cursor
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if player_rect.collidepoint(event.pos):
                    player_gravity = -15
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 350:
                    player_gravity = -15
                if event.key == pygame.K_a:
                    player_direction = -1
                if event.key == pygame.K_d:
                    player_direction = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player_direction == -1:
                    player_direction = 0
                if event.key == pygame.K_d and player_direction == 1:
                    player_direction = 0

        else:
            if event.type == pygame.KEYDOWN:
                player_rect.bottom = 350
                game_active = True


    if game_active:
        # Title and Background
        screen.blit(background_surf,(0,0))
        screen.blit(gameTitle_surf,gameTitle_rect)
        display_time()

        # Player
        player_gravity += 0.5
        player_rect.y += player_gravity
        player_rect.x += player_direction*2
        if player_rect.bottom >= 350:
            player_rect.bottom = 350
        screen.blit(player_surf,player_rect)

        if player_rect.top <= 0:
            game_active = False
        
    else:
        screen.fill('Pink')


    pygame.display.update()
    clock.tick(fps)