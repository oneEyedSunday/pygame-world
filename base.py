"""
Pygame base template for opening a window, done with functions

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""

import pygame, sys
from pygame.locals import *
from player import Player
from landscape import Landscape
import globals
# The use of the main function is described in Chapter 9.

# move this to colors file
# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BRIGHTBLUE = (  0, 170, 255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE
# The total width and height of each tile in pixels.



def main():
    global DISPLAYSURF, BASICFONT, FPSCLOCK, player, camera, allLandscapeList, allSpriteList
    """ Main function for the game. """
    pygame.init()

    # Set the width and height of the screen [width,height]
    size = [globals.WINWIDTH, globals.WINHEIGHT]
    DISPLAYSURF = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game - Finally")
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    # Used to manage how fast the screen updates
    FPSCLOCK = pygame.time.Clock()
    # A global dict value that will contain all the Pygame
    # Surface objects returned by pygame.image.load().



    # cameraRect starts at point where edge is acvounted
    # leftest edge of screen is -150, so add to cameraRect
    cameraRect = pygame.Rect([150, 0, globals.WINWIDTH, globals.WINHEIGHT])
    player = Player(cameraRect) # create player object
    player.rect.top = globals.HALFWINHEIGHT
    player.rect.left = globals.HALFWINWIDTH
    startScreen()
    # Loop until the user clicks the close button.
    done = False
    allLandscapeList = pygame.sprite.Group()
    allSpriteList = pygame.sprite.Group() # incl players and enemies etc
    getLandscape()
    getInitialObstacles()  # push to Game class
    allSpriteList.add(player)




    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_d:
                    player.go_right(allLandscapeList)
                    # print("%d - %d" % (player.rect.left, cameraRect.right))

                if event.key == K_a:
                    player.go_left(allLandscapeList)
                    # print("%d - %d" % (player.rect.left, cameraRect.left))

                if event.key == K_w:
                    player.go_up(allLandscapeList)
                if event.key == K_s:
                    player.go_down(allLandscapeList)
                if event.key == K_p:
                    player.change_avatar()
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.fill(BGCOLOR)
        # use draw instead for landscape
        for b in allSpriteList:
            b.draw(DISPLAYSURF)
        # draw player
        # DISPLAYSURF.blit(player.image, player.rect)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 60 frames per second
        FPSCLOCK.tick(60)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()


def startScreen():
    """Display the start screen (which has the title and instructions)
    until the player presses a key. Returns None."""

    # Position the title image.
    titleRect = globals.IMAGESDICT['title'].get_rect()
    topCoord = 50 # topCoord tracks where to position the top of the text
    titleRect.top = topCoord
    titleRect.centerx = globals.HALFWINWIDTH
    topCoord += titleRect.height

    # Unfortunately, Pygame's font & text system only shows one line at
    # a time, so we can't use strings with \n newline characters in them.
    # So we will use a list with each line in it.
    instructionText = ['Push the stars over the marks.',
                       'Arrow keys to move, WASD for camera control, P to change character.',
                       'Backspace to reset level, Esc to quit.',
                       'N for next level, B to go back a level.']

    # Start with drawing a blank color to the entire window:
    DISPLAYSURF.fill(BGCOLOR)

    # Draw the title image to the window:
    DISPLAYSURF.blit(globals.IMAGESDICT['title'], titleRect)

    # Position and draw the text.
    for i in range(len(instructionText)):
        instSurf = BASICFONT.render(instructionText[i], 1, TEXTCOLOR)
        instRect = instSurf.get_rect()
        topCoord += 10 # 10 pixels will go in between each line of text.
        instRect.top = topCoord
        instRect.centerx = globals.HALFWINWIDTH
        topCoord += instRect.height # Adjust for the height of the line.
        DISPLAYSURF.blit(instSurf, instRect)

    while True: # Main loop for the start screen.
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return # user has pressed a key, so return.

        # Display the DISPLAYSURF contents to the actual screen.
        pygame.display.update()
        FPSCLOCK.tick()


def getInitialObstacles():
    """ gets the position of the initial blocks """
    # hardcode number of blocks
    # will account for movemnet
    from random import choice
    from globals import TILEWIDTH, TILEHEIGHT, WINHEIGHT, TILEFLOORHEIGHT, LEVEL, HALFWINWIDTH

    no_of_blocks = 50
    for b in range(no_of_blocks // 2):
        # get image
        # image = globals.IMAGESDICT['rock']
        for y in range(1,5):
            image = globals.IMAGESDICT[choice(['ugly tree', 'rock', 'tall tree'])]
            # make rect
            spaceRect = pygame.Rect((b * TILEWIDTH, y * TILEFLOORHEIGHT, TILEWIDTH, TILEFLOORHEIGHT))
            landscape = Landscape(image, spaceRect)
            allLandscapeList.add(landscape)
            allSpriteList.add(landscape)

    image = globals.IMAGESDICT['corner']
    negativeRect = pygame.Rect([-150, WINHEIGHT - TILEHEIGHT, TILEWIDTH, TILEHEIGHT])
    landscape = Landscape(image, negativeRect)
    allLandscapeList.add(landscape)
    allSpriteList.add(landscape)

    image = globals.IMAGESDICT['corner']
    positiveRect = pygame.Rect([LEVEL[0] - TILEWIDTH, WINHEIGHT - TILEHEIGHT, TILEWIDTH, TILEFLOORHEIGHT])
    landscape = Landscape(image, positiveRect)
    allLandscapeList.add(landscape)
    allSpriteList.add(landscape)

    bottomRect = pygame.Rect([HALFWINWIDTH, LEVEL[1] - TILEHEIGHT, TILEWIDTH, TILEFLOORHEIGHT])
    landscape = Landscape(image, bottomRect)
    allLandscapeList.add(landscape)
    allSpriteList.add(landscape)

    for x in range(0, LEVEL[0], 50):
        for y in range(10):
            image = globals.IMAGESDICT[choice(['ugly tree', 'rock', 'tall tree'])]
            spaceRect = pygame.Rect((x, LEVEL[1] - (y * TILEHEIGHT), TILEWIDTH, TILEFLOORHEIGHT))
            landscape = Landscape(image, spaceRect)
            if choice([0,1,0]):
                allLandscapeList.add(landscape)
                allSpriteList.add(landscape)


    return

def getLandscape():
    # itesm representing end of the world at both edges
    image = globals.IMAGESDICT['corner']
    negativeRect = pygame.Rect([-150, globals.WINHEIGHT - globals.TILEHEIGHT, globals.TILEWIDTH, globals.TILEHEIGHT])
    landscape = Landscape(image, negativeRect)
    allLandscapeList.add(landscape)
    allSpriteList.add(landscape)

    image = globals.IMAGESDICT['corner']
    positiveRect = pygame.Rect([globals.LEVEL[0] - globals.TILEWIDTH, globals.WINHEIGHT - globals.TILEHEIGHT, globals.TILEWIDTH, globals.TILEHEIGHT])
    landscape = Landscape(image, positiveRect)
    allLandscapeList.add(landscape)
    allSpriteList.add(landscape)
    return

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
