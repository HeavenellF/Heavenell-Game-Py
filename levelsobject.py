import pygame
def level1_object(width, height):
    level1_object = []
    
    platform1_surf = pygame.image.load('image/level/level1/Platform1.png').convert()
    platform1_rect = platform1_surf.get_rect(topleft=(8, 515))
    level1_object.append((platform1_surf, platform1_rect))

    platform2_surf = pygame.image.load('image/level/level1/Platform2.png').convert_alpha()
    platform2_rect = platform2_surf.get_rect(topleft=(-48, 409))
    level1_object.append((platform2_surf, platform2_rect))

    platform3_surf = pygame.image.load('image/level/level1/Platform3.png').convert_alpha()
    platform3_rect = platform3_surf.get_rect(topleft=(610, 410))
    level1_object.append((platform3_surf, platform3_rect))

    platform4_surf = pygame.image.load('image/level/level1/Platform4.png').convert_alpha()
    platform4_rect = platform4_surf.get_rect(topleft=(230, 232))
    level1_object.append((platform4_surf, platform4_rect))

    platform5_surf = pygame.image.load('image/level/level1/Platform5.png').convert_alpha()
    platform5_rect = platform5_surf.get_rect(topleft=(623, 76))
    level1_object.append((platform5_surf, platform5_rect))

    platform6_surf = pygame.image.load('image/level/level1/Platform6.png').convert_alpha()
    platform6_rect = platform6_surf.get_rect(topleft=(-2, -50))
    level1_object.append((platform6_surf, platform6_rect))

    return level1_object

def level2_object(width, height):
    level2_object = []
    
    platform1_surf = pygame.image.load('image/level/level2/Platform1.png').convert_alpha()
    platform1_rect = platform1_surf.get_rect(topleft=(-2, 571))
    level2_object.append((platform1_surf, platform1_rect))

    platform2_surf = pygame.image.load('image/level/level2/Platform2.png').convert_alpha()
    platform2_rect = platform2_surf.get_rect(topleft=(360, 395))
    level2_object.append((platform2_surf, platform2_rect))

    platform3_surf = pygame.image.load('image/level/level2/Platform3.png').convert_alpha()
    platform3_rect = platform3_surf.get_rect(topleft=(164, 209))
    level2_object.append((platform3_surf, platform3_rect))

    platform4_surf = pygame.image.load('image/level/level2/Platform4.png').convert_alpha()
    platform4_rect = platform4_surf.get_rect(topleft=(-267, 86))
    level2_object.append((platform4_surf, platform4_rect))

    platform5_surf = pygame.image.load('image/level/level2/Platform5.png').convert_alpha()
    platform5_rect = platform5_surf.get_rect(topleft=(229, -29))
    level2_object.append((platform5_surf, platform5_rect))

    return level2_object
