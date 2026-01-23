import pygame
from classes import Fruits
from konstanter import WIDTH, HEIGHT, TITLE_SIZE, FPS, BACKGROUND_COLOR, SNAKE_COLOR, FOOD_COLOR
from game import Game


#tegn slangen
def draw_snake(screen, snake):
    for (x, y) in snake.body:
        rect = pygame.Rect(x * TITLE_SIZE, y * TITLE_SIZE, TITLE_SIZE, TITLE_SIZE)
        pygame.draw.rect(screen, SNAKE_COLOR, rect)
#tegn frugten
def draw_fruit(screen, fruit):
    x, y = fruit.position
    rect = pygame.Rect(x * TITLE_SIZE, y * TITLE_SIZE, TITLE_SIZE, TITLE_SIZE)
    pygame.draw.rect(screen, FOOD_COLOR, rect)

def main():
#lav displayet    
    pygame.init()
    screen = pygame.display.set_mode(WIDTH,HEIGHT)

    clock = pygame.time.Clock()
    game = Game()

    while game.running:
        clock.tick(FPS)
#quit funktion    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
#kontrol til slangen for at få den til at bevæge sig        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.snake.change_direction((0,-1))
                elif event.key == pygame.K_DOWN:
                    game.snake.change_direction((0,1))
                elif event.key == pygame.K_LEFT:
                    game.snake.change_direction((-1,0))
                elif event.key == pygame.K_RIGHT:
                    game.snake.change_direction((1,0))

        if not game.stats.game_over:
            game.snake.move()

            if game.snake.body[0] == game.fruit.position:
                game.snake.move(Grow=True)
                game.stats.increase_score()
                game.fruit = Fruits(game.snake.body)

            if game.snake.collides_with_self() or game.snake.collides_with_wall():
                game.stats.game_over = True

        screen.fill(BACKGROUND_COLOR)
        draw_snake(screen, game.snake)
        draw_fruit(screen, game.fruit)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
