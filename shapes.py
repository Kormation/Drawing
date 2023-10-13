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
pygame.draw.circle(screen, "green", (300, 50), 20)

#Ellipse
ellipse = pygame.Rect(300, 250, 40, 80)
pygame.draw.ellipse(screen, "black", ellipse, 1)

#Rectangle
rectangle = pygame.Rect(150, 300, 100, 50)
pygame.draw.rect(screen, "black", rectangle)

#Line

# Uncomment this line to show a grid
draw_grid()

# Flip the changes to the screen to the computer display
pygame.display.flip()
