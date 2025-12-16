import pygame
import random

from .itens import Item

from src.sonoplastia import presente_especial

class presenteEspecial(Item):
    # Representa um item coletável que concede bônus de pontuação e aumento de velocidade temporário
    # Ao coletar um presente especial, Jack ganha o dobro de presentes

    def __init__(self, x, y, labirinto):
    
        self.labirinto = labirinto

        # Imagem 
        self.image = pygame.image.load('assets/itens/presente_especial.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (42, 42))

        super().__init__(x, y) # precisa passar a imagem oficial

        # Controle de tempo para o teletransporte (5 segundos)
        self.ultimo_pulo = pygame.time.get_ticks()
        self.intervalo_pulo = 12000

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
        jogador.velocidade = 6.0

        presente_especial.play()

        # Gerenciador de tempo para que o aumento da velocidade seja temporário (5 segundos)(ajustavel)
        jogador.timer_do_bonus = pygame.time.get_ticks() # Marca a hora da coleta
        jogador.bonus_ativo = True
        print(f"BÔNUS DE OURO!")