import pygame
import random

from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    """
    Represents an Asteroid

    Attributes
    ----------
        x: int - x position
        y: int - y position
        radius: int - radius of asteroid

    Methods
    -------
        draw(screen: Surface) -> None
            Draws the asteroid on the screen

        update(delta_time: int) -> None
            Moves the asteroid forwards

        split() -> None
            Splits the asteroid into two if possible
    """

    def __init__(self, x:int, y:int, radius:int):
        super().__init__(x, y, radius)

    def draw(self, screen:pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, delta_time:int) -> None:
        self.position += self.velocity * delta_time
    
    def split(self) -> None:
        self.kill()

        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        
        random_degree:int = random.uniform(20, 50)
        vector1:pygame.Vector2 = self.velocity.rotate(-random_degree)
        vector2:pygame.Vector2 = self.velocity.rotate(random_degree) 
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position[0] + self.radius, self.position[1], new_radius)
        asteroid1.velocity = vector1 * 1.2

        asteroid2 = Asteroid(self.position[0], self.position[1] + self.radius, new_radius)
        asteroid2.velocity = vector2 * 1.2
        