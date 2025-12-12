from .itens import Item

class Meia(Item):

    #precisa aumentar o contador de meias coletadas do jogador

    def __init__(self, x, y):
        super().__init__(x, y) #precisa passar a imagem no super()

    def coletar(self, jogador):  
        #lógica para quando o jogador coleta a meia
        pass