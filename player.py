import pygame
import time
import random

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, groups, create_basketball, ):
		super().__init__(groups)
		self.group = groups
		self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 1215, 812
		self.status = "right"
		self.frame_index = 0
		self.direction = pygame.math.Vector2(1, 0)
		self.position = pygame.math.Vector2(pos)
		self.rect = None
		self.selected_player = "zilla"
		self.dttimer = 0
		self.import_assets()
		self.animation = self.animations["idle"]
		self.image = self.animation[self.frame_index]
		self.rect = self.image.get_rect(center=pos)
		self.create_basketball = create_basketball

		self.height = 0
		self.velocity = 0
		self.jump_speed = 400
		self.jump_start = 1
		self.gravity = -800
		
		self.love = True
		self.is_idle = False
		self.scale_factor = 1.0

		self.jump_sound = pygame.mixer.Sound("sounds/jump.wav")
		self.jump_sound.set_volume(0.05)

		self.landing_sound = pygame.mixer.Sound("sounds/land.ogg")
		self.landing_sound.set_volume(0.02)
		

	def load_animation(self, path, frame_count):
		images = []

		for i in range(frame_count):
			image_path = f"{path}{i}.png"
			image = pygame.image.load(image_path).convert_alpha()

			images.append(image)

		return images
	
	def import_assets(self):
		# Define animation types and frame counts
		animation_data = {
			"walk": ("walk/", 5),
			"jump": ("jump/", 6),
			"jump_shirt": ("jump_shirt/", 6),
			"walk_shirt": ("walk_shirt/", 5),
			"walk_clothed": ("walk_clothed/", 5),
			"idle": ("idle/", 5),
		}
		
		base_path = f"images/"
		
		self.animations = {
			key: self.load_animation(base_path + path, frames)
			for key, (path, frames) in animation_data.items()
		}
		
	def input(self, events, dt, screen):
		for event in events:
			keys = pygame.key.get_pressed()
			if keys[pygame.K_RIGHT]:
				self.is_idle = False
				self.status = "right"
				self.direction.x = 1
				
	def apply_scale(self):
		width, height = self.image.get_size()
		new_width = int(width * self.scale_factor)
		new_height = int(height * self.scale_factor)
		self.image = pygame.transform.scale(
			self.animation[int(self.frame_index)], (new_width, new_height)
		)
		self.rect = self.image.get_rect(center=self.rect.center)
		
	def update_frame(self, dt):

		if self.animation in [
			self.animations["jump"]
		]:

			if self.frame_index > len(self.animation) - 2:
				self.animation_done()
			else:
				self.speed = self.speed

		if self.frame_index >= len(self.animation):
			self.frame_index = 0
		self.image = self.animation[int(self.frame_index)]
		
	def update(self, dt, events, screen, selected_player):
		self.input(events, dt, screen)
		self.move(dt, screen)
		self.animate(dt)
		return 
					