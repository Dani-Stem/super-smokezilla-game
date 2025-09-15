import pygame
import time
from menu import start_menu, render_start_menu
from game_loop import game_loop
from all_sprites import AllSprites

class Game:
	def __init__(self):
		pygame.init()
		pygame.mixer.init()
		self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 620, 900
		self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
		pygame.display.set_caption("SUPER SMOKEZILLA")
		self.clock = pygame.time.Clock()
		
		# varaibles 
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

		# groups
		self.all_sprites_group = AllSprites()


		self.load_animation()

	def load_animation(self):
		num_frames = 6
		self.idle_anim = {}
		self.idle_anim['frame_index'] = 0
		self.idle_anim['frames'] = []
		self.idle_anim['num_frames'] = num_frames
		for i in range(num_frames):
			self.idle_anim['frames'].append(pygame.image.load("images/idle_clothed/" + str(i) + ".png").convert_alpha())

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
