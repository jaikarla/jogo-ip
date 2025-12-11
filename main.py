import pygame
from personagem import Jogador

pygame.init()

tela = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player = Jogador(100, 300)

rodando = True
while rodando:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    keys = pygame.key.get_pressed()
    player.mover(keys)
    player.atualizar_animacao()
    player.fisica()

    tela.fill((30, 30, 30))
    player.draw(tela)
    pygame.display.update()

pygame.quit()
