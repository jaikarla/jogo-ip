import pygame
import random

from .itens import Item

class Presente(Item):
    # Represnta um item coletável sem efeito colateral 
    # Aumenta o contador de presentes coletados pelo jogador

    # Quantidade miníma para vitória (ajustável)
    limite = 7

    def __init__(self, x, y, labirinto):
        self.labirinto = labirinto

        # imagem 
        self.image = pygame.image.load('assets/itens/presente_simples.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (38, 38))

        super().__init__(x, y) # precisa passar a imagem oficial

        # Controle de tempo para a troca de lugar
        self.ultimo_pulo = pygame.time.get_ticks()
        self.intervalo_pulo = 15000

    def atualizar(self):
        # Lógica para fazer o item aparecer em outro lugar aleatoriamente
        agora = pygame.time.get_ticks()

        if agora - self.ultimo_pulo > self.intervalo_pulo:
            vagas = self.labirinto.buscar_vagas()
            nova_pos = random.choice(vagas)
            self.rect.topleft = nova_pos
            self.ultimo_pulo = agora

    def coletar(self, jogador):  
        # Lógica para quando o Jack colidir com um presente comum
        # Contador de presentes
        jogador.presentes += 1
        print(f"Presentes coletados: {jogador.presentes}")
 