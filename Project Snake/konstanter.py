import pygame
import time

WIDTH = 800
HEIGHT = 600
TITLE_SIZE = 20
FPS = 30

# Farver
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


score = 0
game_window = pygame.display.set_mode((WIDTH,HEIGHT))

fps = pygame.time.Clock()

def show_score(choice, color, font, size):
    
    score_font = pygame.font.SysFont(font, size)

    score_surface = score_font.render('Score : ' + str(score), True, GREEN)

    
