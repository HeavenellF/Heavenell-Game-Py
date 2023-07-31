import pygame
from sys import exit

from Button import mainMenu_elements, gameOver_elements

def display_time(finish):
    current_time = pygame.time.get_ticks() - start_time - pause_duration
    minutes = current_time // 60000
    seconds = (current_time % 60000) // 1000
    # Convert to strings and add leading zeros if necessary
    minutes_str = str(minutes).zfill(2)
    seconds_str = str(seconds).zfill(2)
    # Create the time string in mm:ss format
    time_str = f'{minutes_str}:{seconds_str}'

    time_surf = font2.render(f'{time_str}',False,'Black')
    time_rect = time_surf.get_rect(center = (width - 700,25))
    screen.blit(time_surf,time_rect)

    if finish:
        # Create the time finish string
        timefinish_str = f'Your Time: {minutes_str}:{seconds_str}'
        timefinish_surf = font3.render(timefinish_str, True, 'Black')
        timefinish_rect = timefinish_surf.get_rect(center=(width / 2, 150))

        return timefinish_surf, timefinish_rect

width = 800
height = 600
fps = 60

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Agent J')    # Window Name here
clock = pygame.time.Clock()
font1 = pygame.font.Font('font/pandabakery.ttf', 65)
font2 = pygame.font.Font('font/pandabakery.ttf', 20)
font3 = pygame.font.Font('font/pandabakery.ttf', 40)

start_time = 0
pause_duration = 0
pause_start = 0
pause_end = 0
game_state = 0
glint_button = None
finish = False
charging = False
jumpCharge = 0

background_surf = pygame.image.load('image/background1.jpg').convert()

button_surf1 = pygame.image.load('image/misc/ButtonMain.png').convert()



player_surf = pygame.image.load('image/player.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom= (width/2,350))
player_gravity = 0
player_direction = 0

mainMenu_elements = mainMenu_elements(width, height, font1, font3, button_surf1)
gameOver_elements = gameOver_elements(width, height, font1, font3, button_surf1)

#pygame.transform.flip(surface_background, True, False)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # click to get the Cord of the Cursor
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if player_rect.collidepoint(event.pos):
                player_gravity = -15
        
        if game_state == 1:
            # Keyboard press down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jumpCharge += 0.2
                    #player_gravity = -15
                if event.key == pygame.K_a:
                    player_direction = -1
                if event.key == pygame.K_d:
                    player_direction = 1

                # Pause in-game
                if event.key == pygame.K_ESCAPE:
                    game_state = 2
                    pause_start = pygame.time.get_ticks()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player_direction == -1:
                    player_direction = 0
                if event.key == pygame.K_d and player_direction == 1:
                    player_direction = 0
                if event.key == pygame.K_SPACE:
                    player_gravity = -1.7 * jumpCharge
                    # print(jumpCharge)
                    # print(player_gravity)
                    jumpCharge = 0
        # pause
        elif game_state == 2:
            if event.type == pygame.KEYDOWN:
                player_rect.bottom = 350
                game_state = 1
                pause_end = pygame.time.get_ticks()
                pause_duration += pause_end - pause_start
        
        # gameover
        elif game_state == 3:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Play Again
                if gameOver_elements['button_rectPlayAgain'].collidepoint(event.pos):
                    game_state = 1
                    start_time = pygame.time.get_ticks()
                # Main Menu
                if gameOver_elements['button_rectMainMenu'].collidepoint(event.pos):
                    game_state = 0
                # Exit
                if gameOver_elements['button_rectExit'].collidepoint(event.pos):
                    pygame.quit()
                    exit()
            # Glinting Effect
            if event.type == pygame.MOUSEMOTION:
                if gameOver_elements['button_rectPlayAgain'].collidepoint(event.pos):
                    glint_button = 'play again'
                elif gameOver_elements['button_rectMainMenu'].collidepoint(event.pos):
                    glint_button = 'main menu'
                elif gameOver_elements['button_rectExit'].collidepoint(event.pos):
                    glint_button = 'exit'
                else:
                    glint_button = None
        
        # Main Menu
        elif game_state == 0:         
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Play
                if mainMenu_elements['button_rectPlay'].collidepoint(event.pos):
                    game_state = 1
                    start_time = pygame.time.get_ticks()
                # Exit
                if mainMenu_elements['button_rectExit'].collidepoint(event.pos):
                    pygame.quit()
                    exit()
            # Glinting Effect
            if event.type == pygame.MOUSEMOTION:
                if mainMenu_elements['button_rectPlay'].collidepoint(event.pos):
                    glint_button = 'play'
                elif mainMenu_elements['button_rectSetting'].collidepoint(event.pos):
                    glint_button = 'setting'
                elif mainMenu_elements['button_rectExit'].collidepoint(event.pos):
                    glint_button = 'exit'
                else:
                    glint_button = None

                    

    # Gameplay
    if game_state == 1:
        # Title and Background
        screen.fill('white')
        display_time(finish)

        # Player
        if jumpCharge !=0 and jumpCharge <= 10:
            jumpCharge += 0.2
        player_gravity += 0.5
        player_rect.y += player_gravity
        player_rect.x += player_direction*3
        if player_rect.bottom >= 350:
            player_rect.bottom = 350
        screen.blit(player_surf,player_rect)

        if player_rect.top <= 0:
            player_rect.bottom = 350
            timefinish_surf,timefinish_rect = display_time(finish=True)
            game_state = 3
    
    # Pause
    elif game_state == 2:
        semitransparent_surf = pygame.Surface((width, height))
        semitransparent_surf.fill((0, 0, 0))
        semitransparent_surf.set_alpha(128)

        screen.blit(background_surf, (0, 0))
        screen.blit(semitransparent_surf, (0, 0))
    
    # Gameover
    elif game_state == 3:
        screen.fill('white')
        screen.blit(gameOver_elements['gameOver_surf'], gameOver_elements['gameOver_rect'])
        screen.blit(timefinish_surf, timefinish_rect)

        screen.blit(button_surf1, gameOver_elements['button_rectPlayAgain'])
        screen.blit(gameOver_elements['buttonPlayAgain_surf'], gameOver_elements['buttonPlayAgain_rect'])
        screen.blit(button_surf1, gameOver_elements['button_rectMainMenu'])
        screen.blit(gameOver_elements['buttonMainMenu_surf'], gameOver_elements['buttonMainMenu_rect'])
        screen.blit(button_surf1, gameOver_elements['button_rectExit'])
        screen.blit(gameOver_elements['buttonExit_surf'], gameOver_elements['buttonExit_rect'])
        if glint_button == 'play again': pygame.draw.rect(screen, 'Black', gameOver_elements['button_rectPlayAgain'], 4)
        elif glint_button == 'main menu': pygame.draw.rect(screen, 'Black', gameOver_elements['button_rectMainMenu'], 4)
        elif glint_button == 'exit': pygame.draw.rect(screen, 'Black', gameOver_elements['button_rectExit'], 4)

    # Main Menu
    elif game_state == 0:
        screen.fill('white')
        screen.blit(mainMenu_elements['gameTitle_surf'], mainMenu_elements['gameTitle_rect'])

        screen.blit(button_surf1, mainMenu_elements['button_rectPlay'])
        screen.blit(mainMenu_elements['buttonPlay_surf'], mainMenu_elements['buttonPlay_rect'])
        screen.blit(button_surf1, mainMenu_elements['button_rectSetting'])
        screen.blit(mainMenu_elements['buttonSetting_surf'], mainMenu_elements['buttonSetting_rect'])
        screen.blit(button_surf1, mainMenu_elements['button_rectExit'])
        screen.blit(mainMenu_elements['buttonExit_surf'], mainMenu_elements['buttonExit_rect'])
        if glint_button == 'play': pygame.draw.rect(screen, 'Black', mainMenu_elements['button_rectPlay'], 4)
        elif glint_button == 'setting': pygame.draw.rect(screen, 'Black', mainMenu_elements['button_rectSetting'], 4)
        elif glint_button == 'exit': pygame.draw.rect(screen, 'Black', mainMenu_elements['button_rectExit'], 4)


    pygame.display.update()
    clock.tick(fps)