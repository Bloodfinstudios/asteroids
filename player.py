from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_MOVEMENT, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, SHOOT_COOLDOWN  
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0  # cooldown timer starts at 0

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
            self.move(dt, direction=1)
        if keys[pygame.K_s]:
            self.position -= disp
            self.move(dt, direction=-1)

        # Update the shooting cooldown timer
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
            if self.shoot_timer < 0:
                self.shoot_timer = 0

    def move(self, dt, direction=1):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction

    def shoot(self):
        if self.shoot_timer <= 0:
            direction = pygame.Vector2(0, -1).rotate(self.rotation)  
            velocity = direction * PLAYER_SHOOT_SPEED
            shot = Shot(self.position.x, self.position.y, velocity)
            self.shoot_timer = SHOOT_COOLDOWN    
            return shot
        else:
            return None

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


