"""
Snake (ООП)

Управление:
- Стрелки: движение
- R: перезапуск
- Esc: выход

Требования:
pip install pygame
"""

from __future__ import annotations

from dataclasses import dataclass
from random import choice, randrange
from typing import List, Optional, Tuple

import pygame


# ---- Константы игры ----
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRID_SIZE = 20

GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

FPS = 20

BOARD_BACKGROUND_COLOR = (0, 0, 0)
BORDER_COLOR = (40, 40, 40)

APPLE_COLOR = (255, 70, 70)
SNAKE_COLOR = (0, 200, 0)
HEAD_COLOR = (0, 255, 0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

Position = Tuple[int, int]


def to_cell(x: int, y: int) -> Position:
    """Привести пиксельные координаты к верхнему левому углу клетки."""
    return (x // GRID_SIZE * GRID_SIZE, y // GRID_SIZE * GRID_SIZE)


class GameObject:
    """Базовый класс для объектов на поле."""

    def __init__(self, position: Optional[Position] = None, body_color=(255, 255, 255)):
        self.position: Position = position or (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.body_color = body_color

    def draw(self, screen: pygame.Surface) -> None:
        """Отрисовка (переопределяется у наследников)."""
        raise NotImplementedError


class Apple(GameObject):
    """Яблоко, которое появляется в случайной клетке."""

    def __init__(self):
        super().__init__(body_color=APPLE_COLOR)
        self.position = (0, 0)

    def randomize_position(self, occupied: set[Position]) -> None:
        """Поставить яблоко в свободную клетку (не на змейку)."""
        while True:
            x = randrange(0, GRID_WIDTH) * GRID_SIZE
            y = randrange(0, GRID_HEIGHT) * GRID_SIZE
            if (x, y) not in occupied:
                self.position = (x, y)
                return

    def draw(self, screen: pygame.Surface) -> None:
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Змейка: список сегментов, движение, рост и проверка самостолкновения."""

    def __init__(self):
        super().__init__(body_color=SNAKE_COLOR)
        self.reset()

    def reset(self) -> None:
        """Сбросить змейку в начальное состояние."""
        start = to_cell(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.length: int = 1
        self.positions: List[Position] = [start]
        self.direction = RIGHT
        self.next_direction: Optional[Tuple[int, int]] = None
        self.last: Optional[Position] = None  # хвост, который надо стереть

    def get_head_position(self) -> Position:
        """Координаты головы."""
        return self.positions[0]

    def update_direction(self) -> None:
        """Применить отложенное направление (если задано)."""
        if self.next_direction is not None:
            self.direction = self.next_direction
            self.next_direction = None

    def set_next_direction(self, new_dir: Tuple[int, int]) -> None:
        """Установить следующее направление, запретив разворот на 180°."""
        dx, dy = self.direction
        ndx, ndy = new_dir
        if (dx + ndx, dy + ndy) == (0, 0):
            return
        self.next_direction = new_dir

    def move(self) -> bool:
        """
        Сдвинуть змейку на 1 клетку.

        Возвращает False, если произошло самостолкновение (нужен reset).
        """
        head_x, head_y = self.get_head_position()
        dx, dy = self.direction

        new_head = (
            (head_x + dx * GRID_SIZE) % SCREEN_WIDTH,
            (head_y + dy * GRID_SIZE) % SCREEN_HEIGHT,
        )

        # Самостолкновение (голова врезалась в тело, кроме первых 2 сегментов)
        if len(self.positions) > 2 and new_head in self.positions[2:]:
            return False

        self.positions.insert(0, new_head)

        if len(self.positions) > self.length:
            self.last = self.positions.pop()
        else:
            self.last = None

        return True

    def draw(self, screen: pygame.Surface) -> None:
        # тело
        for pos in self.positions[1:]:
            rect = pygame.Rect(pos, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        # голова
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, HEAD_COLOR, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        # “стирание” хвоста (опционально, если не очищать весь экран)
        if self.last is not None:
            tail_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, tail_rect)


def handle_keys(snake: Snake) -> bool:
    """
    Обработчик событий.

    Возвращает False, если нужно выйти из игры.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
            if event.key == pygame.K_r:
                snake.reset()

            if event.key == pygame.K_UP:
                snake.set_next_direction(UP)
            elif event.key == pygame.K_DOWN:
                snake.set_next_direction(DOWN)
            elif event.key == pygame.K_LEFT:
                snake.set_next_direction(LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.set_next_direction(RIGHT)

    return True


def draw_grid(screen: pygame.Surface) -> None:
    """Ненавязчивая сетка (опционально)."""
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, BORDER_COLOR, (x, 0), (x, SCREEN_HEIGHT), 1)
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, BORDER_COLOR, (0, y), (SCREEN_WIDTH, y), 1)


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Змейка (ООП)")
    clock = pygame.time.Clock()

    snake = Snake()
    apple = Apple()
    apple.randomize_position(occupied=set(snake.positions))

    running = True
    while running:
        clock.tick(FPS)  # ограничение частоты кадров/тиков [web:32]
        running = handle_keys(snake)

        snake.update_direction()
        alive = snake.move()
        if not alive:
            snake.reset()
            apple.randomize_position(occupied=set(snake.positions))
            continue

        # съели яблоко
        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position(occupied=set(snake.positions))

        # отрисовка
        screen.fill(BOARD_BACKGROUND_COLOR)
        draw_grid(screen)
        apple.draw(screen)
        snake.draw(screen)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
