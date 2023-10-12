# Programmer: 
# Description: 

# Import and initialize the pygame library
import pygame
from pygame.locals import *
from pygame_grid import draw_grid
pygame.init()

# Create and open a pygame screen with the given size
width = 640
height = 220

screen = pygame.display.set_mode((width, height))
screen.fill("lightgray")


# Set the title of the pygame screen
pygame.display.set_caption("My Game")

### PUT YOUR GAME CODE HERE

#Red Box
red_box = pygame.Rect(50, 20, 120, 100)
pygame.draw.rect(screen, "red", red_box)

second_red_box = pygame.Rect(350, 20, 120, 100)
pygame.draw.rect(screen, "red", second_red_box, 1)

#Green Box
green_box = pygame.Rect(100, 60, 120, 100)
pygame.draw.rect(screen, "green", green_box)

second_green_box = pygame.Rect(400, 60, 120, 100)
pygame.draw.rect(screen, "green", second_green_box, 4)

#Blue Box
blue_box = pygame.Rect(150, 100, 120, 100)
pygame.draw.rect(screen, "blue", blue_box)

second_blue_box = pygame.Rect(450, 100, 120, 100)
pygame.draw.rect(screen, "blue", second_blue_box, 8)

# Uncomment this line to show a grid
draw_grid()

# Flip the changes to the screen to the computer display
pygame.display.flip()
