import pygame
import time
import random
from menu import start_menu, render_start_menu
from game_loop import game_loop
from all_sprites import AllSprites
from player import Player
from shirt import Shirt
from hat import Hat

class Game:
	def __init__(self):
		pygame.init()
		pygame.mixer.init()
		self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 620, 900
		self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
		pygame.display.set_caption("SUPER SMOKEZILLA")
		self.clock = pygame.time.Clock()
		
		# varaibles 
		self.love = True
		self.start_selected_index = 0
		self.menu_items = ["START GAME", "HOW TO PLAY"]
		
		# Colors
		self.WHITE = (255, 255, 255)
		self.BLACK = (40, 40, 40)
		self.HIGHLIGHT = "green"
		self.start = True

		# fonts
		self.font = pygame.font.Font("font.ttf", 74)
		
        # sounds
		self.start_music = pygame.mixer.Sound("sounds/start.ogg")
		self.start_music.set_volume(0.2)
		self.highlight_sound = pygame.mixer.Sound("sounds/highlight.ogg")
		self.highlight_sound.set_volume(0.05)
		
        # channels
		if not hasattr(self, "start_channel"):
			self.start_channel = pygame.mixer.Channel(0)

		self.center = pygame.math.Vector2(self.WINDOW_WIDTH/2, self.WINDOW_HEIGHT/2+200)
		self.player = Player(self.center)

		self.shirt = Shirt(pygame.math.Vector2(self.WINDOW_WIDTH/2+350, self.WINDOW_HEIGHT/2+100))

		self.hat = Hat(pygame.math.Vector2(self.WINDOW_WIDTH/2+900, self.WINDOW_HEIGHT/2+100))

		self.load_animation()
		self.load_background()
		self.load_clouds()

	def load_animation(self):
		num_frames = 6
		self.idle_anim = {}
		self.idle_anim['frame_index'] = 0
		self.idle_anim['frames'] = []
		self.idle_anim['num_frames'] = num_frames
		for i in range(num_frames):
			self.idle_anim['frames'].append(pygame.image.load("images/idle_clothed/" + str(i) + ".png").convert_alpha())

	def load_background(self):
		self.bg = {}
		scale_factor = .5
		img = pygame.image.load("images/bg.jpg").convert_alpha()
		size = img.get_size()
		scaled = pygame.transform.scale(img, (size[0]*scale_factor, size[0]*scale_factor))
		self.bg['image'] = scaled
		self.bg['x_pos'] = 0

	def load_clouds(self):
		self.show_clouds = True
		self.clouds = []
		imgs = []
		imgs.append(pygame.image.load("images/cloud.png").convert_alpha())
		#imgs.append(pygame.image.load("images/cloud2.png").convert_alpha())
		for i in range(50):
			scale_factor = random.random()*0.8 + 0.2
			img = random.choice(imgs)
			size = img.get_size()
			scaled = pygame.transform.scale(img, (size[0]*scale_factor, size[1]*scale_factor))
			x = random.randint(-1000,15000)
			mid = int(self.WINDOW_HEIGHT/2)
			y = random.randint(mid - mid + 200, mid - 100)
			pos = pygame.math.Vector2(x, y)
			self.clouds.append({'image':scaled, 'pos':pos,
				'floaty':random.randint(0,10000),
				'speed':random.randint(5,20),
				'parallax':scale_factor*0.5
			})

		self.clouds.sort(key=lambda cloud: cloud['parallax'])
		

	def smokezilla_avi(self, dt):
		index = self.idle_anim['frame_index']
		img = self.idle_anim['frames'][int(index)]
		self.screen.blit(img, pygame.Rect(160, 285, 20, 20))

		self.idle_anim['frame_index'] += 8 * dt
		self.idle_anim['frame_index'] %= self.idle_anim['num_frames']
    
	def start_menu(self):
		start_menu(self)
		
	def render_start_menu(self, dt):
		render_start_menu(self, dt)
		
	def game_loop(self):
		game_loop(self)
		    
	def run(self):
		self.start_menu()
		
if __name__ == "__main__":
	game = Game()
	game.run()
