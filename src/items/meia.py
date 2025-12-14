import pygame
from .itens import Item

class Meia(Item):
    # Representa um item coletável sem efeitos
    # Aumenta o contador de meias coletadas pelo jogador

    # Quantidade mínima para vitória (ajustável)
    limite = 7 

    def __init__(self, x, y):
         
        # imagem temporaria 
        self.image = pygame.Surface((20, 25), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (200, 0, 0), (0, 5, 20, 20)) # Base vermelha
        pygame.draw.rect(self.image, (255, 255, 255), (0, 0, 20, 7)) # Topo branco
        
        super().__init__(x, y)
        
    def coletar(self, jogador):
        # Lógica para quando o Jack colidir com uma meia  
        # Contador de meias
        jogador.meias += 1
        print(f"Meias coletadas: {jogador.meias}")