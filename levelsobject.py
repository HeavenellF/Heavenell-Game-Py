import pygame
def level1_object(width, height):
    level1_object = []

    background_surf = pygame.image.load('image/level/level1/Background.png').convert()
    background_rect = background_surf.get_rect(topleft=(0,0))
    level1_object.append((background_surf, background_rect, False))

    platform1_surf = pygame.image.load('image/level/level1/Platform1.png').convert()
    platform1_rect = platform1_surf.get_rect(topleft=(166, 825))
    level1_object.append((platform1_surf, platform1_rect, True))

    platform2_surf = pygame.image.load('image/level/level1/Platform2.png').convert_alpha()
    platform2_rect = platform2_surf.get_rect(topleft=(-166, 724))
    level1_object.append((platform2_surf, platform2_rect, True))

    platform3_surf = pygame.image.load('image/level/level1/Platform3.png').convert_alpha()
    platform3_rect = platform3_surf.get_rect(topleft=(958, 724))
    level1_object.append((platform3_surf, platform3_rect, True))

    platform4_surf = pygame.image.load('image/level/level1/Platform4.png').convert_alpha()
    platform4_rect = platform4_surf.get_rect(topleft=(336, 462))
    level1_object.append((platform4_surf, platform4_rect, True))

    platform5_surf = pygame.image.load('image/level/level1/Platform5.png').convert_alpha()
    platform5_rect = platform5_surf.get_rect(topleft=(958, 216))
    level1_object.append((platform5_surf, platform5_rect, True))

    platform6_surf = pygame.image.load('image/level/level1/Platform6.png').convert_alpha()
    platform6_rect = platform6_surf.get_rect(topleft=(-66, -15))
    level1_object.append((platform6_surf, platform6_rect, True))

    return level1_object

def level2_object(width, height):
    level2_object = []

    background_surf = pygame.image.load('image/level/level2/Background.png').convert()
    background_rect = background_surf.get_rect(topleft=(0,0))
    level2_object.append((background_surf, background_rect, False))
    
    platform1_surf = pygame.image.load('image/level/level2/Platform1.png').convert_alpha()
    platform1_rect = platform1_surf.get_rect(topleft=(-66, 871))
    level2_object.append((platform1_surf, platform1_rect, True))

    platform2_surf = pygame.image.load('image/level/level2/Platform2.png').convert_alpha()
    platform2_rect = platform2_surf.get_rect(topleft=(426, 604))
    level2_object.append((platform2_surf, platform2_rect, True))

    platform3_surf = pygame.image.load('image/level/level2/Platform3.png').convert_alpha()
    platform3_rect = platform3_surf.get_rect(topleft=(265, 345))
    level2_object.append((platform3_surf, platform3_rect, True))

    platform4_surf = pygame.image.load('image/level/level2/Platform4.png').convert_alpha()
    platform4_rect = platform4_surf.get_rect(topleft=(-80, 161))
    level2_object.append((platform4_surf, platform4_rect, True))

    platform5_surf = pygame.image.load('image/level/level2/Platform5.png').convert_alpha()
    platform5_rect = platform5_surf.get_rect(topleft=(370, -51))
    level2_object.append((platform5_surf, platform5_rect, True))

    return level2_object

def level3_object(width, height):
    level3_object = []

    background_surf = pygame.image.load('image/level/level3/Background.png').convert()
    background_rect = background_surf.get_rect(topleft=(0,0))
    level3_object.append((background_surf, background_rect, False))

    platform1_surf = pygame.image.load('image/level/level3/Platform1.png').convert_alpha()
    platform1_rect = platform1_surf.get_rect(topleft=(370, 863))
    level3_object.append((platform1_surf, platform1_rect, True))

    platform2_surf = pygame.image.load('image/level/level3/Platform2.png').convert_alpha()
    platform2_rect = platform2_surf.get_rect(topleft=(-150, -44))
    level3_object.append((platform2_surf, platform2_rect, True))

    platform3_surf = pygame.image.load('image/level/level3/Platform3.png').convert_alpha()
    platform3_rect = platform3_surf.get_rect(topleft=(671, -258))
    level3_object.append((platform3_surf, platform3_rect, True))

    platform4_surf = pygame.image.load('image/level/level3/Platform4.png').convert_alpha()
    platform4_rect = platform4_surf.get_rect(topleft=(370, 612))
    level3_object.append((platform4_surf, platform4_rect, True))

    platform5_surf = pygame.image.load('image/level/level3/Platform5.png').convert_alpha()
    platform5_rect = platform4_surf.get_rect(topleft=(370, 362))
    level3_object.append((platform5_surf, platform5_rect, True))

    platform6_surf = pygame.image.load('image/level/level3/Platform6.png').convert_alpha()
    platform6_rect = platform6_surf.get_rect(topleft=(370, 112))
    level3_object.append((platform6_surf, platform6_rect, True))

    return level3_object

def level4_object(width, height):
    level4_object = []

    background_surf = pygame.image.load('image/level/level4/Background.png').convert()
    background_rect = background_surf.get_rect(topleft=(0,0))
    level4_object.append((background_surf, background_rect, False))

    platform1_surf = pygame.image.load('image/level/level4/Platform1.png').convert_alpha()
    platform1_rect = platform1_surf.get_rect(topleft=(671, 806))
    level4_object.append((platform1_surf, platform1_rect, True))

    platform2_surf = pygame.image.load('image/level/level4/Platform2.png').convert_alpha()
    platform2_rect = platform2_surf.get_rect(topleft=(666, 559))
    level4_object.append((platform2_surf, platform2_rect, True))

    platform3_surf = pygame.image.load('image/level/level4/Platform3.png').convert_alpha()
    platform3_rect = platform3_surf.get_rect(topleft=(117, 341))
    level4_object.append((platform3_surf, platform3_rect, True))

    platform4_surf = pygame.image.load('image/level/level4/Platform4.png').convert_alpha()
    platform4_rect = platform4_surf.get_rect(topleft=(750, 260))
    level4_object.append((platform4_surf, platform4_rect, True))

    platform5_surf = pygame.image.load('image/level/level4/Platform5.png').convert_alpha()
    platform5_rect = platform5_surf.get_rect(topleft=(-105, -41))
    level4_object.append((platform5_surf, platform5_rect, True))

    platform6_surf = pygame.image.load('image/level/level4/Platform6.png').convert_alpha()
    platform6_rect = platform6_surf.get_rect(topleft=(-150, 804))
    level4_object.append((platform6_surf, platform6_rect, True))

    return level4_object

def level5_object(width, height):
    level5_object = []

    background_surf = pygame.image.load('image/level/level5/Background.png').convert()
    background_rect = background_surf.get_rect(topleft=(0,0))
    level5_object.append((background_surf, background_rect, False))

    platform1_surf = pygame.image.load('image/level/level5/Platform1.png').convert_alpha()
    platform1_rect = platform1_surf.get_rect(topleft=(-105, 865))
    level5_object.append((platform1_surf, platform1_rect, True))

    platform2_surf = pygame.image.load('image/level/level5/Platform2.png').convert_alpha()
    platform2_rect = platform2_surf.get_rect(topleft=(920, 655))
    level5_object.append((platform2_surf, platform2_rect, True))

    platform3_surf = pygame.image.load('image/level/level5/Platform3.png').convert_alpha()
    platform3_rect = platform3_surf.get_rect(topleft=(920, 382))
    level5_object.append((platform3_surf, platform3_rect, True))

    platform4_surf = pygame.image.load('image/level/level5/Platform4.png').convert_alpha()
    platform4_rect = platform4_surf.get_rect(topleft=(131, 208))
    level5_object.append((platform4_surf, platform4_rect, True))

    platform5_surf = pygame.image.load('image/level/level5/Platform5.png').convert_alpha()
    platform5_rect = platform5_surf.get_rect(topleft=(914, -28))
    level5_object.append((platform5_surf, platform5_rect, True))

    return level5_object

def level6_object(width, height):
    level6_object = []

    background_surf = pygame.image.load('image/level/level6/Background.png').convert()
    background_rect = background_surf.get_rect(topleft=(0,0))
    level6_object.append((background_surf, background_rect, False))

    platform1_surf = pygame.image.load('image/level/level6/Platform1.png').convert_alpha()
    platform1_rect = platform1_surf.get_rect(topleft=(914, 864))
    level6_object.append((platform1_surf, platform1_rect, True))

    platform2_surf = pygame.image.load('image/level/level6/Platform2.png').convert_alpha()
    platform2_rect = platform2_surf.get_rect(center=(600, 700))
    level6_object.append((platform2_surf, platform2_rect, True))

    platform3_surf = pygame.image.load('image/level/level6/Platform3.png').convert_alpha()
    platform3_rect = platform3_surf.get_rect(center=(1090, 500))
    level6_object.append((platform3_surf, platform3_rect, True))

    platform4_surf = pygame.image.load('image/level/level6/Platform4.png').convert_alpha()
    platform4_rect = platform4_surf.get_rect(center=(1120, 140))
    level6_object.append((platform4_surf, platform4_rect, True))

    platform5_surf = pygame.image.load('image/level/level6/Platform5.png').convert_alpha()
    platform5_rect = platform5_surf.get_rect(center=(110, 500))
    level6_object.append((platform5_surf, platform5_rect, True))

    platform6_surf = pygame.image.load('image/level/level6/Platform6.png').convert_alpha()
    platform6_rect = platform6_surf.get_rect(center=(80, 140))
    level6_object.append((platform6_surf, platform6_rect, True))

    platform7_surf = pygame.image.load('image/level/level6/Platform7.png').convert_alpha()
    platform7_rect = platform7_surf.get_rect(center=(600, 300))
    level6_object.append((platform7_surf, platform7_rect, True))

    return level6_object

def level7_object(width, height):
    level7_object = []

    background_surf = pygame.image.load('image/level/level7/Background.png').convert()
    background_rect = background_surf.get_rect(topleft=(0,0))
    level7_object.append((background_surf, background_rect, False))

    platform1_surf = pygame.image.load('image/level/level7/Platform1.png').convert_alpha()
    platform1_rect = platform1_surf.get_rect(center=(600, 750))
    level7_object.append((platform1_surf, platform1_rect, True))

    platform2_surf = pygame.image.load('image/level/level7/Platform2.png').convert_alpha()
    platform2_rect = platform2_surf.get_rect(center=(1100, 575))
    level7_object.append((platform2_surf, platform2_rect, True))

    platform3_surf = pygame.image.load('image/level/level7/Platform3.png').convert_alpha()
    platform3_rect = platform3_surf.get_rect(center=(100, 575))
    level7_object.append((platform3_surf, platform3_rect, True))

    platform4_surf = pygame.image.load('image/level/level7/Platform4.png').convert_alpha()
    platform4_rect = platform4_surf.get_rect(center=(600, 400))
    level7_object.append((platform4_surf, platform4_rect, True))

    platform5_surf = pygame.image.load('image/level/level7/Platform5.png').convert_alpha()
    platform5_rect = platform5_surf.get_rect(center=(271, 150))
    level7_object.append((platform5_surf, platform5_rect, True))

    platform6_surf = pygame.image.load('image/level/level7/Platform6.png').convert_alpha()
    platform6_rect = platform6_surf.get_rect(center=(929, 150))
    level7_object.append((platform6_surf, platform6_rect, True))

    return level7_object

def level8_object(width, height):
    level8_object = []

    background_surf = pygame.image.load('image/level/level8/Background.png').convert()
    background_rect = background_surf.get_rect(topleft=(0,0))
    level8_object.append((background_surf, background_rect, False))

    platform1_surf = pygame.image.load('image/level/level8/Platform1.png').convert_alpha()
    platform1_rect = platform1_surf.get_rect(topleft=(-50, 730))
    level8_object.append((platform1_surf, platform1_rect, True))

    platform2_surf = pygame.image.load('image/level/level8/Platform2.png').convert_alpha()
    platform2_rect = platform2_surf.get_rect(center=(1050, 530))
    level8_object.append((platform2_surf, platform2_rect, True))

    platform3_surf = pygame.image.load('image/level/level8/Platform3.png').convert_alpha()
    platform3_rect = platform3_surf.get_rect(center=(750, 430))
    level8_object.append((platform3_surf, platform3_rect, True))

    platform4_surf = pygame.image.load('image/level/level8/Platform4.png').convert_alpha()
    platform4_rect = platform4_surf.get_rect(center=(450, 330))
    level8_object.append((platform4_surf, platform4_rect, True))

    platform5_surf = pygame.image.load('image/level/level8/Platform5.png').convert_alpha()
    platform5_rect = platform5_surf.get_rect(center=(150, 230))
    level8_object.append((platform5_surf, platform5_rect, True))

    platform6_surf = pygame.image.load('image/level/level8/Platform6.png').convert_alpha()
    platform6_rect = platform6_surf.get_rect(center=(1050, 65))
    level8_object.append((platform6_surf, platform6_rect, True))

    platform7_surf = pygame.image.load('image/level/level8/Platform7.png').convert_alpha()
    platform7_rect = platform7_surf.get_rect(center=(750, -35))
    level8_object.append((platform7_surf, platform7_rect, True))

    platform8_surf = pygame.image.load('image/level/level8/Platform8.png').convert_alpha()
    platform8_rect = platform8_surf.get_rect(center=(450, -135))
    level8_object.append((platform8_surf, platform8_rect, True))

    platform9_surf = pygame.image.load('image/level/level8/Platform9.png').convert_alpha()
    platform9_rect = platform9_surf.get_rect(topleft=(290, -120))
    level8_object.append((platform9_surf, platform9_rect, True))

    return level8_object

def levelend1_object(width, height):
    levelend1_object = []

    background_surf = pygame.image.load('image/level/levelend1/Background.png').convert()
    background_rect = background_surf.get_rect(topleft=(0,0))
    levelend1_object.append((background_surf, background_rect, False))

    platform1_surf = pygame.image.load('image/level/levelend1/Platform1.png').convert_alpha()
    platform1_rect = platform1_surf.get_rect(center=(400, 60))
    levelend1_object.append((platform1_surf, platform1_rect, True))

    platform2_surf = pygame.image.load('image/level/levelend1/Platform2.png').convert_alpha()
    platform2_rect = platform2_surf.get_rect(center=(800, 60))
    levelend1_object.append((platform2_surf, platform2_rect, True))

    platform3_surf = pygame.image.load('image/level/levelend1/Platform3.png').convert_alpha()
    platform3_rect = platform3_surf.get_rect(center=(770, 560))
    levelend1_object.append((platform3_surf, platform3_rect, True))

    platform4_surf = pygame.image.load('image/level/levelend1/Platform4.png').convert_alpha()
    platform4_rect = platform4_surf.get_rect(center=(430, 560))
    levelend1_object.append((platform4_surf, platform4_rect, True))

    platform5_surf = pygame.image.load('image/level/levelend1/Platform5.png').convert_alpha()
    platform5_rect = platform5_surf.get_rect(center=(770, 280))
    levelend1_object.append((platform5_surf, platform5_rect, True))

    platform6_surf = pygame.image.load('image/level/levelend1/Platform6.png').convert_alpha()
    platform6_rect = platform6_surf.get_rect(center=(430, 280))
    levelend1_object.append((platform6_surf, platform6_rect, True))

    platform7_surf = pygame.image.load('image/level/levelend1/Platform7.png').convert_alpha()
    platform7_rect = platform7_surf.get_rect(center=(770, 0))
    levelend1_object.append((platform7_surf, platform7_rect, True))

    platform8_surf = pygame.image.load('image/level/levelend1/Platform8.png').convert_alpha()
    platform8_rect = platform8_surf.get_rect(center=(430, 0))
    levelend1_object.append((platform8_surf, platform8_rect, True))

    platform9_surf = pygame.image.load('image/level/levelend1/Platform9.png').convert_alpha()
    platform9_rect = platform9_surf.get_rect(topleft=(290, 815))
    levelend1_object.append((platform9_surf, platform9_rect, True))

    return levelend1_object

def levelend2_object(width, height):
    levelend2_object = []

    background_surf = pygame.image.load('image/level/levelend2/Background.png').convert()
    background_rect = background_surf.get_rect(topleft=(0,0))
    levelend2_object.append((background_surf, background_rect, False))

    platform1_surf = pygame.image.load('image/level/levelend2/Platform1.png').convert_alpha()
    platform1_rect = platform1_surf.get_rect(center=(400, 750))
    levelend2_object.append((platform1_surf, platform1_rect, True))

    platform2_surf = pygame.image.load('image/level/levelend2/Platform2.png').convert_alpha()
    platform2_rect = platform2_surf.get_rect(center=(800, 750))
    levelend2_object.append((platform2_surf, platform2_rect, True))

    platform3_surf = pygame.image.load('image/level/levelend2/Platform3.png').convert_alpha()
    platform3_rect = platform3_surf.get_rect(center=(770, 900))
    levelend2_object.append((platform3_surf, platform3_rect, True))

    platform4_surf = pygame.image.load('image/level/levelend2/Platform4.png').convert_alpha()
    platform4_rect = platform4_surf.get_rect(center=(430, 900))
    levelend2_object.append((platform4_surf, platform4_rect, True))

    platform5_surf = pygame.image.load('image/level/levelend2/Platform5.png').convert_alpha()
    platform5_rect = platform5_surf.get_rect(center=(770, 620))
    levelend2_object.append((platform5_surf, platform5_rect, True))

    platform6_surf = pygame.image.load('image/level/levelend2/Platform6.png').convert_alpha()
    platform6_rect = platform6_surf.get_rect(center=(430, 620))
    levelend2_object.append((platform6_surf, platform6_rect, True))

    platform7_surf = pygame.image.load('image/level/levelend2/Platform7.png').convert_alpha()
    platform7_rect = platform7_surf.get_rect(center=(770, 340))
    levelend2_object.append((platform7_surf, platform7_rect, True))

    platform8_surf = pygame.image.load('image/level/levelend2/Platform8.png').convert_alpha()
    platform8_rect = platform8_surf.get_rect(center=(430, 340))
    levelend2_object.append((platform8_surf, platform8_rect, True))

    platform9_surf = pygame.image.load('image/level/levelend2/Platform9.png').convert_alpha()
    platform9_rect = platform9_surf.get_rect(center=(200, -80))
    levelend2_object.append((platform9_surf, platform9_rect, True))

    platform10_surf = pygame.image.load('image/level/levelend2/Platform10.png').convert_alpha()
    platform10_rect = platform10_surf.get_rect(center=(1000, -80))
    levelend2_object.append((platform10_surf, platform10_rect, True))

    platform11_surf = pygame.image.load('image/level/levelend2/Platform11.png').convert_alpha()
    platform11_rect = platform11_surf.get_rect(center=(600, 0))
    levelend2_object.append((platform11_surf, platform11_rect, True))

    return levelend2_object

def levelend3_object(width, height):
    levelend3_object = []

    background_surf = pygame.image.load('image/level/levelend3/Background.png').convert()
    background_rect = background_surf.get_rect(topleft=(0,0))
    levelend3_object.append((background_surf, background_rect, False))

    platform1_surf = pygame.image.load('image/level/levelend3/Platform1.png').convert_alpha()
    platform1_rect = platform1_surf.get_rect(center=(200, 795))
    levelend3_object.append((platform1_surf, platform1_rect, True))

    platform2_surf = pygame.image.load('image/level/levelend3/Platform2.png').convert_alpha()
    platform2_rect = platform1_surf.get_rect(center=(1000, 795))
    levelend3_object.append((platform2_surf, platform2_rect, True))

    platform3_surf = pygame.image.load('image/level/levelend3/Platform3.png').convert_alpha()
    platform3_rect = platform3_surf.get_rect(center=(600, 900))
    levelend3_object.append((platform3_surf, platform3_rect, True))

    platform4_surf = pygame.image.load('image/level/levelend3/Platform4.png').convert_alpha()
    platform4_rect = platform4_surf.get_rect(center=(600, 630))
    levelend3_object.append((platform4_surf, platform4_rect, True))

    return levelend3_object