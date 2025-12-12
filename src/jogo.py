import pygame

from jogador import Jogador #importar a classe Jogador
from aparicoes import Aparicoes #importar a classe Aparicoes
from cenarios import Cenarios #importar a classe Cenarios
from pontuacoes import Pontuacoes #importar a classe Pontuações

#---------------------------------------------------------------
#Cérebro do jogo - aqui controla-se o fluxo principal do jogo
#- loop principal
#- atualização lógica
#- desenho na tela
#- troca de estados (do menu para o jogo, do jogo para a tela de game over, etc)
#---------------------------------------------------------------

class Jogo:
    def __init__(self, tela):
        self.tela = tela
        self.clock = pygame.time.Clock()

        #estados do jogo
        self.state = "menu"  #estado inicial do jogo
        self.state = "jogando"  #quando o jogo está em andamento
        self.state = "game_over"  #quando o jogador perde todas as vidas
        self.state = "vitoria"  #quando o jogador vence o jogo

        #instanciar os componentes do jogo
        self.jogador = Jogador(300, 100)  #posição inicial do jogador
        self.aparicoes = Aparicoes()
        self.cenarios = Cenarios()
        self.pontuacoes = Pontuacoes()

    def rodar(self):
        rodando = True
        while rodando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False

            #atualizar lógica do jogo
            self.jogador.mover()
            self.aparicoes.atualizar()
            self.pontuacoes.atualizar_pontuacao(
                self.jogador.presentes,
                self.jogador.meias,
                self.jogador.aboboras
            )

            #desenhar na tela
            self.cenarios.desenhar(self.tela)
            self.jogador.desenhar(self.tela)
            self.aparicoes.desenhar(self.tela)
            self.pontuacoes.desenhar(self.tela)
