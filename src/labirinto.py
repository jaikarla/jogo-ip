import pygame

from src.cenarios import TILE, COR_PAREDE, COR_NATAL

#mapa do labirinto
class Labirinto:
    def __init__(self):
        self.mapa = [
            "11111111111111111111111111111111",
            "1J000000000001000000000000000001",
            "10111101111110101111111101111101",
            "10000100000000100000000100000001",
            "11110101111111111011111110111111",
            "10000100000000000010000000100001",
            "10111111111101111110111111101101",
            "10000000000100000000100000000001",
            "11111101110111111110101111111101",
            "10000001000100000000000000000001",
            "10111111011101111111111101111101",
            "10000000000001000000000001000001",
            "11111111111111011111110111111111",
            "10000000000000010000000100000001",
            "10111111111111110111111101111101",
            "100000000000000000000000000000N1",
            "11111111111111111111111111111111"
        ]

        self.rows = len(self.mapa)
        self.cols = len(self.mapa[0])

    #desenha o labirinto na tela
    def desenhar(self, tela):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * TILE
                y = row * TILE
                tile = self.mapa[row][col]

                if tile == "1":
                    pygame.draw.rect(tela, COR_PAREDE, (x, y, TILE, TILE))
                elif tile == "N":
                    pygame.draw.rect(tela, COR_NATAL, (x, y, TILE, TILE))

    #checa colisão com paredes
    def colide_parede(self, rect):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.mapa[row][col] == "1":
                    parede = pygame.Rect(col*TILE, row*TILE, TILE, TILE)
                    if rect.colliderect(parede):
                        return True
        return False

    #checa se Jack chegou no Natal
    def chegou_no_natal(self, x, y):
        col = x // TILE
        row = y // TILE
        return self.mapa[row][col] == "N"

    #encontra a posição inicial do Jack no labirinto
    def posicao_inicial_jack(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.mapa[row][col] == "J":
                    return col * TILE, row * TILE
