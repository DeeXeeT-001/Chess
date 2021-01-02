import pygame, sys

# Initialize the game
pygame.init()

width = 750
cols = 8
sq_sz = width // cols

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen
screen = pygame.display.set_mode((width, width))

# Condition for game to run
running = True


def gameBoard():
    blockColor = (255, 255, 255)


print(sq_sz)


def main():
    global screen

    clock = pygame.time.Clock()

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameBoard()
        screen.fill((0, 0, 0))
        pygame.display.update()


main()