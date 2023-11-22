
# LIBRARIES
import pygame
import os
import sys
# CUSTOM LIBRARIES
from settings import *
from player import Player
from overlay import Overlay

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # Play game in fullscreen
pygame.display.set_caption("Universe Unveiled") # Set Window Title
running = True

# Create a player object
player = Player(WIDTH // 2 - 25, HEIGHT // 2 - 25, 50, 50, 5)

# Create an overlay object
overlay = Overlay(WIDTH, 100, 100)  # Adjust height as needed

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quit game if X is pressed
            running = False
    
    keys = pygame.key.get_pressed()
    player.move(keys, WIDTH, HEIGHT)

    # Update

    # Draw (pay attention to draw order)
    screen.fill(BLACK)  # Fill the screen with white for now
    player.draw(screen)
    overlay.draw(screen)
    
    # Refresh the display
    pygame.display.flip()   # Update display every frame
    
    # Control frame rate
    pygame.time.Clock().tick(FPS)   # Delta time

pygame.quit()
sys.exit()      # Terminate process