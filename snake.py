import pygame
import random

# Initialize pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define Snake class
class Snake:
    def __init__(self):
        self.body = [(WIDTH / 2, HEIGHT / 2)]
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])

    def move(self):
        x, y = self.body[0]
        if self.direction == 'UP':
            y -= CELL_SIZE
        elif self.direction == 'DOWN':
            y += CELL_SIZE
        elif self.direction == 'LEFT':
            x -= CELL_SIZE
        elif self.direction == 'RIGHT':
            x += CELL_SIZE
        self.body.insert(0, (x, y))

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

# Define Food class
class Food:
    def __init__(self):
        self.x = random.randrange(0, WIDTH, CELL_SIZE)
        self.y = random.randrange(0, HEIGHT, CELL_SIZE)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, CELL_SIZE, CELL_SIZE))

# Initialize Snake and Food
snake = Snake()
food = Food()

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != 'DOWN':
                snake.direction = 'UP'
            elif event.key == pygame.K_DOWN and snake.direction != 'UP':
                snake.direction = 'DOWN'
            elif event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                snake.direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                snake.direction = 'RIGHT'

    snake.move()

    if snake.body[0][0] == food.x and snake.body[0][1] == food.y:
        snake.grow()
        food = Food()

    snake.draw()
    food.draw()

    pygame.display.update()
    clock.tick(10)

pygame.quit()
