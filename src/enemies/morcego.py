from src.enemies.inimigos import Inimigo

class Morcego(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        #add a imagem do morcego

    def colisao(self, jogador):
        #lógica para quando o morcego colidir com o jogador
        pass

