import pygame, sys

# Initialize the game
pygame.init()

cellNum = 8
cellSize = 90

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen
screen = pygame.display.set_mode((cellNum * cellSize, cellNum * cellSize))

# Condition for game to run
running = True


class CHESSBOARD:
    def __init__(self):
        pass

    def gameBoard(self):
        blockColor = (255, 255, 255)

        for col in range(cellNum):
            if col % 2 == 0:
                print("Hello")
                boardRect = pygame.Rect(col * cellSize, 0, cellSize, cellSize)
                pygame.draw.rect(screen, blockColor, boardRect)


chess = CHESSBOARD()


def main():
    global screen

    clock = pygame.time.Clock()

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        chess.gameBoard()
        screen.fill((0, 0, 0))
        pygame.display.update()


main()