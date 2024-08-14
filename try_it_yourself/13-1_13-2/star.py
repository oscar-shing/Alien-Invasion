import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single Star in the fleet."""

    def __init__(self, stars_game):
        """Initialize the Star and set its starting position."""
        super().__init__()
        self.screen = stars_game.screen

        # Load the Star image and set its rect attribute.
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        # Start each new Star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Note: Since the stars won't be moving, we don't need to track their exact position.