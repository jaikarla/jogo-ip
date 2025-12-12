from .itens import Item

class presenteEspecial(Item):

    #ativa o estado presente especial no jogador

    def __init__(self, x, y):
        super().__init__(x, y) #precisa passar a imagem no super()

    def coletar(self, jogador):  
        #lógica para quando o jogador coleta o presente especial
        pass