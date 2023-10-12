# Programmer: 
# Description: 

# Import and initialize the pygame library
import pygame
from pygame.locals import *
from pygame_grid import draw_grid
pygame.init()

# Create and open a pygame screen with the given size
width = 400
height = 400

screen = pygame.display.set_mode((width, height))
screen.fill("lightgray")

# Set the title of the pygame screen
pygame.display.set_caption("My Game")

### PUT YOUR GAME CODE HERE

#Polygon
point_list = [(145, 0), (290, 105), (235, 275), (55, 275), (0, 105), (145, 0)]
pygame.draw.polygon(screen, "darkblue", point_list)

#Circle
pygame.draw.circle(screen, "green" (300, 30), 20)

# Uncomment this line to show a grid
draw_grid()

# Flip the changes to the screen to the computer display
pygame.display.flip()
