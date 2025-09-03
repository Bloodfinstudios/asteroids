# python
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    pygame.init()
    pygame.mixer.quit()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("My Pygame Window")
    clock = pygame.time.Clock()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        dt = clock.tick(60) / 1000
        player.update(dt) 
        
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()