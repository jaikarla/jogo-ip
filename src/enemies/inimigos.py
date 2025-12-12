import pygame

class Inimigo:

    #base para todos os inimigos
    #define a posição e atualiza o estado do inimigo
    #cada inimigo específico (Morcego) herda desta classe

    #esta classe é utilizada como classe mãe - NÃO DEVE SER INSTANCIADA DIRETAMENTE

    def __init__(self, x, y):
        self.rect = self.image.get_rect(topleft=(x, y))

    def atualizar(self, jogador):
        pass

class Morcego(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        #add a imagem do morcego