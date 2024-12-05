import pygame
from Board import Board

if __name__ == '__main__':
    pygame.init()
    board = Board(5, 7)

    size = width, height = 5 * board.cell_size + board.left * 2, 7 * board.cell_size + board.top * 2
    screen = pygame.display.set_mode(size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
