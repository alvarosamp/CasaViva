import pygame
import sys
import random

pygame.init()

# Configurações de Tela
WIDTH, HEIGHT = 800, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo do Dino: Humano vs IA Avançada")

# Cores
WHITE = (247, 247, 247)
BLACK = (32, 33, 36)
GRAY = (150, 150, 150)
GREEN_BTN = (22, 163, 74)
BTN_BG = (71, 85, 105)
RED = (239, 68, 68)
BLUE = (37, 99, 235)
BIRD_COLOR = (120, 80, 40)

clock = pygame.time.Clock()

font_sm = pygame.font.SysFont("Arial", 16, bold=True)
font_md = pygame.font.SysFont("Arial", 22, bold=True)
font_lg = pygame.font.SysFont("Arial", 36, bold=True)

# Estados do Jogo
estado_jogo = "MENU"
modo_jogador = "HUMANO"

# Configurações do Dino
CHAO_Y = 320
DINO_X = 100
DINO_W = 40
DINO_H_NORMAL = 40
DINO_H_AGACHADO = 22

dino_y = CHAO_Y
dino_velocity = 0
gravity = 0.6
jump_force = -12
is_jumping = False
is_ducking = False

# Obstáculo
obstaculo = {
    "tipo": "cacto",
    "x": WIDTH + 50,
    "w": 20,
    "h": 45,
    "y": CHAO_Y + DINO_H_NORMAL - 45
}

game_speed = 5.5
pontos = 0

btn_humano = pygame.Rect(WIDTH // 2 - 130, 200, 260, 50)
btn_ia = pygame.Rect(WIDTH // 2 - 130, 280, 260, 50)


def reset_jogo(modo):
    global dino_y, dino_velocity, is_jumping, is_ducking
    global obstaculo, game_speed, pontos, estado_jogo, modo_jogador

    modo_jogador = modo
    estado_jogo = "JOGANDO"

    dino_y = CHAO_Y
    dino_velocity = 0
    is_jumping = False
    is_ducking = False

    game_speed = 5.5
    pontos = 0

    obstaculo = criar_obstaculo()


def criar_obstaculo():
    tipo = random.choice(["cacto", "cacto", "cacto", "passaro"])

    if tipo == "cacto":
        altura = random.choice([35, 45, 55, 65])
        largura = random.choice([20, 25, 30])

        return {
            "tipo": "cacto",
            "x": WIDTH + random.randint(80, 220),
            "w": largura,
            "h": altura,
            "y": CHAO_Y + DINO_H_NORMAL - altura
        }

    else:
        altura_passaro = random.choice([CHAO_Y - 10, CHAO_Y + 10, CHAO_Y + 25])

        return {
            "tipo": "passaro",
            "x": WIDTH + random.randint(120, 260),
            "w": 45,
            "h": 25,
            "y": altura_passaro
        }


def desenhar_menu(mx, my):
    screen.fill(BLACK)

    title = font_lg.render("JOGO DO DINO: HUMANO VS IA", True, WHITE)
    screen.blit(title, title.get_rect(center=(WIDTH // 2, 100)))

    subtitle = font_sm.render(
        "Agora com velocidade crescente, cactos maiores e passarinho.",
        True,
        GRAY
    )
    screen.blit(subtitle, subtitle.get_rect(center=(WIDTH // 2, 150)))

    pygame.draw.rect(
        screen,
        GREEN_BTN if btn_humano.collidepoint(mx, my) else BTN_BG,
        btn_humano,
        border_radius=10
    )

    pygame.draw.rect(
        screen,
        GREEN_BTN if btn_ia.collidepoint(mx, my) else BTN_BG,
        btn_ia,
        border_radius=10
    )

    txt_h = font_md.render("OP 1) Você", True, WHITE)
    txt_i = font_md.render("OP 2) Controlado por IA", True, WHITE)

    screen.blit(txt_h, txt_h.get_rect(center=btn_humano.center))
    screen.blit(txt_i, txt_i.get_rect(center=btn_ia.center))

    comandos = font_sm.render(
        "Humano: ESPAÇO pula | SETA PARA BAIXO agacha | ESC volta ao menu",
        True,
        GRAY
    )
    screen.blit(comandos, comandos.get_rect(center=(WIDTH // 2, HEIGHT - 45)))


def get_dino_rect():
    altura = DINO_H_AGACHADO if is_ducking and not is_jumping else DINO_H_NORMAL
    y = CHAO_Y + DINO_H_NORMAL - altura if not is_jumping else dino_y

    return pygame.Rect(DINO_X, int(y), DINO_W, altura)


def pular():
    global dino_velocity, is_jumping, is_ducking

    if not is_jumping:
        dino_velocity = jump_force
        is_jumping = True
        is_ducking = False


def agachar(ativo):
    global is_ducking

    if not is_jumping:
        is_ducking = ativo
    else:
        is_ducking = False


def atualizar_dino():
    global dino_y, dino_velocity, is_jumping

    dino_velocity += gravity
    dino_y += dino_velocity

    if dino_y >= CHAO_Y:
        dino_y = CHAO_Y
        dino_velocity = 0
        is_jumping = False


def ia_decidir():
    """
    IA avançada:
    - Se for cacto, calcula tempo até colisão e pula.
    - Se for passarinho baixo, agacha.
    - Se for passarinho muito baixo, pode pular/agachar dependendo da altura.
    - Se não houver risco, segue normal.
    """

    distancia = obstaculo["x"] - (DINO_X + DINO_W)

    if distancia <= 0:
        agachar(False)
        return

    tempo_ate_obstaculo = distancia / game_speed

    tempo_ideal_pulo = 24 - min(game_speed, 12)

    if obstaculo["tipo"] == "cacto":
        agachar(False)

        if obstaculo["h"] >= 55:
            tempo_ideal_pulo += 2

        if game_speed < 7:
            tempo_ideal_pulo -= 1

        if tempo_ate_obstaculo < tempo_ideal_pulo:
            pular()

    elif obstaculo["tipo"] == "passaro":
        passaro_base = obstaculo["y"] + obstaculo["h"]
        dino_topo_agachado = CHAO_Y + DINO_H_NORMAL - DINO_H_AGACHADO  # 338

        if tempo_ate_obstaculo < 28:
            if passaro_base < dino_topo_agachado:
                # Pássaro passa por cima do dino abaixado
                agachar(True)
            else:
                # Pássaro está baixo demais, agachar não adianta — pular
                agachar(False)
                if tempo_ate_obstaculo < tempo_ideal_pulo:
                    pular()
        else:
            agachar(False)


def atualizar_obstaculo():
    global obstaculo, pontos, game_speed

    obstaculo["x"] -= game_speed

    if obstaculo["x"] < -obstaculo["w"]:
        pontos += 1
        game_speed += 0.25

        if game_speed > 13:
            game_speed = 13

        obstaculo = criar_obstaculo()


def verificar_colisao():
    dino_rect = get_dino_rect()

    obstaculo_rect = pygame.Rect(
        int(obstaculo["x"]),
        int(obstaculo["y"]),
        obstaculo["w"],
        obstaculo["h"]
    )

    return dino_rect.colliderect(obstaculo_rect)


def desenhar_jogo():
    screen.fill(WHITE)

    pygame.draw.line(
        screen,
        GRAY,
        (0, CHAO_Y + DINO_H_NORMAL),
        (WIDTH, CHAO_Y + DINO_H_NORMAL),
        2
    )

    dino_rect = get_dino_rect()

    obstaculo_rect = pygame.Rect(
        int(obstaculo["x"]),
        int(obstaculo["y"]),
        obstaculo["w"],
        obstaculo["h"]
    )

    if modo_jogador == "IA":
        distancia = obstaculo["x"] - (DINO_X + DINO_W)

        if distancia > 0:
            tempo = distancia / game_speed
        else:
            tempo = 0

        pygame.draw.line(
            screen,
            RED,
            (DINO_X + DINO_W, CHAO_Y + 20),
            (int(obstaculo["x"]), int(obstaculo["y"] + obstaculo["h"] // 2)),
            2
        )

        pygame.draw.circle(
            screen,
            BLUE,
            (int(obstaculo["x"]), int(obstaculo["y"] + obstaculo["h"] // 2)),
            5
        )

        txt_ia = font_sm.render(
            f"IA: obstáculo={obstaculo['tipo']} | tempo={tempo:.1f} frames",
            True,
            BLACK
        )
        screen.blit(txt_ia, (20, 20))

    pygame.draw.rect(screen, BLACK, dino_rect)

    if obstaculo["tipo"] == "cacto":
        pygame.draw.rect(screen, GRAY, obstaculo_rect)

        # Detalhe visual do cacto
        pygame.draw.rect(
            screen,
            GRAY,
            (
                int(obstaculo["x"]) - 8,
                int(obstaculo["y"]) + 12,
                8,
                10
            )
        )
        pygame.draw.rect(
            screen,
            GRAY,
            (
                int(obstaculo["x"]) + obstaculo["w"],
                int(obstaculo["y"]) + 22,
                8,
                10
            )
        )

    else:
        pygame.draw.rect(screen, BIRD_COLOR, obstaculo_rect)

        # Asa do passarinho
        pygame.draw.polygon(
            screen,
            BIRD_COLOR,
            [
                (int(obstaculo["x"]) + 10, int(obstaculo["y"])),
                (int(obstaculo["x"]) + 25, int(obstaculo["y"]) - 15),
                (int(obstaculo["x"]) + 35, int(obstaculo["y"]))
            ]
        )

    pygame.draw.rect(screen, BLACK, (0, HEIGHT - 60, WIDTH, 60))

    txt_p = font_sm.render(
        f"PONTOS: {pontos} | VELOCIDADE: {game_speed:.1f} | MODO: {modo_jogador}",
        True,
        WHITE
    )

    txt_i = font_sm.render(
        "ESPAÇO = pular | SETA BAIXO = agachar | ESC = menu",
        True,
        GRAY
    )

    screen.blit(txt_p, (20, HEIGHT - 50))
    screen.blit(txt_i, (20, HEIGHT - 28))


while True:
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and estado_jogo == "MENU":
            if btn_humano.collidepoint(mx, my):
                reset_jogo("HUMANO")

            elif btn_ia.collidepoint(mx, my):
                reset_jogo("IA")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                estado_jogo = "MENU"

            if estado_jogo == "JOGANDO" and modo_jogador == "HUMANO":
                if event.key == pygame.K_SPACE:
                    pular()

                if event.key == pygame.K_DOWN:
                    agachar(True)

        if event.type == pygame.KEYUP:
            if estado_jogo == "JOGANDO" and modo_jogador == "HUMANO":
                if event.key == pygame.K_DOWN:
                    agachar(False)

    if estado_jogo == "MENU":
        desenhar_menu(mx, my)

    elif estado_jogo == "JOGANDO":
        if modo_jogador == "IA":
            ia_decidir()

        atualizar_dino()
        atualizar_obstaculo()
        desenhar_jogo()

        if verificar_colisao():
            estado_jogo = "MENU"

    pygame.display.update()
    clock.tick(60)