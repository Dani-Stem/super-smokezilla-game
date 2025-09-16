import pygame
from pygame.math import Vector2 as vec

class Hat:
	def __init__(self, center):
		self.center = center
		self.pos = vec(0,0)
		self.dir = vec(0,0)
		self.display = True
		
		self.load_animations_hat()

	def load_animations_hat(self):
		self.anims = {}
		self.flipped = False
		animations = {'hat':4,}
		for anim, num_frames in animations.items():
			self.anims[anim] = {}
			self.anims[anim]['frame_index'] = 0
			self.anims[anim]['frames'] = []
			self.anims[anim]['num_frames'] = num_frames
			self.anims[anim]['frame_rate'] = 4
			for i in range(num_frames):
				self.anims[anim]['frames'].append(pygame.image.load(f"images/{anim}/{i}.png").convert_alpha())

	def update_anims(self, dt):
		self.cur_anim = 'hat'
			
		anim = self.anims[self.cur_anim]
		index = anim['frame_index']

		anim['frame_index'] += 8 * dt
		anim['frame_index'] %= anim['num_frames']
		
		img = anim['frames'][int(index)]
		if self.flipped:
			flipped_img = pygame.transform.flip(img, True, False)
			return flipped_img

		return img

	def draw(self, screen, dt, player):
		img = self.update_anims(dt)
		rect = img.get_rect()
		rect.center = (self.center.x - player.x, self.center.y - player.y)
		screen.blit(img, rect)


