import pygame
import random

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE
from asteroid import Asteroid

class AsteroidField(pygame.sprite.Sprite):
    """
    Represents the Asteroid Field

    Attributes
    ----------
        edges - list of vectors to calculate direction and spawn edge
    
    Methods
    -------
        spawn(position: int, velocity: int, radius: int) -> None
            Spawns the new asteroid 

        update(delta_time: int) -> None
            Calculates spawn of a new asteroid
    """

    edges = [
        [
            pygame.Vector2(1, 0), # Move right
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT), # Spawn at left edge
        ],
        [
            pygame.Vector2(-1, 0), # Move left
            lambda y: pygame.Vector2(ASTEROID_MAX_RADIUS + SCREEN_WIDTH, y * SCREEN_HEIGHT), # Spawn at right edge
        ],
        [
            pygame.Vector2(0, 1), # Move up
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS), # Spawn at bottom edge
        ],
        [
            pygame.Vector2(0, -1), # Move down
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, ASTEROID_MAX_RADIUS + SCREEN_HEIGHT), # Spawn at top edge
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, position:int, velocity:int, radius:int) -> None:
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity
    
    def update(self, delta_time:int) -> None:
        self.spawn_timer += delta_time

        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # Spawn a new asteroid at a random edge
            edge:list = random.choice(self.edges)
            speed:int = random.randint(40, 100)
            velocity:pygame.Vector2 = edge[0] * speed
            velocity.rotate(random.randint(-30, 30))

            position:int = edge[1](random.uniform(0, 1)) # Executes lambda with random number
            kind:int = random.randint(1, ASTEROID_KINDS)
            self.spawn(position, velocity, ASTEROID_MIN_RADIUS * kind)