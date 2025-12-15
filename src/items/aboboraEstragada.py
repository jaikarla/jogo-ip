import pygame
import random 

from .itens import Item

class AboboraEstragada(Item):
    # Representa um item coletável de penalidade.
    # Coletar abóboras reduz a velocidade do Jack e pode levar ao Game Over.
    # Aumenta o contador de abóboras

    # Quantidade máxima que o jogador pode coletar (ajustável)
    limite = 4

    def __init__(self, x, y, labirinto):
        self.labirinto = labirinto
    
        # Imagem 
        self.image = pygame.image.load('assets/itens/abobora_estragada.png').convert_alpha()

        self.image = pygame.transform.scale(self.image, (40, 40))

        super().__init__(x, y)
        # Precisa passar a imagem oficial 

        # Controle de tempo para a troca de lugar
        self.ultimo_pulo = pygame.time.get_ticks()
        self.intervalo_pulo = 10000

    def atualizar(self):
        # Lógica para fazer o item aparecer em outro lugar aleatoriamente
        agora = pygame.time.get_ticks()

        if agora - self.ultimo_pulo > self.intervalo_pulo:
            vagas = self.labirinto.buscar_vagas()
            nova_pos = random.choice(vagas)
            self.rect.topleft = nova_pos
            self.ultimo_pulo = agora

    
    def coletar(self, jogador):  
        # Lógica para quando o Jack colidir com uma abóbora estragada
        
        # Contador de abóboras
        jogador.aboboras+= 1
        
        # Penalidade de Velocidade (reduz em 30%)
        jogador.velocidade *= 0.6

        # Gerenciador de tempo para que o efeito seja temporário 
        jogador.timer_do_bonus = pygame.time.get_ticks()
        jogador.bonus_ativo = True
        print(f"Abóboras: {jogador.aboboras}")

        # Condição de derrota (passar da quantidade limite estabelecida)
        if jogador.aboboras >= self.limite:
            jogador.morrer()
            print("GAME OVER por abóboras!")

       