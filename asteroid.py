import pygame
from circleshape import CircleShape
from player import Player  

class Asteroid(CircleShape):
    containers = ()  

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.center = self.position

        for group in self.containers:
             group.add(self)