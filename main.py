from cProfile import run
from turtle import screensize
from webbrowser import BackgroundBrowser
import pygame

background_colour = (234, 212, 252)
screen = pygame.display.set_mode((300, 300))

pygame.display.set_caption('Blyat')
screen.fill(background_colour)
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False