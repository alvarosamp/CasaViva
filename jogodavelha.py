"""
Fácil primeiro. Elas vão rir porque a IA toma decisões sem sentido. 
Depois mude para o modo Médio e mostre que ela começou a "prestar atenção" e te bloquear. 
Por fim, coloque no modo Difícil e desafie a sala inteira a tentar ganhar dela (ninguém vai conseguir, pois ela calcula todas as árvores de possibilidades!)

"""
import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações de Janela e Cores
WIDTH, HEIGHT = 450, 550
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Velha - Inteligência Artificial")

# Cores (Paleta moderna e amigável)
BG_COLOR = (240, 244, 248)
LINE_COLOR = (203, 213, 225)
X_COLOR = (59, 130, 246)
O_COLOR = (239, 68, 68)
TEXT_COLOR = (15, 23, 42)
BTN_BG = (34, 197, 94)
BTN_TEXT = (255, 255, 255)
PANEL_BG = (255, 255, 255)

# Fontes
FONT_BOARD = pygame.font.SysFont("Arial", 60, bold=True)
FONT_MENU = pygame.font.SysFont("Arial", 16, bold=True)
FONT_STATUS = pygame.font.SysFont("Arial", 20, bold=True)

# Estado do Jogo
board = [" " for _ in range(9)]
current_player = "X"
game_mode = "MENU"  # MENU, FACIL, MEDIO, DIFICIL, 1VS1
winner = None
game_over = False

# Coordenadas dos Botões do Menu Principal
buttons = {
    "FACIL": pygame.Rect(30, 480, 80, 40),
    "MEDIO": pygame.Rect(120, 480, 80, 40),
    "DIFICIL": pygame.Rect(210, 480, 80, 40),
    "1VS1": pygame.Rect(300, 480, 110, 40)
}

def check_winner(b):
    win_configs = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for config in win_configs:
        if b[config[0]] == b[config[1]] == b[config[2]] != " ":
            return b[config[0]]
    if " " not in b:
        return "EMPATE"
    return None

def get_empty_positions(b):
    return [i for i, val in enumerate(b) if val == " "]

# --- ESTRATÉGIAS DE IA ---

def ia_facil():
    # Escolha 100% aleatória
    empty = get_empty_positions(board)
    return random.choice(empty) if empty else None

def ia_medio():
    empty = get_empty_positions(board)
    if not empty:
        return None
        
    # 1. Se a IA puder ganhar na próxima jogada, ela joga lá
    for pos in empty:
        board_copy = list(board)
        board_copy[pos] = "O"
        if check_winner(board_copy) == "O":
            return pos
            
    # 2. Se o jogador puder ganhar na próxima jogada, ela bloqueia
    for pos in empty:
        board_copy = list(board)
        board_copy[pos] = "X"
        if check_winner(board_copy) == "X":
            return pos
            
    # 3. Caso contrário, joga no centro se livre, ou aleatório
    if 4 in empty:
        return 4
    return random.choice(empty)

def minimax(board_state, depth, is_maximizing):
    res = check_winner(board_state)
    if res == "O": return 10 - depth
    if res == "X": return depth - 10
    if res == "EMPATE": return 0
    
    empty = [i for i, val in enumerate(board_state) if val == " "]
    
    if is_maximizing:
        best_score = -float('inf')
        for pos in empty:
            board_state[pos] = "O"
            score = minimax(board_state, depth + 1, False)
            board_state[pos] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for pos in empty:
            board_state[pos] = "X"
            score = minimax(board_state, depth + 1, True)
            board_state[pos] = " "
            best_score = min(score, best_score)
        return best_score

def ia_dificil():
    empty = get_empty_positions(board)
    if not empty:
        return None
    best_score = -float('inf')
    best_move = None
    for pos in empty:
        board[pos] = "O"
        score = minimax(board, 0, False)
        board[pos] = " "
        if score > best_score:
            best_score = score
            best_move = pos
    return best_move

def reset_game(mode=None):
    global board, current_player, winner, game_over, game_mode
    board = [" " for _ in range(9)]
    current_player = "X"
    winner = None
    game_over = False
    if mode:
        game_mode = mode

def draw_objects():
    SCREEN.fill(BG_COLOR)
    
    # Desenha o painel do tabuleiro
    pygame.draw.rect(SCREEN, PANEL_BG, (30, 30, 390, 390), border_radius=15)
    
    # Desenha as linhas do tabuleiro
    # Horizontais
    pygame.draw.line(SCREEN, LINE_COLOR, (160, 30), (160, 420), 5)
    pygame.draw.line(SCREEN, LINE_COLOR, (290, 30), (290, 420), 5)
    # Verticais
    pygame.draw.line(SCREEN, LINE_COLOR, (30, 160), (420, 160), 5)
    pygame.draw.line(SCREEN, LINE_COLOR, (30, 290), (420, 290), 5)
    
    # Desenha os X e O
    for i in range(9):
        row = i // 3
        col = i % 3
        x = 30 + col * 130 + 65
        y = 30 + row * 130 + 65
        
        if board[i] == "X":
            text = FONT_BOARD.render("X", True, X_COLOR)
            text_rect = text.get_rect(center=(x, y))
            SCREEN.blit(text, text_rect)
        elif board[i] == "O":
            text = FONT_BOARD.render("O", True, O_COLOR)
            text_rect = text.get_rect(center=(x, y))
            SCREEN.blit(text, text_rect)

    # Desenha os botões de menu
    for mode, rect in buttons.items():
        # Destaca o modo ativo
        color = (15, 118, 110) if game_mode == mode else BTN_BG
        pygame.draw.rect(SCREEN, color, rect, border_radius=8)
        lbl = FONT_MENU.render(mode, True, BTN_TEXT)
        lbl_rect = lbl.get_rect(center=rect.center)
        SCREEN.blit(lbl, lbl_rect)

    # Desenha a barra de status
    if game_over:
        if winner == "EMPATE":
            status_text = "Fim de Jogo: Deu Velha! 🤝"
        else:
            status_text = f"Fim de Jogo: O jogador '{winner}' venceu!"
    else:
        if game_mode == "MENU":
            status_text = "Escolha um modo de jogo abaixo para começar!"
        elif game_mode == "1VS1":
            status_text = f"Modo 1 vs 1 - Vez do '{current_player}'"
        else:
            status_text = f"Contra IA ({game_mode}) - Sua vez!" if current_player == "X" else "IA pensando..."

    status_lbl = FONT_STATUS.render(status_text, True, TEXT_COLOR)
    SCREEN.blit(status_lbl, (30, 440))

# Loop Principal do Jogo
reset_game("MENU")
while True:
    draw_objects()
    pygame.display.update()
    
    # Turno da IA
    if not game_over and game_mode != "MENU" and game_mode != "1VS1" and current_player == "O":
        pygame.time.delay(500) # Pequena pausa para parecer que está pensando
        if game_mode == "FACIL":
            move = ia_facil()
        elif game_mode == "MEDIO":
            move = ia_medio()
        elif game_mode == "DIFICIL":
            move = ia_dificil()
            
        if move is not None:
            board[move] = "O"
            winner = check_winner(board)
            if winner:
                game_over = True
            else:
                current_player = "X"
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            # Verificação do clique nos botões de Modo
            clicked_mode = None
            for mode, rect in buttons.items():
                if rect.collidepoint(mx, my):
                    clicked_mode = mode
                    break
            
            if clicked_mode:
                reset_game(clicked_mode)
                continue
                
            # Clique no Tabuleiro
            if not game_over and game_mode != "MENU":
                # Verifica se o clique foi dentro da área do tabuleiro
                if 30 <= mx <= 420 and 30 <= my <= 420:
                    col = (mx - 30) // 130
                    row = (my - 30) // 130
                    index = row * 3 + col
                    
                    if board[index] == " ":
                        board[index] = current_player
                        winner = check_winner(board)
                        if winner:
                            game_over = True
                        else:
                            # Alterna jogador
                            if game_mode == "1VS1":
                                current_player = "O" if current_player == "X" else "X"
                            else:
                                current_player = "O" # Passa para IA