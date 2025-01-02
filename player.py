import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_LIVES, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_COOLDOWN, PLAYER_RESPAWN_COOLDOWN, SHOT_RADIUS, SHOT_SPEED
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
            default to 180 (facing upwards)
        timer: int - timer until player can shoot again
        respawn_timer: int - timer after being respawned where the player is invincible
        lives: int - number of lives a player has
        
    Methods
    -------
        get_respawn_timer() -> int
            Return the player's respawn timer

        get_lives() -> int
            Return the number of lives remaining

        lose_life() -> None
            Reduces a player's life    
    
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

        respawn() -> Player
            Respawns the player, resetting their respawn timer and lowering their lives
    """

    def __init__(self, x:int, y:int, rotation:int=180):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = rotation
        self.timer = 0
        self.respawn_timer = 0
        self.lives = PLAYER_LIVES

    def get_respawn_timer(self) -> int:
        return self.respawn_timer
    
    def get_lives(self) -> int:
        return self.lives
    
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

        if (self.respawn_timer <= 0):
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.rotate(-delta_time)
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.rotate(delta_time)
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.move(delta_time)
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.move(-delta_time)
            if keys[pygame.K_SPACE]:
                if self.timer <= 0:
                    self.shoot()

        self.timer -= delta_time
        self.respawn_timer -= delta_time

    def shoot(self) -> None:
        self.timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.triangle()[0], self.position[1], SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * SHOT_SPEED

    def respawn(self):
        lives:int = self.lives
        self.kill()

        player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 180)
        player.respawn_timer = PLAYER_RESPAWN_COOLDOWN
        player.lives = lives - 1
        return player