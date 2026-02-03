import pygame
from konstanter import *
from game import Game


# tegn slangen
def draw_snake(screen, snake):
    for (x, y) in snake.body:
        rect = pygame.Rect(x * TITLE_SIZE, y * TITLE_SIZE, TITLE_SIZE, TITLE_SIZE)
        pygame.draw.rect(screen, SNAKE_COLOR, rect)


# tegn frugten
def draw_fruit(screen, fruit):
    x, y = fruit.position
    rect = pygame.Rect(x * TITLE_SIZE, y * TITLE_SIZE, TITLE_SIZE, TITLE_SIZE)
    pygame.draw.rect(screen, FOOD_COLOR, rect)


# tegn grid som slangen bevæger sig i
def draw_grid(screen):
    cols = WIDTH // TITLE_SIZE
    rows = HEIGHT // TITLE_SIZE

    for y in range(rows):
        for x in range(cols):
            # skift farve baseret på om x+y er lige eller ulige
            if (x + y) % 2 == 0:
                color = DARK_GRAY
            else:
                color = LIGHT_GRAY

            rect = pygame.Rect(x * TITLE_SIZE, y * TITLE_SIZE, TITLE_SIZE, TITLE_SIZE)
            pygame.draw.rect(screen, color, rect)


# tegn start skærm
def draw_start_screen(screen):
    screen.fill(BLACK)

    font = pygame.font.SysFont(None, 60)
    small_font = pygame.font.SysFont(None, 36)

    title = font.render("SNAKE", True, GREEN)
    text = small_font.render("Tryk SPACE for at starte", True, WHITE)

    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))


def main():
    # lav displayet
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")

    clock = pygame.time.Clock()
    game = Game()

    while game.running:
        clock.tick(SPEED)

        # quit funktion
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

            # input til spillet
            if event.type == pygame.KEYDOWN:

                # start spillet fra startskærmen
                if game.state == "START":
                    if event.key == pygame.K_SPACE:
                        game.start_game()

                # kontrol til slangen
                elif game.state == "PLAYING":
                    if event.key == pygame.K_UP:
                        game.snake.change_direction((0, -1))
                    elif event.key == pygame.K_DOWN:
                        game.snake.change_direction((0, 1))
                    elif event.key == pygame.K_LEFT:
                        game.snake.change_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        game.snake.change_direction((1, 0))

        # opdater og tegn afhængigt af spillets tilstand
        if game.state == "START":
            draw_start_screen(screen)

        elif game.state == "PLAYING":
            game.update()
            draw_grid(screen)
            draw_snake(screen, game.snake)
            draw_fruit(screen, game.fruit)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
