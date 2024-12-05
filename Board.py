import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for h in range(self.width + 1):
            pygame.draw.line(screen, "white", (self.left + h * self.cell_size, self.top),
                             (self.left + h * self.cell_size, self.top + self.height * self.cell_size))
        for w in range(self.height + 1):
            pygame.draw.line(screen, "white", (self.left, self.top + w * self.cell_size),
                             (self.left + self.width * self.cell_size, self.top + w * self.cell_size))

