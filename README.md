# O Pesadelo de Jack
## Integrantes da Equipe

  - Ana Clara Souza Bizarria <acsb2>
  - Byanca Haially Candido de Souza <bhcs>
  - Jaianny Karla de Oliveira Souza <jkos>
  - Maria Cláudia Silva Rocha <mcsr>
  - Raiana Laís Pereira Donato <rlpd>
  - Samara Petrilly de Arruda Barbosa <spab>

---

## Descrição Geral do Projeto
O Pesadelo de Jack é um jogo 2D inspirado no filme O Estranho Mundo de Jack, dirigido por Tim Burton. A narrativa acompanha Jack Skellington, o Rei das Abóboras, que ao sair de sua cidade descobre a Cidade do Natal. 
No jogo, o personagem precisa encontrar seu próprio caminho até o Natal, enfrentando diferentes rotas que nem sempre são corretas ou até mesmo seguras. Dessa forma, o jogador é desafiado a tomar decisões estratégicas enquanto explora um cenário que mescla elementos sombrios do Halloween com aspectos característicos do Natal. Todo o ambiente visual foi cuidadosamente inspirado no filme, preservando a identidade estética e realizando uma transição gradual para elementos natalinos.


## Estrutura do Projeto

---

## Arquitetura do Projeto
```
JOGO-IP/
├── assets/                       # Pasta original de recursos
├── src/                          # Código-fonte organizado
│   ├── enemies/                  # Submódulo de inimigos
│   │   ├── __init__.py           # Pasta de iniciação do python
│   │   └── morcego.py            # Classe do morcego
│   ├── items/                    # Personagens e objetos
│   │   ├── __init__.py           # asta de iniciação do python
│   │   ├── aboboraEstratada.py   # Classe abóbora estragada
│   │   ├── itens.py              # Classe dos itens coletáveis
│   │   ├── meia.py               # Classe da meia
│   │   ├── presente.py           # Classe do presente
│   │   └── presenteEspecial.py   # Classe do presente especial
│   ├── aparicoes.py              # Classe das aparições
│   ├── cenarios.py               # Classe dos cenários
│   ├── efeitos.py                # Classe dos efeitos especiais
│   ├── jogador.py                # Classe do jogador
│   ├── jogo.py                   # Classe do jogo, onde está a logica principal
│   ├── labirinto.py              # Classe do labirinto
│   ├── pontuacoes.py             # Classe pontuação
│   └── sonoplastia.py            # Sistema de áudio
├── .gitignore                    # Ignorar __pycache__ e arquivos de sistema
└── main.py                       # Arquivo que inicia tudo
```

---

## Capturas de Tela
### Tela Inicial:
### Como Jogar:
### Labirinto:
### Tela vitória:
### Tela game over:

## Ferramentas e Justificativas

Para o desenvolvimento de O Pesadelo de Jack, foram utilizadas diversas ferramentas que em conjunto tornaram possível os cenários, funcionamento e a sonoplastia aplicados. São essas: 

- **Python**: linguagem de programação utilizada para construção de todo o projeto, desde a implementação de classes até a integração com outras bibliotecas utilizadas; 
- **Pygame**: biblioteca python utilizada para carregamento e manipulação de imagens, captura de eventos do teclado para interações no jogo e reprodução de efeitos sonoros; 
- **Visual Studio Code**: ambiente de desenvolvimento utilizado pela equipe pela fácil adaptação, além de garantir fácil integração com o gitHub; 
- **GitHub**: utilizado para hospedagem do código fonte, controle de versões e colaboração da equipe; 
- **Trello**: ambiente de organização do projeto, utilizado para distribuir e rastrear as responsabilidades individuais e em equipe; 
- **Google Drive**: organização e visualização fácil dos requisitos gerais do projeto, armazenamento de links úteis e materiais de estudo; 
- **Discord e WhatsApp**: principais sistemas de comunicação com a monitoria e em equipe respectivamente.

---

## Divisão de Trabalho

| Membro                         | Responsabilidades                                                                 |
|--------------------------------|-----------------------------------------------------------------------------------|
| Ana Clara S. Bizarria          | Estrutura do código, documentação, organização da equipe e GitHub, relatório, apoio ao design e sonoplastia |
| Byanca Hayally C. Souza        | Mecânicas dos elementos, sistema de pontuação, interface e apoio à documentação   |
| Jaianny Karla O. Souza         | Design de personagens e elementos, mecânicas, organização do GitHub, documentação e sonoplastia |
| Maria Cláudia S. Rocha         | Estrutura do código, documentação, README, sonoplastia e apoio ao design dos cenários |
| Raiana Laís P. Donato          | Design de cenários e personagens, mecânicas e apoio à documentação                |
| Samara Petrilly A. Barbosa     | Mecânicas dos elementos, sistema de pontuação, interface e apoio à documentação   |


---

## Conceitos Utilizados na Disciplina

- **Comandos condicionais**: [if, elif, else] foram fundamentais para definir casos e aplicar condições específicas em que o personagem se encontra durante o percorrer do jogo, como aplicar condições de colisão com o inimigo, além de definir a sua própria movimentação ao receber os comandos do teclado;

- **Estruturas de laços de repetição**: [for e while] garantiram o loop de execução do jogo até que a condição de encerramento foi atingida;

- **Funções**: definiram as principais rotinas do jogo, ou seja, todas as ações que se repetiam com frequência. Dessa maneira foi possível atualizar o estado do personagem com muito mais facilidade. 

- **Programação orientada à objetos**: utilizada de forma essencial para uma boa modularização do projeto. Garantiu que cada classe fosse criada para representar entidades como o jogador, inimigos e elementos de cenário, encapsulando seus atributos e comportamentos e permitindo instanciá-los quando necessário.

---

## Desafios, Erros e Lições Aprendidas

**Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?**  

**Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?**  

**Quais as lições aprendidas durante o projeto?**  

---

## Instruções de Execução

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Instale as dependências:
```bash
pip install pygame
```

3. Execute o jogo:
```bash
python jogo.py
```

---

## Controles

| Ação                  | Jack                        | 
|-----------------------|-----------------------------|
| Mover para cima       | W ou ⭡                      | 
| Mover para baixo      | S ou ⭣                      | 
| Mover para a esquerda | A ou ⭠                      |
| Mover para a direita  | D ou ⭢                      | 


  
