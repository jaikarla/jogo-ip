import pygame
import random

from .itens import Item

class presenteEspecial(Item):
    # Representa um item coletável que concede bônus de pontuação e aumento de velocidade temporário
    # Ao coletar um presente especial, Jack ganha o dobro de presentes

    def __init__(self, x, y, labirinto):
    
        self.labirinto = labirinto

        # Imagem temporaria
        self.image = pygame.Surface((25, 25))
        self.image.fill((255, 215, 0)) # Cor Ouro
        pygame.draw.rect(self.image, (255, 255, 255), (10, 0, 5, 25)) 
        
        super().__init__(x, y) # precisa passar a imagem oficial

        # Controle de tempo para o teletransporte (5 segundos)
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
        # Logica para quando o Jack colidir com um presente de ouro

        # Dobra a quantidade atual de presentes
        jogador.presentes += 2
        jogador.especiais += 1

        # Boost de velocidade (ajustavel)
        jogador.velocidade = 5.5

        # Gerenciador de tempo para que o aumento da velocidade seja temporário (5 segundos)(ajustavel)
        jogador.timer_do_bonus = pygame.time.get_ticks() # Marca a hora da coleta
        jogador.bonus_ativo = True
        print(f"BÔNUS DE OURO!")