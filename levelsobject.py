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

