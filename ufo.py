import pygame

class Ufo:
    def __init__(self, bb_game):
        """Initialize the ufo and set its starting position."""
        self.screen = bb_game.screen
        self.screen_rect = bb_game.screen.get_rect()

        """Load the ufo image and set its rect attribute."""
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        """Start each new ufo near the center of the screen."""
        self.rect.center = self.screen_rect.center

    
    def blitme(self):
        """Draw the ufo at its current location."""
        self.screen.blit(self.image, self.rect)