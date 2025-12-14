import pygame
from .itens import Item

class Presente(Item):
    # Represnta um item coletável sem efeito colateral 
    # Aumenta o contador de presentes coletados pelo jogador

    # Quantidade miníma para vitória (ajustável)
    limite = 7

    def __init__(self, x, y):
        
        # imagem tempóraria
        self.image = pygame.Surface((25, 25))
        self.image.fill((34, 139, 34)) # verde

        # linha vermelha
        pygame.draw.rect(self.image, (255, 0, 0), (10, 0, 5, 25))
        pygame.draw.rect(self.image, (255, 0, 0), (0, 10, 25, 5))

        super().__init__(x, y) # precisa passar a imagem oficial

    def coletar(self, jogador):  
        # Lógica para quando o Jack colidir com um presente comum
        # Contador de presentes
        jogador.presentes += 1
        print(f"Presentes coletados: {jogador.presentes}")
 