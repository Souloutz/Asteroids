import pygame

class CircleShape(pygame.sprite.Sprite):
    """
    Represents a Circle - extends Sprite

    Base class for game objects
    
    Attributes
    ----------
        position: int - x, y position
        velocity: int - speed in direction
        radius: int - radius of circle

    Methods
    -------
        draw() -> None
            Draws the game object on the screen

        update() -> None
            Update the game object on the screen

        check_collision(object: CircleShape) -> bool
            Check if a collision occurred
    """

    def __init__(self, x:int, y:int, radius:int):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen:pygame.Surface) -> None:
        pass

    def update(self, delta_time:int) -> None:
        pass

    def check_collision(self, object) -> bool:
        distance:int = self.position.distance_to(object.position)
        radii_distance:int = self.radius + object.radius

        if (distance > radii_distance):
            return False

        return True