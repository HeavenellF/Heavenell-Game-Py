import pygame
def level1_object(width, height):
    level1_object = []
    
    platform1_surf = pygame.image.load('image/misc/ButtonMain.png').convert()
    platform_1_rect = platform1_surf.get_rect(topleft=(width/2-200, height-60))
    level1_object.append((platform1_surf, platform_1_rect))

    platform2_surf = pygame.image.load('image/misc/ButtonMain.png').convert()
    platform_2_rect = platform2_surf.get_rect(topleft=(width-200, height-300))
    level1_object.append((platform2_surf, platform_2_rect))

    # platform3_surf = pygame.image.load('image/misc/ButtonMain.png').convert()
    # platform_3_rect = platform3_surf.get_rect(topleft=(100, 200))
    # level1_object.append((platform3_surf, platform_3_rect))

    return level1_object

def level2_object(width, height):
    level2_object = []
    
    platform1_surf = pygame.image.load('image/misc/ButtonMain.png').convert()
    platform_1_rect = platform1_surf.get_rect(topleft=(width/2, height-60))
    level2_object.append((platform1_surf, platform_1_rect))

    platform2_surf = pygame.image.load('image/misc/ButtonMain.png').convert()
    platform_2_rect = platform2_surf.get_rect(topleft=(0, height-400))
    level2_object.append((platform2_surf, platform_2_rect))

    # platform3_surf = pygame.image.load('image/misc/ButtonMain.png').convert()
    # platform_3_rect = platform3_surf.get_rect(topleft=(100, 200))
    # level1_object.append((platform3_surf, platform_3_rect))

    return level2_object
