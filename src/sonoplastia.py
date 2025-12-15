import pygame

pygame.mixer.init()

abobora_ruim = pygame.mixer.Sound('assets/sons/mixkit-losing-bleeps-2026.wav')
abobora_ruim.set_volume(0.5)

batida_morcego = pygame.mixer.Sound('assets/sons/smw_stomp_koopa_kid.wav')
batida_morcego.set_volume(0.9)

game_over = pygame.mixer.Sound('assets/sons/mixkit-horror-lose-2028.wav')
game_over.set_volume(0.8)

meias_e_presentes = pygame.mixer.Sound('assets/sons/smw_lemmy_wendy_correct.wav')
meias_e_presentes.set_volume(0.8)

presente_especial = pygame.mixer.Sound('assets/sons/mixkit-correct-answer-tone-2870.wav')

def inicio():
    pygame.mixer.music.load('assets/sons/Keshco - Halloween.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def tocar_musica_fundo():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('assets/sons/Denys Kyshchuk - Halloween.mp3')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

def tocar_vitoria():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('assets/sons/Christmas Village - Aaron Kenny.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def parar_musica():
    pygame.mixer.music.stop()
