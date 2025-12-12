import random

from src.items.presente import Presente
from src.items.meia import Meia
from src.items.aboboraEstragada import aboboraEstragada
from src.items.presenteEspecial import presenteEspecial
from src.enemies.morcego import Morcego


#essa classe gerencia as aparições de itens e inimigos no jogo
#decide quando:
#- itens aparecem para o jogador coletar
#- reduzir a vida do jogador ao colidir com inimigos (morcegos)

#DEVE SER INSTANCIADA NO JOGO


