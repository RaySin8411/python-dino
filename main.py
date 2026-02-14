import pygame 
import os 
import random 

pygame.init() 

screen_height = 600 
screen_width = 1100 

screen = pygame.display.set_mode((screen_width, screen_height))

RUNNING = [ 
	pygame.image.load(os.path.join("assets/Dino", "Chrome Dino Run.png")), 
	pygame.image.load(os.path.join("assets/Dino", "Chrome Dino Run 2.png")) 
] 
JUMPING = pygame.image.load(os.path.join("assets/Dino", "Dino Jump.png")) 
DUCKING = [ 
	pygame.image.load(os.path.join("assets/Dino", "Dino Duck.png")), 
	pygame.image.load(os.path.join("assets/Dino", "Dino Duck 2.png")) 
]