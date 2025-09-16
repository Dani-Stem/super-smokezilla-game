import pygame
from pygame.math import Vector2 as vec

class Player2:
	def __init__(self, center):
		self.center = center
		self.pos = vec(0,0)
		self.vel = vec(0,0)
		self.dir = vec(0,0)
		self.speed = 250
		self.jump_vel = -320
		self.gravity = 700
		self.grounded = True
		
		self.load_animations()

	def load_animations(self):
		self.anims = {}
		self.cur_anim = 'idle'
		self.flipped = False
		animations = {'idle':6, 'idle_clothed':7, 'jump':7,
			'walk':6, 'walk_clothed':6, 'walk_shirt':6
		}
		for anim, num_frames in animations.items():
			self.anims[anim] = {}
			self.anims[anim]['frame_index'] = 0
			self.anims[anim]['frames'] = []
			self.anims[anim]['num_frames'] = num_frames
			self.anims[anim]['frame_rate'] = 6
			for i in range(num_frames):
				self.anims[anim]['frames'].append(pygame.image.load(f"images/{anim}/{i}.png").convert_alpha())

	def update_anims(self, dt):
		if self.dir.x < 0:
			self.cur_anim = 'walk'
			self.flipped = True
		elif self.dir.x > 0:
			self.cur_anim = 'walk'
			self.flipped = False

		if self.dir.x == 0:
			self.cur_anim = 'idle'
			
		anim = self.anims[self.cur_anim]
		index = anim['frame_index']

		anim['frame_index'] += 8 * dt
		anim['frame_index'] %= anim['num_frames']
		
		img = anim['frames'][int(index)]
		if self.flipped:
			flipped_img = pygame.transform.flip(img, True, False)
			return flipped_img

		return img

	def jump(self):
		if not self.grounded:
			return

		self.vel.y += self.jump_vel
		self.grounded = False

	def move_left(self):
		self.dir.x = -1
		
	def move_right(self):
		self.dir.x = 1

	def draw(self, screen, dt):
		img = self.update_anims(dt)
		rect = img.get_rect()
		rect.center = (self.center.x, self.center.y)
		screen.blit(img, rect)

	def collision(self):
		# ground level
		if self.pos.y > 0:
			self.pos.y = 0
			self.vel.y = 0
			self.grounded = True

	def update(self, dt):
		self.pos += self.vel * dt
		self.pos += self.dir * self.speed * dt
		
		# gravity
		self.vel.y += self.gravity * dt

		self.collision()

