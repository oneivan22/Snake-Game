import pygame
from random import randint

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRID_SIZE = 20
SPEED = 5

BG_COLOR = (30, 30, 60)
APPLE_COLOR = (230, 50, 50)
SNAKE_COLOR = (80, 220, 80)
BORDER_COLOR = (180, 180, 200)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()


def create_apple():
    x = randint(0, SCREEN_WIDTH // GRID_SIZE - 1) * GRID_SIZE
    y = randint(0, SCREEN_HEIGHT // GRID_SIZE - 1) * GRID_SIZE
    return (x, y)


def draw_apple(surface, position):
    rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(surface, APPLE_COLOR, rect)
    pygame.draw.rect(surface, BORDER_COLOR, rect, 1)


def draw_snake(surface, positions):
    for pos in positions:
        rect = pygame.Rect(pos, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, SNAKE_COLOR, rect)
        pygame.draw.rect(surface, BORDER_COLOR, rect, 1)


def move_snake(positions, direction):
    head = positions[0]
    dx, dy = direction
    new_head = (
        (head[0] + dx * GRID_SIZE) % SCREEN_WIDTH,
        (head[1] + dy * GRID_SIZE) % SCREEN_HEIGHT
    )
    positions.insert(0, new_head)
    tail = positions.pop()
    return tail


def handle_keys(current_direction):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and current_direction != DOWN:
                return UP
            elif event.key == pygame.K_DOWN and current_direction != UP:
                return DOWN
            elif event.key == pygame.K_LEFT and current_direction != RIGHT:
                return LEFT
            elif event.key == pygame.K_RIGHT and current_direction != LEFT:
                return RIGHT
    return current_direction


def main():
    snake_positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
    snake_direction = RIGHT
    apple_position = create_apple()

    while True:
        clock.tick(SPEED)
        snake_direction = handle_keys(snake_direction)
        tail = move_snake(snake_positions, snake_direction)

        if snake_positions[0] == apple_position:
            snake_positions.append(tail)
            apple_position = create_apple()

        head = snake_positions[0]
        if head in snake_positions[1:]:
            snake_positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
            snake_direction = RIGHT
            apple_position = create_apple()

        screen.fill(BG_COLOR)
        draw_apple(screen, apple_position)
        draw_snake(screen, snake_positions)
        pygame.display.update()


main()
