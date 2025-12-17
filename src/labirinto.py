import pygame

from src.cenarios import TILE, COR_PAREDE
from src.porta import pode_abrir_porta ### raih

#mapa do labirinto
class Labirinto:
    # Define a estrutura física do mapa (caminhos, parede e o ponto de vitória)
    def __init__(self):
        # Matriz do mapa
        self.mapa = [
            "11111111111111111111111111111111",
            "1J000000000000000000000000000001",
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
            "11111111111101011111110111111111",
            "10000000000000010000000100000001",
            "10111111111111110111111101111101",
            "100000000000000000000000000000N1",
            "11111111111111111111111111111111",
            "11111111111111111111111111111111"
        ]

        # Dimensões do labirinto
        self.rows = len(self.mapa)
        self.cols = len(self.mapa[0])

        # Carrega a imagem da parede
        self.img_parede = pygame.image.load('assets/parede1.jpeg').convert()
        #ajusta pra tamanho do tile
        self.img_parede = pygame.transform.scale(self.img_parede, (TILE, TILE))

    # Desenha o labirinto na tela
    def desenhar(self, tela):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * TILE
                y = row * TILE
                tile = self.mapa[row][col]

                if tile == "1":
                    tela.blit(self.img_parede, (x, y))
                elif tile == "N":
                    pass  # Não desenha nada, a porta vai aparecer por cima (raiih)

    # Checa colisão com paredes
    def colide_parede(self, rect):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.mapa[row][col] == "1":
                    parede = pygame.Rect(col*TILE, row*TILE, TILE, TILE)
                    if rect.colliderect(parede):
                        return True
        return False

    def buscar_vagas(self):
        # Retornar uma lista com as coordenadas vazias para sortear onde os objetos vão aparecer
        vagas = []
        for r in range(self.rows):
            for c in range(self.cols):
                if self.mapa[r][c] == "0" or self.mapa[r][c] == "J":
                    vagas.append((c * TILE, r * TILE))
        return vagas

    # Checa se Jack chegou no Natal
    def chegou_no_natal(self, x, y, jack):
        col = int(x // TILE)
        row = int(y // TILE)

        if 0 <= row < self.rows and 0 <= col < self.cols:
            if self.mapa[row][col] == "N":
                return True
        return False

    # Encontra a posição inicial do Jack no labirinto
    def posicao_inicial_jack(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.mapa[row][col] == "J":
                    return col * TILE, row * TILE
                
    def posicao_porta(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.mapa[row][col] == "N":
                    return col * TILE, row * TILE
    
    
