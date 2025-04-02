# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from circleshape import CircleShape
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (bullets, updatable, drawable)

    player = Player(x,y)
    asteroid_field = AsteroidField()


#glowna petla gry
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        updatable.update(dt)

        screen.fill("black")

        for object in drawable:
            object.draw(screen)

        for obj in asteroids:
            if obj.collision_check(player):
                exit("Game over!")

        for obj in asteroids:
            for obj2 in bullets:
                if obj.collision_check(obj2):
                    obj.split()
                    obj2.kill()
            
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        



if __name__ == "__main__":
    main()

