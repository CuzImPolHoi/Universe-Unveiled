
# LIBRARIES
import pygame

class Overlay:
    def __init__(self, width, height, alpha):
        
        # general Variables
        self.width = width
        self.height = height
        self.alpha = alpha  # Transparency level
        self.color = (20, 20, 20, self.alpha)  # Add alpha value to the color tuple

    def draw(self, screen):
        overlay_surface = pygame.Surface((screen.get_width(), self.height), pygame.SRCALPHA)
        overlay_surface.fill(self.color)
        screen.blit(overlay_surface, (0, screen.get_height() - self.height))