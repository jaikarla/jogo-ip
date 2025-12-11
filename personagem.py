import pygame
import os

class Jogador:
    def __init__(self, x, y):
        # posição
        self.x = x
        self.y = y
        self.vel = 5

        # física do pulo
        self.vel_y = 0
        self.gravidade = 0.8
        self.chao = y      # posição base do chão
        self.no_chao = True

        # carregar animações
        self.idle = pygame.image.load(os.path.join("pngs", "jogador", "idle.png"))
        self.pulo = pygame.image.load(os.path.join("pngs", "jogador", "pulo.png"))

        self.walk_frames = [
            pygame.image.load(os.path.join("pngs", "jogador", "walk1.png")),
            pygame.image.load(os.path.join("pngs", "jogador", "walk2.png")),
            pygame.image.load(os.path.join("pngs", "jogador", "walk3.png"))
        ]

        # controle de animação
        self.frame_index = 0
        self.frame_delay = 10
        self.frame_count = 0

        # estado
        self.andando = False
        self.pulando = False

        self.image = self.idle

    def mover(self, keys):
        self.andando = False

        # movimentos laterais
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.vel
            self.andando = True

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.vel
            self.andando = True

        # pulo
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if self.no_chao:          # só pula se estiver no chão
                self.vel_y = -15      # força do pulo
                self.no_chao = False

    def fisica(self):
        # gravidade
        if not self.no_chao:
            self.vel_y += self.gravidade
            self.y += self.vel_y

        # tocar no chão
        if self.y >= self.chao:
            self.y = self.chao
            self.no_chao = True
            self.vel_y = 0

    def atualizar_animacao(self):
        if not self.no_chao:
            self.image = self.pulo
            return

        if self.andando:
            self.frame_count += 1
            if self.frame_count >= self.frame_delay:
                self.frame_count = 0
                self.frame_index = (self.frame_index + 1) % len(self.walk_frames)
            self.image = self.walk_frames[self.frame_index]
        else:
            self.image = self.idle

    def draw(self, tela):
        tela.blit(self.image, (self.x, self.y))
