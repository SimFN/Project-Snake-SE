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


def main():
    pygame.init()
    screen = pygame.display.set_mode(WIDTH,HEIGHT)

    clock = pygame.time.Clock()
    game = Game()

    while game.running:
        clock.tick(FPS)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.snake.change_direction((0,-1))
                elif event.key == pygame.K_DOWN:
                    game.snake.change_direction((0,1))
                elif event.key == pygame.K_LEFT:
                    game.snake.change_direction((-1,0))
                elif event.key == pygame.K_RIGHT:
                    game.snake.change_direction((1,0))
