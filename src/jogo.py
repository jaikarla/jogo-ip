import pygame
import random

from src.cenarios import WIDTH, HEIGHT, FPS, TILE
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

        self.rodando = True

        #cria labirinto e jogador
        self.labirinto = Labirinto()
        x, y = self.labirinto.posicao_inicial_jack()
        self.jack = Jack(x, y)
        
        #lista de morcegos pra gerar
        self.morcegos = []

        # controle de spawn dos morcegos
        self.tempo_spawn_morcego = 0
        self.intervalo_spawn = 10000  # 12 segundos (ms)
        self.max_morcegos = 3

        # ADICIONA O CORAÇÃO/PNG DA VIDA
        self.imagem_coracao = pygame.image.load('assets/coracao.png').convert_alpha()
        self.imagem_coracao = pygame.transform.scale(self.imagem_coracao, (40, 40))

    # desenha os corações na tela
    def desenhar_vidas(self):
        for i in range(self.jack.vidas):
            self.tela.blit(self.imagem_coracao, (10 + i * 36, 3)) # espaçamento de 36 pixels, altura 4 pixels, margem esquerda 12 pixels


    # cria um novo morcego em posições aleatórias
    def spawn_morcego(self):
        x = random.randint(1, (WIDTH // TILE) - 2) * TILE
        y = random.randint(1, (HEIGHT // TILE) - 2) * TILE
        self.morcegos.append(Morcego(x, y))


    #executa o loop principal do jogo
    def executar(self):
        while self.rodando:
            self.tela.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando = False

            teclas = pygame.key.get_pressed()

            #movimenta o Jack
            self.jack.mover(teclas, self.labirinto)

            # atualiza morcegos
            for morcego in self.morcegos:
                morcego.perseguir(self.jack)


            # controle de spawn por tempo
            self.tempo_spawn_morcego += self.clock.get_time()

            if self.tempo_spawn_morcego >= self.intervalo_spawn:
                self.tempo_spawn_morcego = 0

                if len(self.morcegos) < self.max_morcegos:
                    self.spawn_morcego()
                  

            #desenha tudo na tela
            self.labirinto.desenhar(self.tela)
            self.jack.desenhar(self.tela)
            self.desenhar_vidas()
         
            for morcego in self.morcegos:
                morcego.desenhar(self.tela)

            # atualiza invencibilidade do Jack
            dt = self.clock.get_time()
            self.jack.atualizar_invencibilidade(dt)

            # verifica colisão entre Jack e morcegos
            for morcego in self.morcegos[:]:
                if self.jack.rect.colliderect(morcego.rect):
                    tomou_dano = self.jack.receber_dano()
                    if tomou_dano:
                        print("Jack foi pego!")
                        self.morcegos.remove(morcego)
                    break
        
            if self.jack.vidas <= 0:
                print("Jack perdeu todas as vidas! Fim de jogo.")
                self.rodando = False

            # vitória
            if self.labirinto.chegou_no_natal(self.jack.hitbox.centerx,
                                              self.jack.hitbox.centery):
                print("Jack chegou ao Natal 🎄")
                self.rodando = False

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()