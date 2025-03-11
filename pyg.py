import pygame
import sys

RED = (200,0,0)
GREEN = (0,200,0)
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 450
WINDOW_WIDTH = 450


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def drawGrid():
    blockSize = 50 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, pygame.Rect(x, y, 50, 50))
            pygame.draw.rect(SCREEN, BLACK, rect, 1)


main()