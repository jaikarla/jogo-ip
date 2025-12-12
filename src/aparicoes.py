import random

from items import presente, meia, abobora_estragada, presente_especial
from enemies import morcego


#essa classe gerencia as aparições de itens e inimigos no jogo
#decide quando:
#- itens aparecem para o jogador coletar
#- reduzir a vida do jogador ao colidir com inimigos (morcegos)

#DEVE SER INSTANCIADA NO JOGO


class Aparicoes:
    def __init__(self):
        self.items = []
        self.ememies = []

    def atualizar(self, jogador):
        #identificar a coleta de itens
        #identificar colisão com morcegos
        pass
