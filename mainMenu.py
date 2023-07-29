import pygame

def mainMenu_elements(width, height, font1, font3, button_surf):
    gameTitle_surf = font1.render('Agent J', True, 'Black')
    gameTitle_rect = gameTitle_surf.get_rect(midtop=(width / 2, 30))

    button_rectPlay = button_surf.get_rect(midtop=(width / 2, height / 2 - 90))
    button_rectSetting = button_surf.get_rect(midtop=(width / 2, height / 2))
    button_rectExit = button_surf.get_rect(midtop=(width / 2, height / 2 + 90))

    buttonPlay_surf = font3.render('Play', True, 'Black')
    buttonPlay_rect = buttonPlay_surf.get_rect(midtop=(width / 2, height / 2 - 85))

    buttonSetting_surf = font3.render('Setting', True, 'Black')
    buttonSetting_rect = buttonSetting_surf.get_rect(midtop=(width / 2, height / 2 + 5))

    buttonExit_surf = font3.render('Exit', True, 'Black')
    buttonExit_rect = buttonExit_surf.get_rect(midtop=(width / 2, height / 2 + 95))

    return {
        'gameTitle_surf': gameTitle_surf,
        'gameTitle_rect': gameTitle_rect,
        'button_rectPlay': button_rectPlay,
        'button_rectSetting': button_rectSetting,
        'button_rectExit': button_rectExit,
        'buttonPlay_surf': buttonPlay_surf,
        'buttonPlay_rect': buttonPlay_rect,
        'buttonSetting_surf': buttonSetting_surf,
        'buttonSetting_rect': buttonSetting_rect,
        'buttonExit_surf': buttonExit_surf,
        'buttonExit_rect': buttonExit_rect,
    }