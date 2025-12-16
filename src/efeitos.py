import pygame
import random

class Vinheta:
    def __init__(self, tela):
        self.surface = pygame.Surface(tela.get_size(), pygame.SRCALPHA)

    def draw(self, tela):
        # Escurece a tela
        self.surface.fill((0, 0, 0, 50))
        tela.blit(self.surface, (0, 0))

class Nevoa:
    def __init__(self, tela):
        self.surface = pygame.Surface(tela.get_size(), pygame.SRCALPHA)
        self.offset = 0
        self._gerar_nevoa()

    def _gerar_nevoa(self):
        for _ in range(300):  # quantidade de manchas
            x = random.randint(0, self.surface.get_width())
            y = random.randint(0, self.surface.get_height())
            r = random.randint(20, 60)
            alpha = random.randint(5, 15)

            pygame.draw.circle(
                self.surface,
                (180, 180, 180, alpha), (x, y), r)

    def draw(self, tela):
        self.offset -= 0.2 # velocidade do movimento da névoa
        tela.blit(self.surface, (self.offset, 0))
        tela.blit(self.surface, (self.offset + tela.get_width(), 0))