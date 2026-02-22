import pygame
from konstanter import *
from game import Game

#tegner slangen felt for felt baseret på koordinater
def draw_snake(screen, snake):
    for (x, y) in snake.body:
        rect = pygame.Rect(x * TITLE_SIZE, y * TITLE_SIZE, TITLE_SIZE, TITLE_SIZE)
        pygame.draw.rect(screen, SNAKE_COLOR, rect)

#tegner frugten på dens givne position
def draw_fruit(screen, fruit):
    x, y = fruit.position
    rect = pygame.Rect(x * TITLE_SIZE, y * TITLE_SIZE, TITLE_SIZE, TITLE_SIZE)
    pygame.draw.rect(screen, FOOD_COLOR, rect)

#tegner gridded så man kan se hvordan slangen bevæger sig
def draw_grid(screen):
    cols = WIDTH // TITLE_SIZE
    rows = HEIGHT // TITLE_SIZE

#sørger for at ternene har forskellige farver
    for y in range(rows):
        for x in range(cols):
            if (x + y) % 2 == 0:
                color = DARK_GRAY
            else:
                color = LIGHT_GRAY

            rect = pygame.Rect(x * TITLE_SIZE, y * TITLE_SIZE, TITLE_SIZE, TITLE_SIZE)
            pygame.draw.rect(screen, color, rect)

#tegner startskærmen med titel, instruktion til at starte og highscore
def draw_start_screen(screen, stats):
    screen.fill(BLACK)

    font = pygame.font.SysFont(None, 60)
    small_font = pygame.font.SysFont(None, 36)

    title = font.render("SNAKE", True, GREEN)
    text = small_font.render("Tryk SPACE for at starte", True, WHITE)
    highscore = small_font.render(f"HIGHSCORE: {stats.highscore}", True, WHITE)

#placerer teksten på skærmen ordentligt
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
    screen.blit(highscore, (WIDTH // 2 - highscore.get_width() // 2, HEIGHT // 2 + 50))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")

    clock = pygame.time.Clock()
    game = Game()

#styrer hastigheden af spillet
    while game.running:
        clock.tick(SPEED)

#håndterer events (inputs)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

            if event.type == pygame.KEYDOWN:
                if game.state == "START":
                    if event.key == pygame.K_SPACE:
                        game.start_game()

#styring af slangen
                elif game.state == "PLAYING":
                    if event.key == pygame.K_UP:
                        game.snake.change_direction((0, -1))
                    elif event.key == pygame.K_DOWN:
                        game.snake.change_direction((0, 1))
                    elif event.key == pygame.K_LEFT:
                        game.snake.change_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        game.snake.change_direction((1, 0))

#tegner startskærmen
        if game.state == "START":
            draw_start_screen(screen, game.stats)

#tegner selve spillet
        elif game.state == "PLAYING":
            game.update()
            screen.fill(BACKGROUND_COLOR)
            draw_grid(screen)
            draw_snake(screen, game.snake)
            draw_fruit(screen, game.fruit)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
