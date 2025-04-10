from constants import *
from player import Player
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys



def main():
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
    
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	asteroid_1 = pygame.sprite.Group()
	asteroid_2 = pygame.sprite.Group()
	
	Asteroid.containers = (asteroid_1, asteroid_2,  asteroids,updatable, drawable)
	AsteroidField.containers= (updatable)
	asteroid_field = AsteroidField()
	
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	Shot.containers = (shots, updatable, drawable)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		updatable.update(dt)
		 
		
		for asteroid in asteroids:
			if asteroid.check_collision(player):
				print("Game Over!")
				sys.exit()
		
			for bullet in shots:
				if bullet.check_collision(asteroid):
					asteroid.split()
					bullet.kill()
		
		screen.fill("black")

		for obj in drawable:
			obj.draw(screen)
		
		pygame.display.flip()
		
		
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
