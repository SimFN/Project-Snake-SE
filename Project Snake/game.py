import pygame
from classes import Snake, Fruits, GameStats
from konstanter import WIDTH, HEIGHT, TITLE_SIZE, FPS

class Game:
    def __init__(self):
        # Opret stats
        self.stats = GameStats()

        # Opret slangen midt på banen
        start_x = (WIDTH // TITLE_SIZE) // 2
        start_y = (HEIGHT // TITLE_SIZE) // 2
        self.snake = Snake((start_x, start_y))
        
        # Opret første frugt
        self.fruit = Fruits(self.snake.body)

        # Spillet skal køre
        self.running = True

    def reset(self):
        # For at genstarte spillet
        self.stats.reset()

        start_x = (WIDTH // TITLE_SIZE) // 2
        start_y = (HEIGHT // TITLE_SIZE) // 2
        self.snake = Snake((start_x, start_y))

        self.fruit = Fruits(self.snake.body)
        self.running = True

    def handle_input(self):
        # Direction kommer til at stamme fra main.py filen ved brug af pygame
        # og ser ud som fx (-1, 0), (0, 1) osv.
        self.snake.change_direction(direction)
    
    def update(self):
        # Opdaterer logik pr. frame
        
        # Tjek om slangen sluger frugt
        if self.snake.body[0] == self.fruit.position:
            self.stats.increase_score()
            self.snake.move(Grow=True)
            self.fruit = Fruits(self.snake.body)
        else:
            self.snake.move(Grow=False)

        # Tjek for kollisioner
        if self.snake.collides_with_self() or self.snake.collides_with_wall():
            self.stats.game_over = True
            self.running = False
