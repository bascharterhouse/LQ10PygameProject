# This is very basic code to create a pyGame window and paint the screen Red. 
# Please use comments to ensure your code is easy to read 

import pygame

pygame.init()
width, height = 800,  600
backgroundColor = 255,  0,  0

screen = pygame.display.set_mode((width, height))

while True:
	screen.fill(backgroundColor)
	pygame.display.flip()