import pygame

from src.jogo import Jogo 

def main():
    #inicializa o pygame
    pygame.init()

    #definir o tamanho da tela
    largura_tela = 800
    altura_tela = 600
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("O Pesadelo de Jack")

    pygame.quit()