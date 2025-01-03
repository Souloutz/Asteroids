import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0 # time since last frame drawn

    background_image:pygame.Surface = pygame.image.load("background.jpg").convert_alpha()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while (player.get_lives() != 0):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for element in updatable:
            element.update(delta_time)

        for asteroid in asteroids:
            collided:bool = asteroid.check_collision(player)

            if (collided and player.get_respawn_timer() <= 0):
                player = player.respawn()
            
            for shot in shots:
                collided:bool = shot.check_collision(asteroid)

                if (collided):
                    shot.kill()
                    asteroid.split()
                
        # screen.fill("black")
        screen.blit(background_image, (0, 0))

        for element in drawable:
            element.draw(screen)
        
        pygame.display.flip() # refreshes the screen
        delta_time = clock.tick(60) / 1000 # limit framemate to 60 FPS

    print("Game Over!")
    pygame.quit()
   
if (__name__ == "__main__"):
    main()