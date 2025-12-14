import pygame
from pygame.locals import *

pygame.init()

musica_de_fundo = pygame.mixer.music.load('Denys Kyshchuk - Halloween.mp3')
pygame.mixer.music.set_volume(0.4)


abobora_ruim = pygame.mixer.Sound('mixkit-losing-bleeps-2026.wav')
abobora_ruim.set_volume(0.5)

batida_morcego = pygame.mixer.Sound('smw_stomp_koopa_kid.wav')
batida_morcego.set_volume(1.1)

game_over = pygame.mixer.Sound('mixkit-horror-lose-2028.wav')

presente_especial = pygame.mixer.Sound('mixkit-correct-answer-tone-2870.wav')
presente_especial.set_volume(1.0)


meias_e_presentes = pygame.mixer.Sound('smw_lemmy_wendy_correct.wav')
meias_e_presentes.set_volume(1.5)
