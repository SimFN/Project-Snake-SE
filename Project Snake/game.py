from classes import Snake, Fruits, GameStats
from konstanter import WIDTH, HEIGHT, TITLE_SIZE

class Game:
    def __init__(self):
        self.stats = GameStats()
        self.state = "START"   # START, PLAYING
        self.running = True

        self.snake = None
        self.fruit = None

    def start_game(self):
        # Starter (eller genstarter) spillet
        self.stats.reset()

        start_x = (WIDTH // TITLE_SIZE) // 2
        start_y = (HEIGHT // TITLE_SIZE) // 2
        self.snake = Snake((start_x, start_y))
        self.fruit = Fruits(self.snake.body)

        self.state = "PLAYING"

    def go_to_start(self):
        # Sender spilleren tilbage til startskærmen
        self.state = "START"

    def update(self):
        if self.state != "PLAYING":
            return

        # Slangen spiser frugt
        if self.snake.body[0] == self.fruit.position:
            self.stats.increase_score()
            self.snake.move(Grow=True)
            self.fruit = Fruits(self.snake.body)
        else:
            self.snake.move(Grow=False)

        # Kollision
        if self.snake.collides_with_self() or self.snake.collides_with_wall():
            self.go_to_start()
