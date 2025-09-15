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

		# test platforms
		plats = [
			pygame.Rect(500,640,120,20),
			pygame.Rect(600,620,80,20),
			pygame.Rect(700,650,50,20),
			pygame.Rect(800,630,100,20),
			pygame.Rect(1000,620,300,20)
		]
		for plat in plats:
			plat.x -= self.player.pos.x
			plat.y -= self.player.pos.y
			pygame.draw.rect(self.screen, "green", plat)

		pygame.display.update()


