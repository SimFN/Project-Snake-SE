import random
from konstanter import WIDTH, HEIGHT, TITLE_SIZE

class Snake:
    def __init__(self, start_pos):
        # Startposition
        self.body = [start_pos]
        self.direction = (1, 0)  # Bevæger sig til højre når spillet starter

    def change_direction(self, new_direction):
        # For at undgå at vende 180 grader
        if (new_direction[0] == -self.direction[0] and new_direction[1] == -self.direction[1]):
            return
        self.direction = new_direction

    def move(self, Grow=False):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        # Nyt hoved tilføjes
        self.body.insert(0, new_head)
        # Hvis slangen ikke skal vokse, fjernes halen
        if not Grow:
            self.body.pop()

    def collides_with_self(self):
        # Definer hvornår slangen rammer sig selv
        return self.body[0] in self.body[1:]
    
    def collides_with_wall(self):
        # Definer hvornår slangen rammer en væg
        head_x, head_y = self.body[0]
        cols = WIDTH // TITLE_SIZE
        rows = HEIGHT // TITLE_SIZE

        # Tjek om hovedet er uden for banen
        return not (0 <= head_x < cols and 0 <= head_y < rows)
    

class Fruits:
    def __init__(self, snake_body):
        self.position = self.spawn(snake_body)

    def spawn(self, snake_body):
        # Definer hvordan frugter spawner
        cols = WIDTH // TITLE_SIZE
        rows = HEIGHT // TITLE_SIZE

        while True:
            pos = (
                random.randint(0, cols - 1),
                random.randint(0, rows - 1)
            )
            if pos not in snake_body:
                return pos
            
class GameStats:
    def __init__(self):
        self.score = 0
        self.highscore = 0
        self.game_over = False

    def reset(self):
        # Ændrer variable tilbage ved genstart
        self.score = 0
        self.game_over = False

    def increase_score(self):
        # Definer at score kan stige
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
