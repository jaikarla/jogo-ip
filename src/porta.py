# A porta só abre se o jogador tiver:
   # - pelo menos 7 meias
   # - pelo menos 7 presentes

def pode_abrir_porta(jogador):
    # Requisitos do jogo
    MEIAS_NECESSARIAS = 7
    PRESENTES_NECESSARIOS = 7

    if jogador.meias >= MEIAS_NECESSARIAS and jogador.presentes >= PRESENTES_NECESSARIOS:
        return True

    return False