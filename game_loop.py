import pygame, sys
import time
import random

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

		self.screen.blit(self.bg['image'],
			(-self.player.pos.x*0.5, -self.player.pos.y*0.2)
		)

		self.player.draw(self.screen, dt)
		
		if (self.player.pos - self.shirt.center).magnitude() < 400:
			self.shirt.display = False

		if self.shirt.display:
			self.shirt.draw(self.screen, dt, self.player.pos)
		if self.hat.display:
			self.hat.draw(self.screen, dt, self.player.pos)

		pygame.display.update()


