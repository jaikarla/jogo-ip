import pygame
from src.cenarios import TILE

class Morcego:
    # ---------------------------------------------------------------
    # Essa classe gerencia:
    # - posição e velocidade do morcego
    # - perseguição ao Jack
    # - animação das asas (4 frames)
    # ---------------------------------------------------------------

    def __init__(self, x, y):
        # posição lógica (float)
        self.pos = pygame.Vector2(x, y)

        # velocidade do morcego
        self.velocidade = 0.7

        # tamanho do morcego
        self.largura = TILE - 3
        self.altura = TILE - 3

        # rect usado para colisão / desenho (inteiro)
        self.rect = pygame.Rect(
            int(self.pos.x),
            int(self.pos.y),
            self.largura,
            self.altura
        )

        # -----------------------------------------------------------
        # carrega frames da animação
        # -----------------------------------------------------------
        self.frames = [
            pygame.image.load('assets/inimigos/morcego1.png').convert_alpha(),
            pygame.image.load('assets/inimigos/morcego2.png').convert_alpha(),
            pygame.image.load('assets/inimigos/morcego3.png').convert_alpha(),
            pygame.image.load('assets/inimigos/morcego4.png').convert_alpha()
        ]

        # redimensiona os frames
        self.frames = [
            pygame.transform.scale(frame, (self.largura, self.altura))
            for frame in self.frames
        ]

        # controle da animação
        self.frame_atual = 0
        self.tempo_animacao = 0
        self.vel_animacao = 0.2

        self.imagem_atual = self.frames[0]

    # ---------------------------------------------------------------
    # persegue o Jack
    # ---------------------------------------------------------------
    def perseguir(self, jack):
        direcao = pygame.Vector2(
            jack.hitbox.centerx - self.rect.centerx,
            jack.hitbox.centery - self.rect.centery
        )

        # evita divisão por zero
        if direcao.length() != 0:
            direcao = direcao.normalize()

        # move o morcego
        self.pos += direcao * self.velocidade

        # atualiza rect (inteiro)
        self.rect.topleft = (int(self.pos.x), int(self.pos.y))

        # anima enquanto se move
        self.animar()

    # ---------------------------------------------------------------
    # controla a animação das asas
    # ---------------------------------------------------------------
    def animar(self):
        self.tempo_animacao += self.vel_animacao

        if self.tempo_animacao >= 1:
            self.tempo_animacao = 0
            self.frame_atual = (self.frame_atual + 1) % len(self.frames)
            self.imagem_atual = self.frames[self.frame_atual]

    # ---------------------------------------------------------------
    # desenha o morcego na tela
    # ---------------------------------------------------------------
    def desenhar(self, tela):
        tela.blit(self.imagem_atual, self.rect)
