import pygame

from src.cenarios import TILE

class Morcego:
    # ---------------------------------------------------------------
    # Essa classe gerencia:
    # - posição e velocidade do morcego
    # - perseguição ao Jack
    # - animação das asas (4 frames)
    # ---------------------------------------------------------------

    #ainda vou alterar coisas aqui - jai
    def __init__(self, x, y):
        #posicao inicial
        self.x = x
        self.y = y

        #velocidade do morcego
        self.velocidade = 0.8

        #tamanho do morcego
        self.largura = TILE - 4
        self.altura = TILE - 4

        # rect usado para posição / colisão
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

        #carrega as imagens e frames do morcego
        self.frames = [
            pygame.image.load('assets/inimigos/morcego1.png').convert_alpha(),
            pygame.image.load('assets/inimigos/morcego2.png').convert_alpha(),
            pygame.image.load('assets/inimigos/morcego3.png').convert_alpha(),
            pygame.image.load('assets/inimigos/morcego4.png').convert_alpha()
        ]

        #redimensionando os frames
        self.frames = [
            pygame.transform.scale(frame, (self.largura, self.altura))
            for frame in self.frames
        ]

        # controle da animação
        self.frame_atual = 0
        self.tempo_animacao = 0
        self.vel_animacao = 0.2  # quanto maior, mais rápido bate a asa

        # frame inicial
        self.imagem_atual = self.frames[0]

    #persegue o Jack
    def perseguir(self, jack):
        if jack.x > self.x:
            self.x += self.velocidade
        elif jack.x < self.x:
            self.x -= self.velocidade

        if jack.y > self.y:
            self.y += self.velocidade
        elif jack.y < self.y:
            self.y -= self.velocidade

        # atualiza rect
        self.rect.topleft = (self.x, self.y)

        # anima enquanto se move
        self.animar()

    #controla animação das asas
    def animar(self):
        self.tempo_animacao += self.vel_animacao

        if self.tempo_animacao >= 1:
            self.tempo_animacao = 0
            self.frame_atual = (self.frame_atual + 1) % len(self.frames)
            self.imagem_atual = self.frames[self.frame_atual]

    #desenha o morcego na tela
    def desenhar(self, tela):
        tela.blit(self.imagem_atual, self.rect)

