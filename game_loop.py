import pygame, sys
import time
import random

def game_loop(self):
	self.game_music.play(loops=-1)
	while True:
		events = pygame.event.get()
		mouse = None
		for event in events:
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse = event.pos

		dt = self.clock.tick(60) / 1000
		
		self.all_sprites_group.customize_draw(
            self.player,
            self.screen,
            self.background,   

			)

		self.draw_sound_toggle(dt, mouse)
		pygame.display.update()


