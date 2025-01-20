import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player1 = Player(x, y)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for u in updatable:    
            u.update(dt)
        
        screen.fill("black")

        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(144) / 1000 # test if 144 is OK

if __name__ == "__main__":
    main()

