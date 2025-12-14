import pygame
from .itens import Item

class AboboraEstragada(Item):
    # Representa um item coletável de penalidade.
    # Coletar abóboras reduz a velocidade do Jack e pode levar ao Game Over.
    # Aumenta o contador de abóboras

    # Quantidade máxima que o jogador pode coletar (ajustável)
    limite = 4

    def __init__(self, x, y):
    
        # Imagem temporária 
        self.image = pygame.Surface((32,32))
        self.image.fill((180, 100, 20))

        super().__init__(x, y)
        # Precisa passar a imagem oficial 

    
    def coletar(self, jogador):  
        # Lógica para quando o Jack colidir com uma abóbora estragada
        
        # Contador de abóboras
        jogador.aboboras+= 1
        
        # Penalidade de Velocidade (reduz em 30%)
        jogador.velocidade *= 0.7

        # Gerenciador de tempo para que o efeito seja temporário 
        jogador.timer_do_bonus = pygame.time.get_ticks()
        jogador.bonus_ativo = True
        print(f"Abóboras: {jogador.aboboras}")

        # Condição de derrota (passar da quantidade limite estabelecida)
        if jogador.aboboras >= self.limite:
            jogador.morrer()
            print("GAME OVER por abóboras!")

       