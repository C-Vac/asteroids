import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while(True):
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            return
        screen.fill("BLACK")

        for obj in updatable:
          obj.update(dt)
        for obj in drawable:
          obj.draw(screen)



        pygame.display.flip()
        dt = clock.tick(60) / 1000

        # collision detection
        for obj in asteroids:
            if obj.check_for_collision(player):
              print("Game over!")
              return
            for shot in shots:
               if obj.check_for_collision(shot):
                  print("asteroid hit")
                  shot.kill()
                  obj.split()
                  break

           

if __name__ == "__main__":
    main()
