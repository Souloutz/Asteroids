import pygame

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
    """

    def __init__(self, x:int, y:int, radius:int):
        super().__init__(x, y, radius)

    def draw(self, screen:pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius, 2)

    def update(self, delta_time:int) -> None:
        self.position += self.velocity * delta_time