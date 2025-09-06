import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid

def main():
    pygame.init()
    pygame.mixer.quit()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("My Pygame Window")
    clock = pygame.time.Clock()

    # Create pygame groups instead of lists
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Create player and add to groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    # Assign groups as containers for Asteroids
    Asteroid.containers = (asteroids, updatable, drawable)

    # Create asteroids; they auto-add to groups via containers
    asteroid1 = Asteroid(100, 100, 40)
    asteroid2 = Asteroid(300, 200, 25)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(60) / 1000

        for obj in updatable:
            obj.update(dt)

        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
