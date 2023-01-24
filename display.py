import pygame

pygame.init()

BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)


class Display:
    WIDTH, HEIGHT = 640, 640
    DIMENSIONS = (WIDTH, HEIGHT)
    FPS = 60

    def __init__(self):
        self.screen = pygame.display.set_mode(self.DIMENSIONS)
        self.clock = pygame.time.Clock()

    def show(self):
        is_running = True

        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

            self.update()
            self.draw(self.screen)

            pygame.display.flip()

        pygame.quit()

    def update(self):
        delta = self.clock.tick(self.FPS)

    def draw(self, surf):
        self.screen.fill(GRAY)
