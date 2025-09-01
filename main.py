import pygame
from constants import *

pygame.init()
pygame.mixer.quit()
clock = pygame.time.Clock()



def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Pygame Window")

dt = 0

if __name__ == "__main__":
    main()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    screen.fill((0, 0, 0))  
    pygame.display.flip()
    clock.tick(60)
    dt = clock.tick(60) / 1000  
              

pygame.quit()

