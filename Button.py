import pygame

def mainMenu_elements(width, height, font1, font3, button_surf1):
    gameTitle_surf = font1.render('Agent J', True, 'Black')
    gameTitle_rect = gameTitle_surf.get_rect(midtop=(width / 2, 65))

    button_rectPlay = button_surf1.get_rect(midtop=(width / 2, height / 2 - 135))
    button_rectSetting = button_surf1.get_rect(midtop=(width / 2, height / 2))
    button_rectExit = button_surf1.get_rect(midtop=(width / 2, height / 2 + 135))

    buttonPlay_surf = font3.render('Play', True, 'Black')
    buttonPlay_rect = buttonPlay_surf.get_rect(midtop=(width / 2, height / 2 - 130))

    buttonSetting_surf = font3.render('Setting', True, 'Black')
    buttonSetting_rect = buttonSetting_surf.get_rect(midtop=(width / 2, height / 2 + 10))

    buttonExit_surf = font3.render('Exit', True, 'Black')
    buttonExit_rect = buttonExit_surf.get_rect(midtop=(width / 2, height / 2 + 135))

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

def gameOver_elements(width, height, font1, font3, button_surf1):
    gameOver_surf = font3.render('You\'ve Completed the Game!', True, 'Black')
    gameOver_rect = gameOver_surf.get_rect(midtop=(width / 2, 65))

    button_rectPlayAgain = button_surf1.get_rect(midtop=(width / 2, height / 2 - 135))
    button_rectMainMenu = button_surf1.get_rect(midtop=(width / 2, height / 2))
    button_rectExit = button_surf1.get_rect(midtop=(width / 2, height / 2 + 135))

    buttonPlayAgain_surf = font3.render('Play Again', True, 'Black')
    buttonPlayAgain_rect = buttonPlayAgain_surf.get_rect(midtop=(width / 2, height / 2 - 130))

    buttonMainMenu_surf = font3.render('Main Menu', True, 'Black')
    buttonMainMenu_rect = buttonMainMenu_surf.get_rect(midtop=(width / 2, height / 2 + 10))

    buttonExit_surf = font3.render('Exit', True, 'Black')
    buttonExit_rect = buttonExit_surf.get_rect(midtop=(width / 2, height / 2 + 135))

    return {
        'gameOver_surf': gameOver_surf,
        'gameOver_rect': gameOver_rect,
        'button_rectPlayAgain': button_rectPlayAgain,
        'button_rectMainMenu': button_rectMainMenu,
        'button_rectExit': button_rectExit,
        'buttonPlayAgain_surf': buttonPlayAgain_surf,
        'buttonPlayAgain_rect': buttonPlayAgain_rect,
        'buttonMainMenu_surf': buttonMainMenu_surf,
        'buttonMainMenu_rect': buttonMainMenu_rect,
        'buttonExit_surf': buttonExit_surf,
        'buttonExit_rect': buttonExit_rect,
    }