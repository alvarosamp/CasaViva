# Inteligência Artificial nos Jogos

Projeto educacional que demonstra diferentes técnicas de Inteligência Artificial através de jogos clássicos implementados em Python com Pygame.

Cada jogo apresenta um conceito diferente de IA, desde algoritmos aleatórios até Minimax e Campos Potenciais.

---

## Jogos

### Akinator — Copa 2026
**Arquivo:** `akinator.py` | **Interface:** Terminal

O programa tenta adivinhar em qual dos 26 jogadores convocados pelo Brasil para a Copa do Mundo de 2026 você está pensando. A cada rodada, o algoritmo escolhe a pergunta que **divide ao meio** os jogadores restantes — a mesma lógica de uma árvore de decisão binária.

**Conceito de IA:** Árvore de Decisão / Ganho de Informação

```bash
python akinator.py
```

---

### Jogo da Velha — 3 níveis de IA
**Arquivo:** `jogodavelha.py` | **Interface:** Pygame

Jogue contra uma IA em três dificuldades crescentes:

| Nível | Estratégia |
|-------|-----------|
| Fácil | Jogadas completamente aleatórias |
| Médio | Ataca se puder ganhar, bloqueia se necessário, prefere o centro |
| Difícil | Algoritmo Minimax — explora todas as possibilidades e nunca perde |

**Conceitos de IA:** Aleatoriedade, Heurística, Minimax

```bash
python jogodavelha.py
```

---

### Jogo do Dino — Obstáculos com IA
**Arquivo:** `dino.py` | **Interface:** Pygame

Recriação do jogo do dinossauro do Chrome com velocidade crescente, cactos de diferentes tamanhos e pássaros voando em alturas variadas. A IA simula o tempo até o obstáculo e decide entre **pular** ou **agachar** com base na geometria real da colisão.

**Conceito de IA:** IA Reativa com Simulação Física

| Controle (Humano) | Ação |
|---|---|
| `Espaço` | Pular |
| `Seta para baixo` | Agachar |
| `ESC` | Voltar ao menu |

```bash
python dino.py
```

---

### Flappy Bird — Previsão de Trajetória
**Arquivo:** `flappybird.py` | **Interface:** Pygame

O pássaro controlado pela IA simula sua trajetória física frame a frame para decidir se deve ou não pular. Ela só pula quando a simulação confirma que o pulo vai colocar o pássaro dentro do vão — sem subir demais nem colidir com o cano de cima.

**Conceito de IA:** Simulação Física / Previsão de Trajetória

| Controle (Humano) | Ação |
|---|---|
| `Espaço` | Pular |
| `ESC` | Voltar ao menu |

```bash
python flappybird.py
```

---

### Sobrevivência — Zumbis e Campos Potenciais
**Arquivo:** `mine.py` | **Interface:** Pygame

O sobrevivente azul precisa coletar o máximo de ouro possível sem ser capturado pelos zumbis. No modo IA, o personagem usa **Campos Potenciais**: o ouro atrai, os zumbis repelem, e as paredes empurram o jogador para o centro da arena.

**Conceito de IA:** Campos Potenciais (Potential Fields)

| Controle (Humano) | Ação |
|---|---|
| `W A S D` ou `Setas` | Mover |
| `ESC` | Voltar ao menu |

```bash
python mine.py
```

---

### Pac-Man — Fuga com Campos Potenciais
**Arquivo:** `pacman.py` | **Interface:** Pygame

O círculo amarelo tenta fugir do fantasma vermelho. No modo IA, o fugitivo usa Campos Potenciais: repulsão do fantasma e das paredes combinadas em um vetor de força resultante que guia o movimento de fuga.

**Conceito de IA:** Campos Potenciais (Fuga)

| Controle (Humano) | Ação |
|---|---|
| `W A S D` ou `Setas` | Mover |
| `1` | Modo Humano |
| `2` | Modo IA |
| `Espaço` | Reiniciar (após game over) |

```bash
python pacman.py
```

---

## Técnicas de IA abordadas

| Técnica | Jogo |
|---|---|
| Árvore de Decisão | Akinator |
| Algoritmo Aleatório | Jogo da Velha (Fácil) |
| Heurística / Regras | Jogo da Velha (Médio) |
| Minimax | Jogo da Velha (Difícil) |
| IA Reativa com Física | Dino |
| Simulação de Trajetória | Flappy Bird |
| Campos Potenciais | Sobrevivência e Pac-Man |

---

## Como rodar

**Requisitos:** Python 3.8+ e Pygame

```bash
pip install pygame
```

Execute qualquer jogo diretamente:

```bash
python akinator.py
python jogodavelha.py
python dino.py
python flappybird.py
python mine.py
python pacman.py
```

---

## Tecnologias

- **Python 3**
- **Pygame** — renderização gráfica e loop de jogo
