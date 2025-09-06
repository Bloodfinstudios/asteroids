import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    font = pygame.font.Font(None, 72)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                screen.fill("black")
                text_surf = font.render("Game Over!", True, pygame.Color("white"))
                text_rect = text_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                screen.blit(text_surf, text_rect)
                pygame.display.flip()
                pygame.time.wait(1500)  
                sys.exit()

        for obj in drawable:
           obj.draw(screen)       

        pygame.display.flip()        

        dt = clock.tick(60) / 1000 

if __name__ == "__main__":
    main()