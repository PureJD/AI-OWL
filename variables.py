import pygame 
from functions import *
from GPTAPI import *

#owl image
owl_sprite = pygame.image.load("images/owl.png")


# for screen size and adjustment of objects on screen 
WIDTH, HEIGHT = 1000, 800

stars = generate_stars(100, WIDTH, HEIGHT)


# Initialize text input variables
question = ""
response = open_ai_chat(question)
