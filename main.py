import pygame
import time
from menu import start_menu, render_start_menu

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

	def smokezilla_avi(self):
		img_smokezilla_avi = pygame.image.load("images/idle/0.png").convert_alpha()
		self.screen.blit(
			img_smokezilla_avi,
			pygame.Rect(190, 225, 20, 20),
		)
    
	def start_menu(self):
		start_menu(self)
		
	def render_start_menu(self):
		render_start_menu(self)
		    
	def run(self):
		self.start_menu()
		
if __name__ == "__main__":
	game = Game()
	game.run()
