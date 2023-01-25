import pygame
pygame.init()

pygame.display.set_caption("sorting visuals")

BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)


class Display:
    WIDTH, HEIGHT = 1080, 720
    DIMENSIONS = (WIDTH, HEIGHT)
    FPS = 0

    DELAY_TIME = 0

    def __init__(self, frames):
        self.screen = pygame.display.set_mode(self.DIMENSIONS)
        self.clock = pygame.time.Clock()

        self.frames = frames
        self.index = 0
        self.time = 0

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
        self.time += delta
        if self.time > self.DELAY_TIME:
            self.time = 0
            self.index = min(len(self.frames) - 1, self.index + 1)

    def draw(self, surf):
        surf.fill(WHITE)

        width = self.WIDTH / len(self.frames[self.index])
        height = self.HEIGHT / max(self.frames[self.index])

        for i, element in enumerate(self.frames[self.index]):
            r = pygame.Rect(i * width, self.HEIGHT - element * height + 1, width + 1, element * height)
            pygame.draw.rect(surf, BLACK, r)
