import pygame, sys
import time

def render_start_menu(self, dt):
    self.screen.fill(self.WHITE)
    start_font = pygame.font.Font("font.ttf", 50)
    select_font = pygame.font.Font("font.ttf", 40)

    score_surface0 = start_font.render("SUPER", True, "BLACK")
    score_rect = score_surface0.get_rect()
    score_rect.midtop = (self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT / 20)

    score_surface1 = start_font.render("SMOKEZILLA GAME", True, "BLACK")
    score_rect1 = score_surface1.get_rect()
    score_rect1.midtop = (self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT / 10)

    self.screen.blit(score_surface0, score_rect)
    self.screen.blit(score_surface1, score_rect1)

    for index, item in enumerate(self.menu_items):
        if index == self.start_selected_index:
            text_color = self.HIGHLIGHT
            if self.menu_items[self.start_selected_index] == "START GAME":
                text_color = "GREEN"
            elif self.menu_items[self.start_selected_index] == "HOW TO PLAY":
                text_color = "GREEN"
        else:
            text_color = self.BLACK

        menu_text = select_font.render(item, True, text_color)

        text_rect = menu_text.get_rect(
            center=(
                self.WINDOW_WIDTH / 1.43
                + (index - len(self.menu_items) // 2) * 250,
                self.WINDOW_HEIGHT // 1.35,
            )
        )
        self.screen.blit(menu_text, text_rect)
        self.smokezilla_avi(dt)


def start_menu(self):
    running = True

    # Disable spacebar for a few seconds when the menu is rendered
    self.spacebar_enabled = False
    pygame.time.set_timer(pygame.USEREVENT, 100)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT:
                self.spacebar_enabled = True
                pygame.time.set_timer(pygame.USEREVENT, 0)  # Stop the timer

            if event.type == pygame.KEYDOWN:
                if not self.spacebar_enabled and event.key == pygame.K_SPACE:
                    continue  # Ignore spacebar presses if disabled

                self.highlight_sound.play()
                if event.key == pygame.K_LEFT:
                    self.highlight_sound.play()
                    self.start_selected_index = (self.start_selected_index - 1) % len(
                        self.menu_items
                    )
                elif event.key == pygame.K_RIGHT:
                    self.highlight_sound.play()
                    self.start_selected_index = (self.start_selected_index + 1) % len(
                        self.menu_items
                    )
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
        
                    # self.confirm_sound.play()
                    self.game_loop()
                    # self.confirm_sound.play()            
        
        dt = self.clock.tick(60) / 1000

        self.render_start_menu(dt)
        pygame.display.flip()
