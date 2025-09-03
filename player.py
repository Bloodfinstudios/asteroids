from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_MOVEMENT
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
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
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        disp = forward * PLAYER_MOVEMENT * dt

        if keys[pygame.K_w]:
            self.position += disp
        if keys[pygame.K_s]:
            self.position -= disp 

