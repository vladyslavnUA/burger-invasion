import pygame

# importing necessary pygame local actions
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# player object
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

pygame.init()

# drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()

# set game active until user quits
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # white background
    screen.fill((0, 0, 0))
    screen.blit(player.surf, player.rect)
    pygame.display.flip()

# game surface
# screen.fill((255, 255, 255))
# surf = pygame.Surface((50, 50))
# suft.fill((0, 0, 0))   # color
# rect = surf.get_srect()

# pygame.display.flip()
# surf_center = (
#     (SCREEN_WIDTH-surf.get_width())/2,
#     (SCREEN_HEIGHT-surf.get_height())/2
# )
# screen.blit(surf, surf_center)    # center
# pygame.display.flip()

# screen.fill((255, 255, 255))





pygame.quit()