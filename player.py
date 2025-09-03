from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED
import pygame
from main import dt

class Player(CircleShape):
    def __init__(self, x, y, rotate):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.rotate = rotate 
        self.rotate = rotate + PLAYER_TURN_SPEED * dt 
# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [(a.x, a.y), (b.x, b.y), (c.x, c.y)]

    def draw(self, screen):
        pygame.draw.polygon(screen, pygame.Color('white'), self.triangle(), 2)
   