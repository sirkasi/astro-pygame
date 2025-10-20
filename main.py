import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable, drawable = pygame.sprite.Group(), pygame.sprite.Group()
    Player.containers = updateable, drawable

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y, PLAYER_RADIUS)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for item in updateable:
            item.update(dt)

        screen.fill("black")
        
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(144) / 1000
       
    
    


if __name__ == "__main__":
    main()
