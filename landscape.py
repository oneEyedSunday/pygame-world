"""
    This file holds the definition of the Landscape class
    representing visual elements in the game
    that aren't the player or enemies - if indeed we end up having enemies in game

"""

import pygame
import globals

class Landscape(pygame.sprite.Sprite):
    def __init__(self, image, rect):
        super().__init__()
        self.image = image
        self.rect = rect

    def draw(self, screen):
        screen.blit(self.image, self.rect)