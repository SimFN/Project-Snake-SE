import pygame
from konstanter import WIDTH, HEIGHT, TITLE_SIZE, FPS, BACKGROUND_COLOR, SNAKE_COLOR, FOOD_COLOR
from game import Game

#
def draw_snake(screen, snake):
    for (x, y) in snake.body:
        rect = pygame.Rect(x * TITLE_SIZE, y * TITLE_SIZE, TITLE_SIZE, TITLE_SIZE)
        pygame.draw.rect(screen, SNAKE_COLOR, rect)

def draw_fruit(screen, fruit):
    x, y = fruit.position
    rect = pygame.Rect(x * TITLE_SIZE, y * TITLE_SIZE, TITLE_SIZE, TITLE_SIZE)
    pygame.draw.rect(screen, FOOD_COLOR, rect)

