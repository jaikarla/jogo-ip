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
from src.porta_sprite import Porta
from src.porta import pode_abrir_porta
from src.efeitos import Vinheta, Nevoa

from src.sonoplastia import (
    inicio,
    tocar_musica_fundo,
    tocar_vitoria,
    abobora_ruim,
    batida_morcego,
    game_over,
    meias_e_presentes,
    parar_musica,
    somporta
)


class Jogo:
    # Inicializa o jogo
    def __init__(self):
        pygame.init()

        self.inventario_completo = False
        self.tocar_som_porta = False

        self.tela = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("O pesadelo de Jack")
        self.clock = pygame.time.Clock()

        # Configurações pixel
        self.fonte = pygame.font.Font('assets/pixel.ttf', 28)
        self.fonte_titulo = pygame.font.Font('assets/pixel.ttf', 60)
        self.fonte_botao = pygame.font.Font('assets/pixel.ttf', 36)

        # FUNDO DO JOGO (atrás do labirinto)     <<<<<<<<<<<<<-----------------------------------------------------------------------------------
        self.imagem_fundo = pygame.image.load('assets/fundo1.jpeg').convert()

        self.imagem_fundo = pygame.transform.scale(self.imagem_fundo, (WIDTH, HEIGHT))

        # Inicialização do labirinto
        self.labirinto = Labirinto()

        # Posição da porta (onde tem "N" no mapa) ###### raih
        x_porta, y_porta = self.labirinto.posicao_porta()

        # Cria a porta do Natal ##### raih
        self.porta = Porta(
            x_porta,
            y_porta,
            TILE
        )

        # Busca de espaços vazios
        vagas = self.labirinto.buscar_vagas()

        # Sorteio de posições iniciais para o Jack e os Morcegos
        pos_inicial_jack = random.choice(vagas)
        self.jack = Jack(pos_inicial_jack[0], pos_inicial_jack[1])
        
        # Lista de morcegos pra gerar
        self.morcegos = []
        self.tempo_spawn_morcego = 0
        self.intervalo_spawn = 15000  # 15 segundos (ms)
        self.max_morcegos = 3

        # ADICIONA O CORAÇÃO/PNG DA VIDA
        self.imagem_coracao = pygame.image.load('assets/coracao.png').convert_alpha()
        self.imagem_coracao = pygame.transform.scale(self.imagem_coracao, (40, 40))

        # ADICIONA AS IMAGENS DE VITÓRIA E DERROTA
        self.imagem_gameover = pygame.image.load('assets/telas/gameover.jpeg').convert() # Derrota
        self.imagem_gameover = pygame.transform.scale(self.imagem_gameover, (WIDTH, HEIGHT))

        self.imagem_youwin = pygame.image.load('assets/telas/ganhou.png').convert_alpha() # Vitoria
        self.imagem_youwin = pygame.transform.scale(self.imagem_youwin, (WIDTH, HEIGHT))

        # ADICIONA A IMAGEM DA TELA INICIAL
        self.imagem_inicio = pygame.image.load('assets/telas/inicio.jpeg').convert()
        self.imagem_inicio = pygame.transform.scale(self.imagem_inicio, (WIDTH, HEIGHT))

        # ADICIONA A IMAGEM DA TELA COMO JOGAR
        self.imagem_como_jogar = pygame.image.load('assets/telas/comojogar.png').convert_alpha()
        self.imagem_como_jogar = pygame.transform.scale(self.imagem_como_jogar, (WIDTH, HEIGHT))

        # Lista de coletavéis no mapa 
        self.itens = []

        # Ícones dos itens coletáveis 
        self.icone_presente = pygame.image.load('assets/itens/presente_simples.png').convert_alpha()
        self.icone_meia = pygame.image.load('assets/itens/meia.png').convert_alpha()
        self.icone_abobora = pygame.image.load('assets/itens/abobora_estragada.png').convert_alpha()
        self.icone_especial = pygame.image.load('assets/itens/presente_especial.png').convert_alpha()

        # Ajustar tamanho
        self.icone_presente = pygame.transform.scale(self.icone_presente, (36, 36))
        self.icone_meia = pygame.transform.scale(self.icone_meia, (36, 36))
        self.icone_abobora = pygame.transform.scale(self.icone_abobora, (36, 36))
        self.icone_especial = pygame.transform.scale(self.icone_especial, (36, 36))

        # timer para itens comuns
        self.tempo_ultimo_item_comum = 0
        self.intervalo_spawn_comum = 3000

        # Timers individuais para o "rodízio"
        self.ultimo_spawn_meia = 0
        self.ultimo_spawn_presente = 0
        self.ultimo_spawn_abobora = 0

        # Variáveis de controle de tempo e respawn 
        self.tempo_inicio = pygame.time.get_ticks()
        self.atraso_morcegos = 500 # Morcegos esperam meio segundo para começar a perseguir
        self.tempo_ultimo_especial = 0
        self.intervalo_respawn_especial = 10000 

        self.vinheta = Vinheta(self.tela)
        self.nevoa = Nevoa(self.tela)

        self.rodando = True

    def reiniciar(self):
        self.__init__()
        self.executar()

    def desenhar_botao_transparente(self, rect, cor, borda, texto, cor_texto):
        botao_surface = pygame.Surface(rect.size, pygame.SRCALPHA)

        # Cor com transparência (RGBA)
        cor_com_alpha = (*cor, 170)   # 170 = transparência (0 a 255)

        pygame.draw.rect(
            botao_surface,
            cor_com_alpha,
            botao_surface.get_rect(),
            border_radius=14
        )

        pygame.draw.rect(
            botao_surface,
            borda,
            botao_surface.get_rect(),
            2,
            border_radius=14
        )

        self.tela.blit(botao_surface, rect.topleft)

        # Texto (normal, sem transparência)
        texto_render = self.fonte_botao.render(texto, True, cor_texto)
        self.tela.blit(
            texto_render,
            texto_render.get_rect(center=rect.center)
        )

    def tela_inicial(self):
        inicio()
        esperando = True
        
        # TAMANHO DOS BOTÕES
        largura_botao = 260
        altura_botao = 70
        espaco = 40  # espaço entre os botões

        # POSIÇÃO BASE (centralizada embaixo)
        y_botao = HEIGHT - 160
        x_centro = WIDTH // 2

        # BOTÕES LADO A LADO
        botao_jogar = pygame.Rect(x_centro - largura_botao - espaco // 2, y_botao, largura_botao, altura_botao)

        botao_como_jogar = pygame.Rect( x_centro + espaco // 2, y_botao, largura_botao, altura_botao)
                
        # CORES (AJUSTAVEL)
        COR_NORMAL = (35, 32, 70)
        COR_HOVER = (55, 50, 110)
        BORDA = (255, 170, 60)
        TEXTO = (255, 200, 80)

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
            self.tela.blit(self.imagem_inicio, (0, 0))
            
            # BOTÃO JOGAR
            cor = COR_HOVER if botao_jogar.collidepoint(mouse_pos) else COR_NORMAL
            self.desenhar_botao_transparente(botao_jogar, cor, BORDA, "JOGAR", TEXTO)

            # BOTÃO COMO JOGAR
            cor = COR_HOVER if botao_como_jogar.collidepoint(mouse_pos) else COR_NORMAL
            self.desenhar_botao_transparente(botao_como_jogar, cor, BORDA, "COMO JOGAR",TEXTO)
            
            pygame.display.update()
            self.clock.tick(FPS)
        
        return False

    def tela_como_jogar(self):
        mostrando = True
        
        botao_voltar = pygame.Rect(WIDTH // 2 - 125, HEIGHT - 100, 250, 65)

        # CORES IGUAIS À TELA INICIAL
        COR_NORMAL = (35, 32, 70)
        COR_HOVER  = (55, 50, 110)
        BORDA      = (255, 170, 60)
        TEXTO      = (255, 200, 80)
        
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
            cor = COR_HOVER if botao_voltar.collidepoint(mouse_pos) else COR_NORMAL
            self.desenhar_botao_transparente( botao_voltar, cor, BORDA, "VOLTAR", TEXTO)
            
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
                self.itens.append(AboboraEstragada(pos[0], pos[1], self.labirinto))

            # Adicionar os presentes
            for i in range(num_abo, num_abo + num_pre):
                pos = locais_escolhidos[i]
                self.itens.append(Presente(pos[0], pos[1], self.labirinto))
            
            # Adicionar as meias 
            for i in range(num_abo + num_pre, total_itens):
                pos = locais_escolhidos[i] 
                self.itens.append(Meia(pos[0], pos[1], self.labirinto))


    # Desenha os elementos (Samara - mudei o nome pra ser mais lúdico quando implementar as imagens dos outros contadores)
    def desenhar_elementos(self):
        # Desenha corações de vida
        for i in range(self.jack.vidas):
            self.tela.blit(self.imagem_coracao, (10 + i * 36, 3)) # espaçamento de 36 pixels, altura 4 pixels, margem esquerda 12 pixels

        # POSIÇÕES DO HUD
        x_inicial = 200
        y = 4
        espacamento = 120

        # PRESENTES
        self.tela.blit(self.icone_presente, (x_inicial, y))
        txt_presente = self.fonte.render(f"{self.jack.presentes}/7", True, (255, 255, 255))
        self.tela.blit(txt_presente, (x_inicial + 40, y + 5))

        # MEIAS
        self.tela.blit(self.icone_meia, (x_inicial + espacamento, y))
        txt_meia = self.fonte.render(f"{self.jack.meias}/7", True, (255, 255, 255))
        self.tela.blit(txt_meia, (x_inicial + espacamento + 40, y + 5))

        # ABÓBORAS
        self.tela.blit(self.icone_abobora, (x_inicial + espacamento * 2, y))
        txt_abo = self.fonte.render(f"{self.jack.aboboras}/5", True, (255, 255, 255))
        self.tela.blit(txt_abo, (x_inicial + espacamento * 2 + 40, y + 5))

        # ESPECIAIS
        self.tela.blit(self.icone_especial, (x_inicial + espacamento * 3, y))
        txt_esp = self.fonte.render(f"{self.jack.especiais}", True, (255, 255, 255))
        self.tela.blit(txt_esp, (x_inicial + espacamento * 3 + 40, y + 5))

        
    # Executa o loop principal do jogo
    def executar(self):
        # Mostrar tela inicial primeiro 
        if not self.tela_inicial():
            pygame.quit()
            return
        tocar_musica_fundo()

        while self.rodando:
            self.tela.blit(self.imagem_fundo, (0, 0)) #------------------------- FUNDO DO JOGO
            agora = pygame.time.get_ticks()
            tempo_decorrido = agora - self.tempo_inicio

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando = False

            if self.tocar_som_porta:
                somporta.play()
                self.tocar_som_porta = False


            # Só ocorre se Jack estiver vivo
            if self.jack.vivo:
                # Movimentação do Jogador
                teclas = pygame.key.get_pressed()
                self.jack.mover(teclas, self.labirinto)

                # VERIFICA COLISÃO COM A PORTA
                if self.porta.rect.colliderect(self.jack.hitbox): ############# raih
                    if not pode_abrir_porta(self.jack):
                        # impede o movimento
                        self.jack.voltar_posicao()

                # Atualiza a invencibilidade do Jack 
                self.jack.atualizar_invencibilidade(self.clock.get_time())

                # GERENCIAMENTO DE ITENS NO MAPA
                for item in self.itens:
                    if hasattr(item, 'atualizar'):
                        item.atualizar()

                # Conta a quantidade atual de cada item para controle de limite
                qtd_meias = len([i for i in self.itens if isinstance(i, Meia)])
                qtd_presentes = len([i for i in self.itens if isinstance(i, Presente)])
                qtd_aboboras = len([i for i in self.itens if isinstance(i, AboboraEstragada)])

                # Meias: Aparecem a cada 4s se houver menos de 3
                if qtd_meias < 3 and agora - self.ultimo_spawn_meia > 4000:
                    vagas = self.labirinto.buscar_vagas()
                    if vagas:
                        pos = random.choice(vagas)
                        self.itens.append(Meia(pos[0], pos[1], self.labirinto))
                        self.ultimo_spawn_meia = agora

                # Presentes: Aparecem a cada 4s se houver menos de 3
                if qtd_presentes < 3 and agora - self.ultimo_spawn_presente > 4000:
                    vagas = self.labirinto.buscar_vagas()
                    if vagas:
                        pos = random.choice(vagas)
                        self.itens.append(Presente(pos[0], pos[1], self.labirinto))
                        self.ultimo_spawn_presente = agora

                # Abóboras: Aparecem a cada 4s se houver menos de 3
                if qtd_aboboras < 3 and agora - self.ultimo_spawn_abobora > 4000:
                    vagas = self.labirinto.buscar_vagas()
                    if vagas:
                        pos = random.choice(vagas)
                        self.itens.append(AboboraEstragada(pos[0], pos[1], self.labirinto))
                        self.ultimo_spawn_abobora = agora

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
                        # ZERAR RELÓGIO DE RESPQAWN QND PEGA O ITEM 
                        if isinstance(item, Meia):
                            self.ultimo_spawn_meia = agora
                        elif isinstance(item, Presente):
                            self.ultimo_spawn_presente = agora
                        elif isinstance(item, AboboraEstragada):
                            self.ultimo_spawn_abobora = agora
                        
                        item.coletar(self.jack) 
                        self.itens.remove(item)

                        if (
                            self.jack.meias >= 7 and
                            self.jack.presentes >= 7 and
                            not self.inventario_completo
                        ):
                            self.inventario_completo = True
                            self.tocar_som_porta = True


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

            # DESENHAR TUDO NA TELA -------------------------------------------------------------------------------------------------------------
            self.labirinto.desenhar(self.tela)

            # Desenha a porta ### raih
            self.porta.desenhar(self.tela, self.jack)

            # Desenha itens
            for item in self.itens: 
                self.tela.blit(item.image, item.rect)
            
            # Desenha morcegos
            for morcego in self.morcegos: 
                morcego.desenhar(self.tela)

            # Desenha o Jack e as vidas
            self.jack.desenhar(self.tela)

            self.nevoa.draw(self.tela)
            self.vinheta.draw(self.tela)
            
            self.desenhar_elementos()
         

            if self.jack.vidas <= 0 or not self.jack.vivo:
                parar_musica()
                game_over.play()

                self.tela.blit(self.imagem_gameover, (0, 0))
                pygame.display.update()
                pygame.time.wait(3000)

                self.reiniciar()
                return

            # Verificar vitória
            if self.labirinto.chegou_no_natal(self.jack.hitbox.centerx,
                                              self.jack.hitbox.centery, self.jack): #### raih
                if self.jack.presentes >= 7 and self.jack.meias >= 7: 
                    tocar_vitoria()

                    self.tela.blit(self.imagem_youwin, (0, 0))
                    pygame.display.update()
                    pygame.time.wait(5000)  # 5s fica melhor

                    self.reiniciar()
                    return

                else: # Derrota
                    # Apenas impedir abrir a porta, sem fechar o jogo
                    print("Jack precisa de mais presentes e meias para abrir a porta!")
                    self.jack.voltar_posicao()

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()