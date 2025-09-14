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
		self.selected_player = "brunson"
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