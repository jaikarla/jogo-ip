import pygame

from src.cenarios import WIDTH, HEIGHT, FPS
from src.labirinto import Labirinto
from src.jogador import Jogador as Jack #jack é o jogador
from src.enemies.morcego import Morcego

class Jogo:
    #inicializa o jogo
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("O pesadelo de Jack")
        self.clock = pygame.time.Clock()

        self.labirinto = Labirinto()
        x, y = self.labirinto.posicao_inicial_jack()
        self.jack = Jack(x, y)
        self.morcego = Morcego(20*40, 8*40)

        self.rodando = True

    #executa o loop principal do jogo
    def executar(self):
        while self.rodando:
            self.tela.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando = False

            teclas = pygame.key.get_pressed()

            self.jack.mover(teclas, self.labirinto)
            self.morcego.perseguir(self.jack)

            self.labirinto.desenhar(self.tela)
            self.jack.desenhar(self.tela)
            self.morcego.desenhar(self.tela)

            if self.jack.rect.colliderect(self.morcego.rect):
                print("Jack foi pego!")
                self.rodando = False

            if self.labirinto.chegou_no_natal(self.jack.x, self.jack.y):
                print("Jack chegou ao Natal 🎄")
                self.rodando = False

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()
