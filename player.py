import pygame

from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED
from circleshape import CircleShape

class Player(CircleShape):
    """
    Represents a Player - extends CircleShape

    Attributes
    ----------
        x: int - x position
        y: int - y position
        rotation: int - degree of rotation (out of 360)
            default to 180
        
    Methods
    -------
        triangle() -> list
            Returns the three points of the player triangle

        rotate(delta_time: int) -> None
            Rotates the player triangle

        draw(screen: Surface) -> None
            Draws the player triangle on the screen

        update(delta_time: int) -> None
            Updates the player triangle on the screen
    """

    def __init__(self, x:int, y:int, rotation:int=180):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = rotation

    def triangle(self) -> list:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, delta_time:int) -> None:
        self.rotation += PLAYER_TURN_SPEED * delta_time

    def draw(self, screen:pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def update(self, delta_time: int) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-delta_time)
        if keys[pygame.K_d]:
            self.rotate(delta_time)
    

        
