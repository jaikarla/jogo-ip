import pygame
from src.cenarios import TILE

class Jogador:
    # ---------------------------------------------------------------
    # Essa classe gerencia:
    # - posição e velocidade
    # - sprite do personagem (Jack)
    # - movimentação
    # - colisão com paredes
    # ---------------------------------------------------------------

    def __init__(self, x, y):
        # posição inicial
        self.x = x
        self.y = y

        # velocidade do personagem
        self.velocidade = 3

        # tamanho do sprite
        self.largura = TILE - 5
        self.altura = TILE - 5

        hitbox_largura = self.largura * 0.5 
        hitbox_altura = self.altura * 0.7   

        self.hitbox = pygame.Rect(
            self.x + (self.largura - hitbox_largura) // 2,  # centraliza
            self.y + self.altura - hitbox_altura,          # cola no chão
            hitbox_largura,
            hitbox_altura
        )

        # rect do sprite
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

        # carregando imagens do personagem
        self.img_frente = pygame.image.load('assets/jogador/jack_frente.png').convert_alpha()
        self.img_costas = pygame.image.load('assets/jogador/jack_costas.png').convert_alpha()
        self.img_esquerda = pygame.image.load('assets/jogador/jack_esquerdo.png').convert_alpha()
        self.img_direita = pygame.image.load('assets/jogador/jack_direito.png').convert_alpha()

        # redimensionando as imagens
        self.img_frente = pygame.transform.scale(self.img_frente, (self.largura, self.altura))
        self.img_costas = pygame.transform.scale(self.img_costas, (self.largura, self.altura))
        self.img_esquerda = pygame.transform.scale(self.img_esquerda, (self.largura, self.altura))
        self.img_direita = pygame.transform.scale(self.img_direita, (self.largura, self.altura))

        # imagem inicial
        self.imagem_atual = self.img_frente

    # movimentação do jogador
    def mover(self, teclas, labirinto):
        vel_x = 0
        vel_y = 0

        # movimentação e troca de sprite
        if teclas[pygame.K_UP]:
            vel_y = -self.velocidade
            self.imagem_atual = self.img_costas

        if teclas[pygame.K_DOWN]:
            vel_y = self.velocidade
            self.imagem_atual = self.img_frente

        if teclas[pygame.K_LEFT]:
            vel_x = -self.velocidade
            self.imagem_atual = self.img_esquerda

        if teclas[pygame.K_RIGHT]:
            vel_x = self.velocidade
            self.imagem_atual = self.img_direita

        # -----------------------------------------------------------
        # movimentação separada por eixo
        self.mover_eixo(vel_x, 0, labirinto)
        self.mover_eixo(0, vel_y, labirinto)

        # atualiza posição do sprite com base na hitbox
        self.rect.centerx = self.hitbox.centerx
        self.rect.bottom = self.hitbox.bottom

    # ---------------------------------------------------------------
    # move pixel por pixel 
    def mover_eixo(self, dx, dy, labirinto):
        passos = int(abs(dx + dy))

        for _ in range(passos):
            novo_hitbox = self.hitbox.move(
                1 if dx > 0 else -1 if dx < 0 else 0,
                1 if dy > 0 else -1 if dy < 0 else 0
            )

            # só bloqueia se colidir com parede
            if not labirinto.colide_parede(novo_hitbox):
                self.hitbox = novo_hitbox
            else:
                break

    # desenha o personagem na tela
    def desenhar(self, tela):
        tela.blit(self.imagem_atual, self.rect)