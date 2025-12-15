import pygame

class Item: #base para todos os itens coletáveis

    #define a posição e atualiza o estado do item
    #cada item específico (Presente, Meia, Abóbora Estragada, Presente Especial) herda desta classe
    
    #esta classe é utilizada como classe mãe - NÃO DEVE SER INSTANCIADA DIRETAMENTE
    
    def __init__(self, x, y):
        self.rect = self.image.get_rect(topleft=(x, y))

    def atualizar(self):
        pass

#requísito mínimo - três objetos coletáveis diferentes que herdam de Item
class Presente(Item):
    def __init__(self, x, y):
        super().__init__(x, y) 
        #add a imagem do presente --- já adicionada em presente.py

class Meia(Item):
    def __init__(self, x, y):
        super().__init__(x, y)
        #add a imagem da meia -- já adicionada em meia.py

class AboboraEstragada(Item):
    def __init__(self, x, y):
        super().__init__(x, y)
        #add a imagem da abóbora estragada -- já adicionada em aboboraEstragada.py

class PresenteEspecial(Item):
    def __init__(self, x, y):
        super().__init__(x, y)
        #add a imagem do presente especial -- já adicionada em presenteEspecial.py