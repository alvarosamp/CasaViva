import pygame
import sys
import math
import random

pygame.init()

# Configurações do ecrã
WIDTH, HEIGHT = 700, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("IA estilo Pac-Man: Perseguição Avançada")

# Cores
BLACK = (15, 23, 42)
YELLOW = (234, 179, 8)  # Fugitivo
RED = (239, 68, 68)     # Fantasma IA
WHITE = (255, 255, 255)
BLUE = (59, 130, 246)
OVERLAY = (0, 0, 0, 150) # Fundo escuro do Game Over

clock = pygame.time.Clock()

# Posições iniciais
player_pos = [350, 350]
ghost_pos = [100, 100]

player_speed = 4
ghost_speed = 3

# Modo de jogo: "HUMANO" ou "IA"
mode = "HUMANO"
game_over = False

font = pygame.font.SysFont("Arial", 20, bold=True)
font_large = pygame.font.SysFont("Arial", 40, bold=True)

def reset_positions():
    global player_pos, ghost_pos, game_over
    player_pos = [350, 350]
    # Spawna o fantasma em um canto aleatório para a IA não prever sempre igual
    ghost_pos = random.choice([[100, 100], [600, 100], [100, 450], [600, 450]])
    game_over = False

while True:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = "HUMANO"
                reset_positions()
            if event.key == pygame.K_2:
                mode = "IA"
                reset_positions()
            if event.key == pygame.K_SPACE and game_over:
                reset_positions()

    # Só processa os movimentos se o jogo NÃO tiver terminado
    if not game_over:
        # --- MOVIMENTO DO FUGITIVO (AMARELO) ---
        if mode == "HUMANO":
            # Controlos do Usuário
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:  player_pos[0] -= player_speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]: player_pos[0] += player_speed
            if keys[pygame.K_UP] or keys[pygame.K_w]:    player_pos[1] -= player_speed
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:  player_pos[1] += player_speed
        else:
            # Controlado por IA — Campos Potenciais (repulsão do fantasma + paredes)
            dx = player_pos[0] - ghost_pos[0]
            dy = player_pos[1] - ghost_pos[1]
            distance = math.hypot(dx, dy)

            force_x, force_y = 0.0, 0.0

            # Repulsão do fantasma (mais forte quando mais perto)
            if distance > 0:
                force_x += (dx / distance) * (5000 / (distance ** 1.5 + 1))
                force_y += (dy / distance) * (5000 / (distance ** 1.5 + 1))

            # Repulsão das paredes (empurra para longe das bordas)
            wall_strength = 4000
            px, py = player_pos[0], player_pos[1]
            left_d   = max(px - 30, 1)
            right_d  = max(WIDTH - 30 - px, 1)
            top_d    = max(py - 30, 1)
            bot_d    = max(HEIGHT - 120 - py, 1)

            force_x += wall_strength / (left_d ** 2)
            force_x -= wall_strength / (right_d ** 2)
            force_y += wall_strength / (top_d ** 2)
            force_y -= wall_strength / (bot_d ** 2)

            # Normaliza e aplica a velocidade
            mag = math.hypot(force_x, force_y)
            if mag > 0:
                player_pos[0] += (force_x / mag) * player_speed
                player_pos[1] += (force_y / mag) * player_speed

        # --- LÓGICA DA IA DO FANTASMA (VERMELHO) ---
        if ghost_pos[0] < player_pos[0]: ghost_pos[0] += ghost_speed
        elif ghost_pos[0] > player_pos[0]: ghost_pos[0] -= ghost_speed

        if ghost_pos[1] < player_pos[1]: ghost_pos[1] += ghost_speed
        elif ghost_pos[1] > player_pos[1]: ghost_pos[1] -= ghost_speed

        # Mantém os personagens dentro do cenário
        player_pos[0] = max(30, min(WIDTH - 30, player_pos[0]))
        player_pos[1] = max(30, min(HEIGHT - 120, player_pos[1]))
        ghost_pos[0] = max(30, min(WIDTH - 30, ghost_pos[0]))
        ghost_pos[1] = max(30, min(HEIGHT - 120, ghost_pos[1]))

        # --- VERIFICAÇÃO DE COLISÃO (O Fantasma encontrou o Amarelo?) ---
        dist_colisao = math.hypot(player_pos[0] - ghost_pos[0], player_pos[1] - ghost_pos[1])
        if dist_colisao < 35:  # Raio dos dois círculos combinados
            game_over = True

    # --- DESENHAR NA TELA ---
    # Desenhar as personagens nas posições atuais
    pygame.draw.circle(screen, YELLOW, (int(player_pos[0]), int(player_pos[1])), 20)
    pygame.draw.circle(screen, RED, (int(ghost_pos[0]), int(ghost_pos[1])), 20)

    # Se o fantasma pegou a bolinha amarela, exibe a tela de Game Over
    if game_over:
        # Criando uma superfície semi-transparente para escurecer o fundo
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))
        
        txt_game_over = font_large.render("FANTASMA PEGOU! 👻", True, RED)
        txt_restart = font.render("Aperte ESPAÇO para tentar de novo", True, WHITE)
        
        screen.blit(txt_game_over, (txt_game_over.get_rect(center=(WIDTH//2, HEIGHT//2 - 30))))
        screen.blit(txt_restart, (txt_restart.get_rect(center=(WIDTH//2, HEIGHT//2 + 20))))

    # Painel de interface embaixo (fixo)
    pygame.draw.rect(screen, BLUE, (0, HEIGHT - 80, WIDTH, 80))
    txt_mode = font.render(f"MODO ATUAL: Círculo Amarelo controlado por -> {mode}", True, WHITE)
    txt_instr = font.render("Controles: [ 1 ] VOCÊ JOGA (Setas)  |  [ 2 ] IA JOGA sozinho", True, WHITE)
    
    screen.blit(txt_mode, (20, HEIGHT - 70))
    screen.blit(txt_instr, (20, HEIGHT - 40))

    pygame.display.update()
    clock.tick(60)