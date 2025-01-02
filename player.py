import pygame

from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, SHOT_SPEED
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    """
    Represents a Player

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
            Rotates the player triangle left and right

        move(delta_time: int) ->
            Moves the player triangle forwards and backwards

        draw(screen: Surface) -> None
            Draws the player triangle on the screen

        update(delta_time: int) -> None
            Updates the player triangle on the screen

        shoot() -> None
            Creates a new shot
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

    def move(self, delta_time: int) -> None:
        self.position += pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * delta_time

    def draw(self, screen:pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def update(self, delta_time: int) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-delta_time)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(delta_time)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(delta_time)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-delta_time)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self) -> None:
        shot = Shot(self.triangle()[0], self.position[1], SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * SHOT_SPEED