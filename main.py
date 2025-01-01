import pygame

from constants import *
from player import Player

def main():
    print("Starting Asteroids!")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0 # time since last frame drawn

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        player:Player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        player.draw(screen)
        
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000 # limit framemate to 60 FPS
   
if (__name__ == "__main__"):
    main()