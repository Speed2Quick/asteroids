import pygame
from constants import *
from asteroids import Asteroid
from asteroidfield import AsteroidField
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    Clock = pygame.time.Clock()
    dt = 0

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")
        
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = Clock.tick(60) / 1000


if __name__ == "__main__":
    main()
