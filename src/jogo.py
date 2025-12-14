import pygame
import random
import math

from src.cenarios import WIDTH, HEIGHT, FPS, TILE
from src.labirinto import Labirinto
from src.jogador import Jogador as Jack 
from src.enemies.morcego import Morcego
from src.items.aboboraEstragada import AboboraEstragada
from src.items.presente import Presente
from src.items.meia import Meia
from src.items.presenteEspecial import presenteEspecial

from src.sonoplastia import (
    inicio,
    tocar_musica_fundo,
    tocar_vitoria,
    abobora_ruim,
    batida_morcego,
    game_over,
    meias_e_presentes,
    parar_musica
)



class Jogo:
    # Inicializa o jogo
    def __init__(self):
        pygame.init()

        self.tela = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("O pesadelo de Jack")
        self.clock = pygame.time.Clock()

        # Configurações pixel
        self.fonte = pygame.font.Font('assets/pixel.ttf', 24)
        self.fonte_titulo = pygame.font.Font('assets/pixel.ttf', 60)
        self.fonte_botao = pygame.font.Font('assets/pixel.ttf', 36)

        # Inicialização do labirinto
        self.labirinto = Labirinto()

        # Busca de espaços vazios
        vagas = self.labirinto.buscar_vagas()

        # Sorteio de posições iniciais para o Jack e os Morcegos
        pos_inicial_jack = random.choice(vagas)
        self.jack = Jack(pos_inicial_jack[0], pos_inicial_jack[1])
        
        # Lista de morcegos pra gerar
        self.morcegos = []

        self.tempo_spawn_morcego = 0
        self.intervalo_spawn = 10000  # 12 segundos (ms)
        self.max_morcegos = 2

        # ADICIONA O CORAÇÃO/PNG DA VIDA
        self.imagem_coracao = pygame.image.load('assets/coracao.png').convert_alpha()
        self.imagem_coracao = pygame.transform.scale(self.imagem_coracao, (40, 40))

        # ADICIONA AS IMAGENS DE VITÓRIA E DERROTA
        self.imagem_gameover = pygame.image.load('assets/gameover.png').convert_alpha() # Derrota
        self.imagem_gameover = pygame.transform.scale(self.imagem_gameover, (WIDTH, HEIGHT))

        self.imagem_youwin = pygame.image.load('assets/youwin.png').convert_alpha() # Vitoria
        self.imagem_youwin = pygame.transform.scale(self.imagem_youwin, (WIDTH, HEIGHT))

        # ADICIONA A IMAGEM DA TELA INICIAL
        self.imagem_inicio = pygame.image.load('assets/INICIO.png').convert_alpha()
        self.imagem_inicio = pygame.transform.scale(self.imagem_inicio, (WIDTH, HEIGHT))

        # ADICIONA A IMAGEM DA TELA COMO JOGAR
        self.imagem_como_jogar = pygame.image.load('assets/comojogar.png').convert_alpha()
        self.imagem_como_jogar = pygame.transform.scale(self.imagem_como_jogar, (WIDTH, HEIGHT))

        # Lista de coletavéis no mapa 
        self.itens = []
        self.espalhar_itens()

        # Variáveis de controle de tempo e respawn 
        self.tempo_inicio = pygame.time.get_ticks()
        self.atraso_morcegos = 500 # Morcegos esperam meio segundo para começar a perseguir
        self.tempo_ultimo_especial = 0
        self.intervalo_respawn_especial = 10000 

        self.rodando = True

    def tela_inicial(self):
        inicio()
        esperando = True
        
        # Definir os botões
        botao_jogar = pygame.Rect(WIDTH - 420, HEIGHT // 2, 300, 70)
        botao_como_jogar = pygame.Rect(WIDTH - 420, HEIGHT // 2 + 100, 300, 70)
        
        while esperando:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                
                # Detectar clique do mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_jogar.collidepoint(mouse_pos):
                        return True  # Começa o jogo
                    if botao_como_jogar.collidepoint(mouse_pos):
                        self.tela_como_jogar()  # Mostra instruções
            
            # Desenhar fundo
            if hasattr(self, 'imagem_inicio'):
                self.tela.blit(self.imagem_inicio, (0, 0))
            else:
                self.tela.fill((20, 20, 40))
            
            # Botão JOGAR
            cor_jogar = (10, 35, 80) if botao_jogar.collidepoint(mouse_pos) else (5, 22, 60)
            pygame.draw.rect(self.tela, cor_jogar, botao_jogar, border_radius=10)
            pygame.draw.rect(self.tela, (255, 215, 0), botao_jogar, 3, border_radius=10)  # Borda amarela dourada
            
            texto_jogar = self.fonte_botao.render("JOGAR", True, (255, 255, 255))
            texto_jogar_rect = texto_jogar.get_rect(center=botao_jogar.center)
            self.tela.blit(texto_jogar, texto_jogar_rect)
            
            # Botão COMO JOGAR
            cor_como = (10, 35, 80) if botao_como_jogar.collidepoint(mouse_pos) else (5, 22, 60)
            pygame.draw.rect(self.tela, cor_como, botao_como_jogar, border_radius=10)
            pygame.draw.rect(self.tela, (255, 215, 0), botao_como_jogar, 3, border_radius=10)  # Borda amarela dourada
            
            texto_como = self.fonte_botao.render("COMO JOGAR", True, (255, 255, 255))
            texto_como_rect = texto_como.get_rect(center=botao_como_jogar.center)
            self.tela.blit(texto_como, texto_como_rect)
            
            pygame.display.update()
            self.clock.tick(FPS)
        
        return False

    def tela_como_jogar(self):
        mostrando = True
        
        botao_voltar = pygame.Rect(WIDTH // 2 - 125, HEIGHT - 100, 250, 65)
        
        while mostrando:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_voltar.collidepoint(mouse_pos):
                        mostrando = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        mostrando = False
            
            # Desenha a imagem de instruções
            if hasattr(self, 'imagem_como_jogar'):
                self.tela.blit(self.imagem_como_jogar, (0, 0))
            else:
                self.tela.fill((20, 20, 40))
            
            # Botão VOLTAR
            cor_voltar = (10, 35, 80) if botao_voltar.collidepoint(mouse_pos) else (5, 22, 60)
            pygame.draw.rect(self.tela, cor_voltar, botao_voltar, border_radius=10)
            pygame.draw.rect(self.tela, (255, 215, 0), botao_voltar, 3, border_radius=10)  # Borda amarela dourada
            
            texto_voltar = self.fonte_botao.render("VOLTAR", True, (255, 255, 255))
            texto_voltar_rect = texto_voltar.get_rect(center=botao_voltar.center)
            self.tela.blit(texto_voltar, texto_voltar_rect)
            
            pygame.display.update()
            self.clock.tick(FPS)

    # cria um novo morcego em posições aleatórias (Samara - Ajustado para evitar spawn na cara do jogador)
    def spawn_morcego(self):  
        vagas = self.labirinto.buscar_vagas()
        
        # Filtra vagas seguras
        vagas_seguras = [
            v for v in vagas 
            if math.hypot(v[0] - self.jack.x, v[1] - self.jack.y) > 350
        ]
        
        # Escolhe uma posição segura 
        if vagas_seguras:
            posicao = random.choice(vagas_seguras)
        else:
            posicao = random.choice(vagas)

        self.morcegos.append(Morcego(posicao[0], posicao[1]))
    
    def espalhar_itens(self):
        # Lógica de distribuição de itens 
        vagas = []

        # Percorre o mapa procurando onde tem espaço livre ("0")
        for r in range(self.labirinto.rows):
            for c in range(self.labirinto.cols):
                if self.labirinto.mapa[r][c] == "0":
                    vagas.append((c * 40, r * 40)) 
        
        # Lista de vagas seguras (lugares longe do Jack para evitar morte imediata)
        vagas_seguras = []
        for vx, vy in vagas:
            # Calcula a distância entre a vaga e a posição atual do Jack
            distancia = math.hypot(vx - self.jack.x, vy - self.jack.y)

            # Garantir que não comece cercado por abóboras
            if distancia > 100:
                vagas_seguras.append((vx, vy))

        # Quantidades dos itens coletaveis no mapa (ajustavel)
        num_abo, num_pre, num_meias = 5, 10, 10
        total_itens = num_abo + num_pre + num_meias
        
        # Escolher lugares que estão seguros
        if len(vagas_seguras) >= total_itens:
            locais_escolhidos = random.sample(vagas_seguras, total_itens) 

            # Adicionar as abóboras
            for i in range(0, num_abo):
                pos = locais_escolhidos[i]
                self.itens.append(AboboraEstragada(pos[0], pos[1]))

            # Adicionar os presentes
            for i in range(num_abo, num_abo + num_pre):
                pos = locais_escolhidos[i]
                self.itens.append(Presente(pos[0], pos[1]))
            
            # Adicionar as meias 
            for i in range(num_abo + num_pre, total_itens):
                pos = locais_escolhidos[i] 
                self.itens.append(Meia(pos[0], pos[1]))


    # Desenha os elementos (Samara - mudei o nome pra ser mais lúdico quando implementar as imagens dos outros contadores)
    def desenhar_elementos(self):
        # Desenha corações de vida
        for i in range(self.jack.vidas):
            self.tela.blit(self.imagem_coracao, (10 + i * 36, 3)) # espaçamento de 36 pixels, altura 4 pixels, margem esquerda 12 pixels

        # Informações de coleta (temporário - apenas para visualização)
        txt_pre = self.fonte.render(f"Presentes: {self.jack.presentes}/7", True, (0, 255, 0))
        txt_meia = self.fonte.render(f"Meias: {self.jack.meias}/7", True, (255, 255, 255)) 
        txt_abo = self.fonte.render(f"Aboboras: {self.jack.aboboras}", True, (255, 128, 0)) 
        txt_esp = self.fonte.render(f"Especiais: {self.jack.especiais}", True, (255, 215, 0)) 
        self.tela.blit(txt_pre, (150, 10))
        self.tela.blit(txt_meia, (380, 10))
        self.tela.blit(txt_abo, (580, 10))
        self.tela.blit(txt_esp, (780, 10))

        
    # Executa o loop principal do jogo
    def executar(self):
        # Mostrar tela inicial primeiro 
        if not self.tela_inicial():
            pygame.quit()
            return
        tocar_musica_fundo()

        while self.rodando:
            self.tela.fill((0, 0, 0))
            agora = pygame.time.get_ticks()
            tempo_decorrido = agora - self.tempo_inicio

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando = False

            # Só ocorre se Jack estiver vivo
            if self.jack.vivo:
                # Movimentação do Jogador
                teclas = pygame.key.get_pressed()
                self.jack.mover(teclas, self.labirinto)

                # Atualiza a invencibilidade do Jack 
                self.jack.atualizar_invencibilidade(self.clock.get_time())

                # Reaparecimento do presente especial
                tem_especial = any(isinstance(item, presenteEspecial) for item in self.itens)
                if not tem_especial:
                    if self.tempo_ultimo_especial == 0:  
                        self.tempo_ultimo_especial = agora

                    if agora - self.tempo_ultimo_especial > self.intervalo_respawn_especial:
                        vagas = self.labirinto.buscar_vagas()
                        if vagas:
                            pos = random.choice(vagas)
                            self.itens.append(presenteEspecial(pos[0], pos[1], self.labirinto))
                            self.tempo_ultimo_especial = 0
                else: 
                    self.tempo_ultimo_especial = 0

                # Controle de spawn por tempo 
                if tempo_decorrido > self.atraso_morcegos:
                    if len(self.morcegos) < self.max_morcegos:
                        self.tempo_spawn_morcego += self.clock.get_time()
                        if self.tempo_spawn_morcego >= self.intervalo_spawn:
                            self.spawn_morcego()
                            self.tempo_spawn_morcego = 0
                    else: 
                        self.tempo_spawn_morcego = 0

                    for morcego in self.morcegos:
                        morcego.perseguir(self.jack)

                # Verificação de colisão com os itens
                hitbox_jack = self.jack.rect.inflate(-10, -10)
                for item in self.itens[:]:
                    if hitbox_jack.colliderect(item.rect):
                        if isinstance(item, AboboraEstragada):
                            abobora_ruim.play()
                            
                        if isinstance(item, Meia):
                            meias_e_presentes.play()

                        if isinstance(item, Presente):
                            meias_e_presentes.play()

                        item.coletar(self.jack) 
                        self.itens.remove(item)

                        # Se coletar a quantidade limite de aboboras 
                        if self.jack.vidas <= 0:
                            print("Jack pegou abóboras demais e não resistiu!")
                            self.rodando = False

                # Verificação de colisão com morcegos 
                for morcego in self.morcegos[:]:
                    if self.jack.rect.colliderect(morcego.rect):
                        if not self.jack.invencivel:
                            batida_morcego.play()
                            if self.jack.receber_dano():
                                self.morcegos.remove(morcego)
                                print("Jack foi pego!")

                # Reset da velocidade 
                if hasattr(self.jack, 'bonus_ativo') and self.jack.bonus_ativo:
                    if agora - self.jack.timer_do_bonus > 5000: # 5 segundos
                        self.jack.velocidade = self.jack.velocidade_original
                        self.jack.bonus_ativo = False
                        print("O efeito passou! Velocidade normalizada.")

            # Desenhar tudo na tela
            self.labirinto.desenhar(self.tela)

            # Desenha itens
            for item in self.itens: 
                self.tela.blit(item.image, item.rect)
            
            # Desenha morcegos
            for morcego in self.morcegos: 
                morcego.desenhar(self.tela)

            # Desenha o Jack e as vidas
            self.jack.desenhar(self.tela)
            
            self.desenhar_elementos()
         

            # Verificar derrota por vidas
            if self.jack.vidas <= 0 or not self.jack.vivo:
                parar_musica()
                game_over.play()
                print("Jack perdeu todas as vidas! Fim de jogo.")

                # Mostra a tela de game over
                self.tela.blit(self.imagem_gameover, (0, 0))
                pygame.display.update()
                pygame.time.wait(3000)  # 3 segundos antes de fechar
                self.rodando = False

            # Verificar vitória
            if self.labirinto.chegou_no_natal(self.jack.hitbox.centerx,
                                              self.jack.hitbox.centery):
                if self.jack.presentes >= 7 and self.jack.meias >= 7: 
                    tocar_vitoria()
                    print("Jack chegou ao Natal 🎄")

                    # Mostra a tela de vitoria  
                    self.tela.blit(self.imagem_youwin, (0, 0))
                    pygame.display.update()
                    pygame.time.wait(10000)  # 3 segundos antes de fechar
            
                    self.rodando = False
                else: # Derrota
                    game_over.play()
                    print("GAME OVER! Jack falhou na missão. As crianças do mundo inteiro ficaram sem presentes e Natal esse ano 💀")

                    # Mostra a tela de game over
                    self.tela.blit(self.imagem_gameover, (0, 0))
                    pygame.display.update()
                    pygame.time.wait(3000)
                    
                    self.jack.vidas = 0 
                    self.rodando = False

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()