import pygame
from src.cenarios import TILE

class Jogador:
    # ---------------------------------------------------------------
    # Essa classe gerencia:
    # - posição e velocidade
    # - sprite do personagem (Jack)
    # - movimentação
    # - colisão com paredes
    #sistema de vidas e invencibilidade
    # ---------------------------------------------------------------

    def __init__(self, x, y):
        # Posição inicial no mapa
        self.x = x
        self.y = y

        # Velocidade do Jack
        self.velocidade_original = 3.5
        self.velocidade = self.velocidade_original

        # Tamanho do sprite
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

        # Vidas do jogador
        self.vidas = 3
        self.vivo = True

        # Inventário do Jack e Power-ups
        self.presentes = 0
        self.meias =  0
        self.aboboras = 0
        self.especiais = 0 
        self.bonus_ativo = False
        self.timer_do_bonus = 0

        # Invencibilidade após dano
        self.invencivel = False
        self.tempo_invencivel = 0
        self.duracao_invencivel = 1500  # ms (1.5s)

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

    # jogador recebe dano
    def receber_dano(self):
        if not self.invencivel:
            self.vidas -= 1
            self.invencivel = True
            self.tempo_invencivel = 0
            return True  # dano recebido
        return False  # sem dano (invencível) 
    
    def atualizar_invencibilidade(self, dt):
        if self.invencivel:
            self.tempo_invencivel += dt
            if self.tempo_invencivel >= self.duracao_invencivel:
                self.invencivel = False
                self.tempo_invencivel = 0

    # Move o jogador conforme as teclas pressionadas
    def mover(self, teclas, labirinto):
        vel_x = 0
        vel_y = 0

        # Teclas utilizáveis (WASD, SETAS)
        # Movimentação e troca de sprite:

        # Cima
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            vel_y = -self.velocidade
            self.imagem_atual = self.img_costas

        # Baixo
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            vel_y = self.velocidade
            self.imagem_atual = self.img_frente

        # Esquerda
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            vel_x = -self.velocidade
            self.imagem_atual = self.img_esquerda

        # Direita
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            vel_x = self.velocidade
            self.imagem_atual = self.img_direita

        # Centralizar o Jack no labirinto para facilitar a navegação
        TILE_SIZE = 40
        
        # Se mover na vertical, alinha horizontalmente ao centro do corredor
        if vel_y != 0:
            centro_x = (self.hitbox.centerx // TILE_SIZE) * TILE_SIZE + TILE_SIZE // 2
            if abs(self.hitbox.centerx - centro_x) < 15:
                self.hitbox.centerx = centro_x
        
        # Se mover na horizontal, alinha verticalmente ao centro do corredor
        if vel_x != 0:
            centro_y = (self.hitbox.centery // TILE_SIZE) * TILE_SIZE + TILE_SIZE // 2
            if abs(self.hitbox.centery - centro_y) < 15:
                self.hitbox.centery = centro_y

        # Movimento com colisão (Eixo por Eixo)
        if vel_x != 0:
            proximo_passo = self.hitbox.move(vel_x, 0)
            if not labirinto.colide_parede(proximo_passo):
                self.hitbox = proximo_passo
        
        if vel_y != 0:
            proximo_passo = self.hitbox.move(0, vel_y)
            if not labirinto.colide_parede(proximo_passo):
                self.hitbox = proximo_passo

        # Atualiza a posição visual
        self.rect.center = self.hitbox.center
        self.x, self.y = self.rect.topleft

    
    # Desenha o personagem na tela
    def desenhar(self, tela): # efeito visual de psicar ao bater em um morcego
        if self.invencivel:
            if (pygame.time.get_ticks() // 100) % 2 == 0:
                tela.blit(self.imagem_atual, self.rect)
        else:
            tela.blit(self.imagem_atual, self.rect)
    
    def morrer(self):
        # Alterar o estado de vida do personagem
        self.vivo = False
        print("GAME OVER - Jack não resistiu")

