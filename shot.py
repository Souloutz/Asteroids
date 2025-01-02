import pygame

from circleshape import CircleShape

class Shot(CircleShape):
    """
    Represents a Shot

    Attributes
    ----------
        x: int - x position
        y: int - y position
        radius: int - radius of shot

    Methods
    -------
        draw(screen: Surface) -> None
            Draws the shot on the screen

        update(delta_time: int) -> None
            Moves the shot forwards
    """

    def __init__(self, x:int, y:int, radius:int):
        super().__init__(x, y, radius)

    def draw(self, screen:pygame.Surface) -> None:
        pygame.draw.circle(screen, "green", self.position, self.radius, 2)

    def update(self, delta_time:int) -> None:
        self.position += self.velocity * delta_time