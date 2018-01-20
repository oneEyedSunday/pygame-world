"""
    This file is going to hold the Player class

"""
import pygame
import globals

class Player(pygame.sprite.Sprite):
    def __init__(self,cameraRect):
        super().__init__()

        # Attributes
        self.change_x = 30
        self.change_y = 15

        self.cameraRect = cameraRect
        self.currentImage = 1
        self.image = globals.PLAYERIMAGES[self.currentImage]
        self.rect = self.image.get_rect()
        self.rect.height = 50 # hard fix to enable more fluent movemnet


    def update(self):
        """ Move the player """
        pass

    def go_right(self, allsprites):
        # if your movemnet willl make you collide with someth
        # pass
        context = None
        if self.cameraRect.right - self.change_x - globals.TILEWIDTH <= globals.LEVEL[0] + globals.TILEWIDTH:
            for s in allsprites:
                s.rect.left -= self.change_x
            self.cameraRect.left += self.change_x
            context = "SPR-CMR+"
        else:
            if self.rect.right + self.change_x <= globals.WINWIDTH:
                self.rect.right += self.change_x
                context = "SLF+"

        landscape_hit_list = pygame.sprite.spritecollide(self, allsprites, False)
        if len(landscape_hit_list) > 0:
            # reverse movemnet
            if context is "SPR-CMR+":
                for s in allsprites:
                    s.rect.left += self.change_x
                self.cameraRect.left -= self.change_x

            elif context is "SLF+":
                self.rect.right -= self.change_x

    def go_left(self, allsprites):
        context = None
        if self.cameraRect.left - self.change_x >= 0:
            for s in allsprites:
                s.rect.left += self.change_x
            self.cameraRect.left -= self.change_x
            context = "SPR+CML-"
        else:
            if self.rect.left - self.change_x >= 0:
                self.rect.left -= self.change_x
                context = "SLF-"
        landscape_hit_list = pygame.sprite.spritecollide(self, allsprites, False)
        if len(landscape_hit_list) > 0:
            # reverse movmnet
            if context is "SPR+CML-":
                for s in allsprites:
                    s.rect.left -= self.change_x
                self.cameraRect.left += self.change_x

            elif context is "SLF-":
                self.rect.left += self.change_x

    def go_up(self, allsprites):
        if self.cameraRect.top - self.change_y >= 0:
            for s in allsprites:
                s.rect.top += self.change_y
            self.cameraRect.top -= self.change_y
        else:
            if self.rect.top - self.change_y >= 0:
                self.rect.top -= self.change_y

    def go_down(self, allsprites):
        if self.cameraRect.bottom + self.change_y <= globals.LEVEL[1]:
            for s in allsprites:
                s.rect.bottom -= self.change_y
            self.cameraRect.bottom += self.change_y
        else:
            if self.rect.bottom <= globals.WINHEIGHT:
                self.rect.bottom += self.change_y

    def change_avatar(self):
        if self.currentImage + 1 >= len(globals.PLAYERIMAGES):
            self.currentImage = 0

        else:
            self.currentImage += 1

        self.image = globals.PLAYERIMAGES[self.currentImage]


    def draw(self, screen):
        screen.blit(self.image, self.rect)