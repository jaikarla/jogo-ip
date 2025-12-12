import pygame

#define a interface do jogador
#deve exibir informações:
#- pontuação atual
#- vidas restantes
#- efeitos especiais ativos

#DEVE SER INSTANCIADA NO JOGO

class Interface:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)  #fonte padrão para o texto

    
    