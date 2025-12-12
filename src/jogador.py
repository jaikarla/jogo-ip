import pygame

class Jogador: #representa o jogador no jogo
    
    #---------------------------------------------------------------
    #essa classe gerencia:
    #- posição, velocidade, vidas, movimento
    #- pontuação (presentes, meias, abóboras)
    # efeitos de power-ups (presente especial)
    #---------------------------------------------------------------
    
    def __init__(self, y, x):
        #definir a posição inicial do jogador
        self.rect = self.image.get_rect(topleft=(x, y)) 

        self.velocidade = 5
        self.vidas = 3

        #pontuação
        self.presentes = 0
        self.meias = 0
        self.aboboras = 0

        #efeito do presente especial
        self.presente_especial = False

    #controla o movimento do jogador
    def mover(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidade # mover para cima
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidade # mover para baixo






