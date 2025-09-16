import pygame, sys
import time
import random
import math

def player_input(events, player):
	for event in events:
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				player.move_left()
			if event.key == pygame.K_d:
				player.move_right()
			if event.key == pygame.K_SPACE:
				player.jump()
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				player.dir *= 0
			if event.key == pygame.K_d:
				player.dir *= 0

def tile_bg(self):
    parallax = 0.2
    x_pos = -self.player.pos.x * parallax
    y_pos = -self.player.pos.y * parallax
    rect = self.bg['image'].get_rect()
    
    num_tiles = (self.WINDOW_WIDTH // rect.width) + 2
    start_x = (x_pos%rect.width) - rect.width
    
    for i in range(num_tiles):
        self.screen.blit(self.bg['image'], (start_x + i * rect.width, y_pos))

def clouds(self, dt):
	for cloud in self.clouds:
		cloud['floaty'] += dt * random.random()
		floaty = math.sin(cloud['floaty']) * 10
		x = cloud['pos'].x - (self.player.pos.x * cloud['parallax'])
		y = cloud['pos'].y - (self.player.pos.y * cloud['parallax']) + floaty
		self.screen.blit(cloud['image'], (x, y))
		cloud['pos'].x -= cloud['speed'] * dt

def game_loop(self):
	while True:
		self.screen.fill(self.WHITE)
		events = pygame.event.get()
		mouse = None
		for event in events:
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse = event.pos
		player_input(events, self.player)

		dt = self.clock.tick(60) / 1000

		self.player.update(dt)

		tile_bg(self)

		if self.show_clouds:
			clouds(self, dt)

		self.player.draw(self.screen, dt)

		if self.shirt.collides_with((self.player.pos + self.center)):
			self.shirt.display = False

		if self.shirt.display:
			self.shirt.draw(self.screen, dt, self.player.pos)
		if self.hat.display:
			self.hat.draw(self.screen, dt, self.player.pos)

		pygame.display.update()


