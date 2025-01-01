import pygame

from constants import PLAYER_RADIUS
from circleshape import CircleShape

class Player(CircleShape):
    """
    Represents a Player - extends CircleShape

    Attributes
    ----------
        x: int - x position
        y: int - y position
        rotation: int - degree of rotation (out of 360)
        
    Methods
    -------
        triangle() -> list
            Returns the three points of the player triangle

        draw(screen: Surface) -> None
            Draws the player on the screen
    """

    rotation:int = 0

    def __init__(self, x:int, y:int):
        super().__init__(x, y, PLAYER_RADIUS)

    def triangle(self) -> list:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen:pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        
