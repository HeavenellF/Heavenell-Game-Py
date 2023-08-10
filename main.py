#!/usr/bin/env python
import pygame
import random
from sys import exit

from Button import mainMenu_elements, gameOver_elements
from collision import get_collision_side
import levelsobject

class Testtube(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('image/misc/testtube.png').convert_alpha()
        self.rect = self.image.get_rect(center = (600, 250))
        self.direction = 1
        self.i = 0
    
    def move_animation(self):
        if game_state == 1:
            if self.rect.y >= 220:
                self.direction *= -1
            elif self.rect.y <= 180:
                self.direction *= -1
            self.i += 0.2
            if self.i >= 1:
                self.rect.y += self.direction
                self.i = 0
        elif game_state == 4 and endingDuration == 0:
            self.rect.y += 1

    def update(self):
        self.move_animation()

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
    time_rect = time_surf.get_rect(center = (100,25))
    screen.blit(time_surf,time_rect)

    if finish:
        # Create the time finish string
        timefinish_str = f'Your Time: {minutes_str}:{seconds_str}'
        timefinish_surf = font3.render(timefinish_str, True, 'Black')
        timefinish_rect = timefinish_surf.get_rect(center=(width / 2, 225))

        return timefinish_surf, timefinish_rect

def start_game():
    global game_state, level, start_time, pause_duration, midAir, midStrafe, player_rect
    bgm_sound.play(-1)
    game_state = 1
    level = 1
    start_time = pygame.time.get_ticks()
    pause_duration = 0
    midAir = False
    midStrafe = False
    player_rect = player_surf.get_rect(midbottom= (width/2,700))
    testtube.sprite.rect.center = (600,250)

def player_animation():
    global player_surf, player_index
    # walking animation
    if midStrafe:
        player_index = 1
        player_surf = player_state[player_index]
    elif jumpCharge != 0:
        player_index = 2
        player_surf = player_state[player_index]
    elif player_gravity < 0 or (player_rect.colliderect(testtube.sprite.rect) and game_state == 4):
        player_index = 3
        player_surf = player_state[player_index]
    elif tired:
        player_index = 4
        player_surf = player_state[player_index]
    else:
        player_index = 0
        player_surf = player_state[player_index]

    
    if player_direction == 1:
        player_surf = pygame.transform.flip(player_surf, True, False)

def play_sound(type):
    if type == 'wall':
        random_number = random.randint(1, 3)
        if random_number == 1 : wallbounce1_sound.play()
        elif random_number == 2 : wallbounce2_sound.play()
        elif random_number == 3 : wallbounce3_sound.play()
    elif type == 'jump':
        jump_sound.play()
    elif type == 'fell':
        fell_sound.play()

width = 1200
height = 900
fps = 60

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Agent J')    # Window Name here
clock = pygame.time.Clock()
font1 = pygame.font.Font('font/pandabakery.ttf', 97)
font2 = pygame.font.Font('font/pandabakery.ttf', 30)
font3 = pygame.font.Font('font/pandabakery.ttf', 60)

start_time = 0
pause_duration = 0
pause_start = 0
pause_end = 0
game_state = 0
glint_button = None
finish = False
endingDuration = 0


background_mainmenu_surf = pygame.image.load('image/mainmenuBackground.png').convert()
background_gameover_surf = pygame.image.load('image/gameoverBackground.png').convert()

#====================================== mp3 ==============================#
bgm_sound = pygame.mixer.Sound('sound/bgm.mp3')
bgm_sound.set_volume(0.5)
finish_sound = pygame.mixer.Sound('sound/finish.mp3')
finish_sound.set_volume(0.5)
wallbounce1_sound = pygame.mixer.Sound('sound/wallhit1.mp3')
wallbounce1_sound.set_volume(0.8)
wallbounce2_sound = pygame.mixer.Sound('sound/wallhit2.mp3')
wallbounce2_sound.set_volume(0.8)
wallbounce3_sound = pygame.mixer.Sound('sound/wallhit3.mp3')
wallbounce3_sound.set_volume(0.8)
jump_sound = pygame.mixer.Sound('sound/jump.mp3')
jump_sound.set_volume(0.9)
fell_sound = pygame.mixer.Sound('sound/fell.mp3')
fell_sound.set_volume(1)
#====================================== mp3 ==============================#

pause_surf = font3.render('Pause', True, 'Black')
pause_rect = pause_surf.get_rect(midbottom=(width / 2, height / 2))

button_surf1 = pygame.image.load('image/misc/ButtonMain.png').convert()

player_stand = pygame.image.load('image/player/playerstand.png').convert_alpha()
player_walk_1 = pygame.image.load('image/player/playerwalk1.png').convert_alpha()
player_charge = pygame.image.load('image/player/playercharge.png').convert_alpha()
player_jump = pygame.image.load('image/player/playerjump.png').convert_alpha()
player_fell = pygame.image.load('image/player/playerfell.png').convert_alpha()
player_state = [player_stand, player_walk_1, player_charge, player_jump, player_fell]
player_index = 0

player_surf = player_state[player_index]
player_rect = player_surf.get_rect()
player_gravity = 0
player_direction = 1
jumpCharge = 0
midAir = False
midStrafe = False
onAir = 0
tired = False
rest = 0

testtube = pygame.sprite.GroupSingle()
testtube.add(Testtube())

mainMenu_elements = mainMenu_elements(width, height, font1, font3, button_surf1)
gameOver_elements = gameOver_elements(width, height, font1, font3, button_surf1)

levels_object = [levelsobject.level1_object(width,height), 
                 levelsobject.level2_object(width,height), 
                 levelsobject.level3_object(width,height),
                 levelsobject.level4_object(width,height),
                 levelsobject.level5_object(width,height),
                 levelsobject.level6_object(width,height),
                 levelsobject.level7_object(width,height),
                 levelsobject.level8_object(width,height),
                 levelsobject.levelend1_object(width,height),
                 levelsobject.levelend2_object(width,height),
                 levelsobject.levelend3_object(width,height)]
level = 0

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
                if event.key == pygame.K_SPACE and not midAir and not tired:
                    jumpCharge += 0.3
                    midStrafe = False
                if event.key == pygame.K_a and not midAir and not tired:
                    player_direction = -1
                    if jumpCharge == 0:
                        midStrafe = True
                if event.key == pygame.K_d and not midAir and not tired:
                    player_direction = 1
                    if jumpCharge == 0:
                        midStrafe = True

                # Pause in-game
                if event.key == pygame.K_ESCAPE:
                    game_state = 2
                    pause_start = pygame.time.get_ticks()
                if event.key == pygame.K_n:
                    level += 1
                    player_rect.y = 800
                if event.key == pygame.K_m:
                    level -= 1
                    player_rect.y = 800

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and midStrafe:
                    midStrafe = False
                if event.key == pygame.K_d and midStrafe:
                    midStrafe = False
                if event.key == pygame.K_SPACE and not midAir and jumpCharge != 0:
                    player_gravity = -1.3 * jumpCharge
                    jumpCharge = 0
                    midAir = True
                    play_sound('jump')
        # pause
        elif game_state == 2:
            if event.type == pygame.KEYDOWN:
                game_state = 1
                pause_end = pygame.time.get_ticks()
                pause_duration += pause_end - pause_start
        
        # gameover
        elif game_state == 3:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Play Again
                if gameOver_elements['button_rectPlayAgain'].collidepoint(event.pos):
                    start_game()
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
                    start_game()
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
        # Blit
        for surf, rect, _ in levels_object[level-1]:
            screen.blit(surf, rect)

        # Jumping 
        if jumpCharge !=0 and jumpCharge <= 15:
            jumpCharge += 0.3
        player_gravity += 0.6
        player_rect.y += player_gravity
        if midAir:
            player_rect.x += player_direction*10
        # Move the Character
        if midStrafe:
            player_rect.x += player_direction*5
        # Stop when touching a Border
        if player_rect.right >= width:
            midStrafe = False
            player_rect.right = width
            if midAir: 
                player_direction *= -1
                play_sound('wall')
        if player_rect.left <= 0:
            player_rect.left = 0
            midStrafe = False
            if midAir: 
                player_direction *= -1
                play_sound('wall')

        onAir += 1
        for platform_surf, platform_rect, platform in levels_object[level-1]:
            if platform:
                if player_rect.colliderect(platform_rect):
                    side = get_collision_side(player_rect, platform_rect)
                    if side == 'top':
                        print('top')
                        player_rect.top = platform_rect.bottom
                        if midAir: 
                            player_gravity = 0
                            play_sound('wall')
                    elif side == 'bottom':
                        if player_gravity >= 30:
                            tired = True
                            midStrafe = False
                            play_sound('fell')
                        if tired:
                            rest += 1
                            if rest >= 90:
                                tired = False
                                rest = 0
                        player_gravity = 0
                        player_rect.bottom = platform_rect.top + 2
                        midAir = False
                    elif side == 'right':
                        if not midStrafe: 
                            player_direction *= -1
                            play_sound('wall')
                        player_rect.right = platform_rect.left
                    elif side == 'left':
                        if not midStrafe: 
                            player_direction *= -1
                            play_sound('wall')
                        player_rect.left = platform_rect.right

        # check if the Player reach top or bottom
        if player_rect.top <= 0:
            player_rect.top += height
            level += 1
        elif player_rect.top >= height:
            player_rect.top -= height
            level -= 1
        
        # showing Testtube
        if level == len(levels_object):
            testtube.draw(screen)
            testtube.update()
            # Game Ending
            if (player_rect.right >= 460 and player_rect.right <= 740) or (player_rect.left >= 460 and player_rect.left <= 740):
                if player_rect.centery <= 630:
                    timefinish_surf,timefinish_rect = display_time(finish=True)
                    bgm_sound.stop()
                    game_state = 4
        player_animation()
        screen.blit(player_surf,player_rect)
        display_time(finish)
    
    # Pause
    elif game_state == 2:
        for surf, rect, _ in levels_object[level-1]:
            screen.blit(surf, rect)
        screen.blit(player_surf,player_rect)
        screen.blit(pause_surf,pause_rect)
    
    # Gameover
    elif game_state == 3:
        screen.blit(background_gameover_surf,(0,0))
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
        screen.blit(background_mainmenu_surf,(0,0))
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

    # Game Ending
    elif game_state == 4:
        # Blit
        for surf, rect, _ in levels_object[level-1]:
            screen.blit(surf, rect)
        player_gravity += 0.6
        player_rect.y += player_gravity
        if midAir:
            player_rect.x += player_direction*10
        if not midAir and player_rect.right != 600 and player_rect.left != 600:
            if player_rect.centerx <= 600:
                player_rect.x += player_direction
            else:
                player_rect.x += player_direction

        onAir += 1
        for platform_surf, platform_rect, platform in levels_object[level-1]:
            if platform:
                if player_rect.colliderect(platform_rect):
                    side = get_collision_side(player_rect, platform_rect)
                    if side == 'top':
                        print('top')
                        player_rect.top = platform_rect.bottom
                        if midAir: 
                            player_gravity = 0
                            play_sound('wall')
                    elif side == 'bottom':
                        if player_gravity >= 30:
                            tired = True
                            midStrafe = False
                            play_sound('fell')
                        if tired:
                            rest += 1
                            if rest >= 90:
                                tired = False
                                rest = 0
                        player_gravity = 0
                        player_rect.bottom = platform_rect.top + 2
                        midAir = False
                    elif side == 'right':
                        if not midStrafe: 
                            player_direction *= -1
                            play_sound('wall')
                        player_rect.right = platform_rect.left
                    elif side == 'left':
                        if not midStrafe: 
                            player_direction *= -1
                            play_sound('wall')
                        player_rect.left = platform_rect.right

        # check if the Player reach top or bottom
        if player_rect.top <= 0:
            player_rect.top += height
            level += 1
        elif player_rect.top >= height:
            player_rect.top -= height
            level -= 1
        
        testtube.draw(screen)
        testtube.update()
        if player_rect.colliderect(testtube.sprite.rect):
            if endingDuration == 0:
                finish_sound.play()
                endingDuration = 1
            elif endingDuration >= 250:
                timefinish_surf,timefinish_rect = display_time(finish=True)
                endingDuration = 0
                game_state = 3
            else:
                endingDuration += 1
                
        player_animation()
        screen.blit(player_surf,player_rect)
        display_time(finish)

    pygame.display.update()
    clock.tick(fps)