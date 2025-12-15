import pygame
from src.porta import pode_abrir_porta

class Porta:
    def __init__(self, x, y, tile_size):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, tile_size, tile_size)

        # Carrega imagens
        self.img_fechada = pygame.image.load(
            "assets/portas/porta_fechada.png"
        ).convert_alpha()
        self.img_aberta = pygame.image.load(
            "assets/portas/porta_aberta.png"
        ).convert_alpha()

        # Ajusta tamanho da imagem para caber exatamente no TILE
        self.img_fechada = pygame.transform.scale(self.img_fechada, (tile_size, tile_size))
        self.img_aberta = pygame.transform.scale(self.img_aberta, (tile_size, tile_size))

    def desenhar(self, tela, jack):
        # Desenha a porta aberta ou fechada dependendo dos itens do jogador
        if pode_abrir_porta(jack):
            tela.blit(self.img_aberta, (self.x, self.y))
        else:
            tela.blit(self.img_fechada, (self.x, self.y))