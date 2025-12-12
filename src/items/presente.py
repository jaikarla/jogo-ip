from .itens import Item

class Presente(Item):

    #precisa aumentar o contador de presentes coletados do jogador

    def __init__(self, x, y):
        super().__init__(x, y) #precisa passar a imagem no super()

    def coletar(self, jogador):  
        #lógica para quando o jogador coleta o presente
        pass