"""
    This file will hold the global variables

"""
import pygame

FPS = 30 # frames per second to update the screen
WINWIDTH = 800 # width of the program's window, in pixels
WINHEIGHT = 600 # height in pixels
HALFWINWIDTH = int(WINWIDTH / 2)
HALFWINHEIGHT = int(WINHEIGHT / 2)

# The total width and height of each tile in pixels.
TILEWIDTH = 50
TILEHEIGHT = 85
TILEFLOORHEIGHT = 40
LEVEL = [1500, 1200]

CAM_MOVE_SPEED = 5 # how many pixels per frame the camera moves

# The percentage of outdoor tiles that have additional
# decoration on them, such as a tree or rock.
OUTSIDE_DECORATION_PCT = 20


UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


IMAGESDICT = {
        'princess': pygame.image.load('sprites/princess.png'),
        'boy': pygame.image.load('sprites/boy.png'),
        'catgirl': pygame.image.load('sprites/catgirl.png'),
        'horngirl': pygame.image.load('sprites/horngirl.png'),
        'pinkgirl': pygame.image.load('sprites/pinkgirl.png'),
        'title': pygame.image.load('sprites/star_title.png'),
        'corner': pygame.image.load('sprites/Wall_Block_Tall.png'),
        'wall': pygame.image.load('sprites/Wood_Block_Tall.png'),
        'inside floor': pygame.image.load('sprites/Plain_Block.png'),
        'outside floor': pygame.image.load('sprites/Grass_Block.png'),
        'rock': pygame.image.load('sprites/Rock.png'),
        'short tree': pygame.image.load('sprites/Tree_Short.png'),
        'tall tree': pygame.image.load('sprites/Tree_Tall.png'),
        'ugly tree': pygame.image.load('sprites/Tree_Ugly.png')
    }

PLAYERIMAGES = [
        IMAGESDICT['princess'],
        IMAGESDICT['boy'],
        IMAGESDICT['catgirl'],
        IMAGESDICT['horngirl'],
        IMAGESDICT['pinkgirl']
    ]