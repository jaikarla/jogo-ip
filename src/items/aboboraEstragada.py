from .itens import Item

class aboboraEstragada(Item):

    #aumenta contador de abóboras
    #ao alcançar limite definido -> game over

    def __init__(self, x, y):
        super().__init__(x, y) #precisa passar a imagem no super()

    def coletar(self, jogador):  
        #lógica para quando o jogador coleta a abóbora estragada
        pass