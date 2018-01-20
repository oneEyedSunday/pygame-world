"""
    This file is going to hold the Player class

"""
import pygame
import globals

class Player(pygame.sprite.Sprite):
    def __init__(self,cameraRect):
        super().__init__()

        # Attributes
        self.change_x = 0
        self.change_y = 0

        self.cameraRect = cameraRect
        self.currentImage = 1
        self.image = globals.PLAYERIMAGES[self.currentImage]
        self.rect = self.image.get_rect()




    def update(self):
        """ Move the player """
        pass

    def go_right(self, allsprites):
        if self.cameraRect.right - 30 - globals.TILEWIDTH <= globals.LEVEL[0] + globals.TILEWIDTH:
            for s in allsprites:
                s[1].left -= 30
            self.cameraRect.left += 30
        else:
            if self.rect.right + 30 <= globals.WINWIDTH:
                self.rect.right += 30

    def go_left(self, allsprites):
        if self.cameraRect.left - 30 >= 0:
            for s in allsprites:
                s[1].left += 30
            self.cameraRect.left -= 30
        else:
            if self.rect.left - 30 >= 0:
                self.rect.left -= 30

    def go_up(self, allsprites):
        if self.cameraRect.top - 30 >= 0:
            for s in allsprites:
                s[1].top += 30
            self.cameraRect.top -= 30
        else:
            if self.rect.top - 30 >= 0:
                self.rect.top -= 30

    def go_down(self, allsprites):
        if self.cameraRect.bottom + 30 <= globals.LEVEL[1]:
            for s in allsprites:
                s[1].bottom -= 30
            self.cameraRect.bottom += 30
        else:
            if self.rect.bottom <= globals.WINHEIGHT:
                self.rect.bottom += 30

    def change_avatar(self):
        if self.currentImage + 1 >= len(globals.PLAYERIMAGES):
            self.currentImage = 0

        else:
            self.currentImage += 1

        self.image = globals.PLAYERIMAGES[self.currentImage]