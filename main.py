import pygame, sys

# Initialize the game
pygame.init()

cellSize = 40
cellNumber = 20

# Screen
screen = pygame.display.set_mode((cellSize * cellNumber, cellSize * cellNumber))

# Condition for game to run
running = True


class CHESSBOARD:
    def __init__(self):
        pass


def main():
    global screen

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        pygame.display.update()


main()