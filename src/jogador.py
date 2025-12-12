import pygame

from src.cenarios import TILE, COR_JACK

class Jogador: #representa o jogador no jogo
    
    #---------------------------------------------------------------
    #essa classe gerencia:
    #- posição, velocidade, vidas, movimento
    #- pontuação (presentes, meias, abóboras)
    # efeitos de power-ups (presente especial)
    #---------------------------------------------------------------
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 3
        self.rect = pygame.Rect(self.x, self.y, TILE-10, TILE-10)

    #move o jogador conforme as teclas pressionadas
    def mover(self, teclas, labirinto):
        vel_x = vel_y = 0

        if teclas[pygame.K_UP]: vel_y = -self.velocidade
        if teclas[pygame.K_DOWN]: vel_y = self.velocidade
        if teclas[pygame.K_LEFT]: vel_x = -self.velocidade
        if teclas[pygame.K_RIGHT]: vel_x = self.velocidade

        novo_rect = pygame.Rect(self.x + vel_x, self.y, TILE-10, TILE-10)
        if not labirinto.colide_parede(novo_rect):
            self.x += vel_x

        novo_rect = pygame.Rect(self.x, self.y + vel_y, TILE-10, TILE-10)
        if not labirinto.colide_parede(novo_rect):
            self.y += vel_y

        self.rect.topleft = (self.x, self.y)

    #desenha o jogador na tela
    def desenhar(self, tela):
        pygame.draw.rect(tela, COR_JACK, self.rect)







