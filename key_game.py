import sys

import pygame

from settings import Settings

class KeyGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Print Key Press (Press 'q' to quit)")

    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        # Show the pressed key on the screen, but quit if q is pressed
        # For more information about the output, see here:
        # https://www.pygame.org/docs/ref/key.html
        keys = pygame.key.get_pressed()
        key_name = pygame.key.name(event.key)
        print(key_name)
        if event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

    
if __name__ == '__main__':
    # Make a game instance, and run the game.
    kg = KeyGame()
    kg.run_game()