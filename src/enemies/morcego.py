import pygame

from src.cenarios import TILE, COR_MORCEGO

class Morcego:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 0.3
        self.rect = pygame.Rect(self.x, self.y, TILE-10, TILE-10)

    #persegue o Jack
    def perseguir(self, jack):
        if jack.x > self.x:
            self.x += self.velocidade
        elif jack.x < self.x:
            self.x -= self.velocidade

        if jack.y > self.y:
            self.y += self.velocidade
        elif jack.y < self.y:
            self.y -= self.velocidade

        self.rect.topleft = (self.x, self.y)

    #desenha o morcego na tela
    def desenhar(self, tela):
        pygame.draw.rect(tela, COR_MORCEGO, self.rect)

