import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
SNAKE_COLOR = (128, 128, 0)  # Olive color
FOOD_COLOR = (255, 0, 0)
SNAKE_SPEED = 1
INITIAL_SNAKE_LENGTH = 3

SKY_BLUE = (135, 206, 235)
WHITE = (255, 255, 255)
LIGHT_GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (1, 0)
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
score = 0

game_over = False

def draw_snake(snake):
    for i, segment in enumerate(snake):
        if i == 0:
            pygame.draw.rect(screen, SNAKE_COLOR, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            pygame.draw.circle(screen, YELLOW, (segment[0] * GRID_SIZE + GRID_SIZE // 4, segment[1] * GRID_SIZE + GRID_SIZE // 3), 5)
            pygame.draw.circle(screen, YELLOW, (segment[0] * GRID_SIZE + 3 * GRID_SIZE // 4, segment[1] * GRID_SIZE + GRID_SIZE // 3), 5)
            pygame.draw.circle(screen, BLACK, (segment[0] * GRID_SIZE + GRID_SIZE // 2, segment[1] * GRID_SIZE + GRID_SIZE // 2), GRID_SIZE // 4)
        else:
            pygame.draw.rect(screen, SNAKE_COLOR, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, FOOD_COLOR, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def check_collision(snake):
    if (
            snake[0][0] < 0
            or snake[0][0] >= GRID_WIDTH
            or snake[0][1] < 0
            or snake[0][1] >= GRID_HEIGHT
            or snake[0] in snake[1:]
    ):
        return True
    return False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

    if check_collision(snake):
        game_over = True

    screen.fill(SKY_BLUE)

    pygame.draw.circle(screen, YELLOW, (100, 100), 50)

    pygame.draw.circle(screen, WHITE, (200, 100), 30)
    pygame.draw.circle(screen, WHITE, (250, 120), 40)
    pygame.draw.circle(screen, WHITE, (300, 100), 30)

    pygame.draw.rect(screen, LIGHT_GREEN, (0, 550, SCREEN_WIDTH, 50))

    draw_snake(snake)
    draw_food(food)

    pygame.display.update()

    pygame.time.delay(200 // SNAKE_SPEED)

font = pygame.font.Font(None, 36)
game_over_text = font.render(f"Game Over! Score: {score}", True, (255, 255, 255))
screen.blit(game_over_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
pygame.display.update()

pygame.time.delay(5000)

pygame.quit()
sys.exit()
