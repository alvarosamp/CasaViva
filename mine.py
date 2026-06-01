import pygame
import sys
import random

pygame.init()

# Configurações da Tela
WIDTH, HEIGHT = 800, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("IA de Sobrevivência: Humano vs IA")

# Cores
C_GRAMA = (34, 139, 34)
C_JOGADOR = (30, 144, 255)
C_ZUMBI_VAGO = (0, 100, 0)
C_ZUMBI_ALERTA = (239, 68, 68)
C_ITEM = (255, 215, 0)
WHITE = (255, 255, 255)
BLACK = (15, 23, 42)
GRAY = (51, 65, 85)
GREEN_BTN = (22, 163, 74)
RED = (220, 38, 38)
YELLOW = (250, 204, 21)
BLUE_LIGHT = (147, 197, 253)

clock = pygame.time.Clock()

font_sm = pygame.font.SysFont("Arial", 16, bold=True)
font_md = pygame.font.SysFont("Arial", 22, bold=True)
font_lg = pygame.font.SysFont("Arial", 36, bold=True)

# Estados globais do jogo
estado_jogo = "MENU"
modo_jogador = "HUMANO"

# Configurações dos personagens
player_pos = [WIDTH // 2, (HEIGHT - 70) // 2]
player_speed = 4
pontos = 0

item_pos = [
    random.randint(100, WIDTH - 100),
    random.randint(100, HEIGHT - 180)
]

zumbis = [
    {"pos": [100, 100], "dir": [1, 1], "estado": "VAGANDO"},
    {"pos": [700, 100], "dir": [-1, 1], "estado": "VAGANDO"},
    {"pos": [400, 450], "dir": [0, -1], "estado": "VAGANDO"}
]

RAIO_VISAO = 140
zumbi_speed_vago = 1
zumbi_speed_alerta = 2.3

# Botões do menu
btn_humano = pygame.Rect(WIDTH // 2 - 150, 260, 300, 50)
btn_ia = pygame.Rect(WIDTH // 2 - 150, 340, 300, 50)


def sortear_item():
    return [
        random.randint(100, WIDTH - 100),
        random.randint(100, HEIGHT - 180)
    ]


def reset_jogo(modo):
    global player_pos, pontos, item_pos, zumbis, estado_jogo, modo_jogador

    modo_jogador = modo
    estado_jogo = "JOGANDO"
    pontos = 0

    player_pos = [WIDTH // 2, (HEIGHT - 70) // 2]
    item_pos = sortear_item()

    zumbis = [
        {"pos": [100, 100], "dir": [1, 1], "estado": "VAGANDO"},
        {"pos": [700, 100], "dir": [-1, 1], "estado": "VAGANDO"},
        {"pos": [400, 450], "dir": [0, -1], "estado": "VAGANDO"}
    ]


def limitar_posicao(pos):
    pos[0] = max(20, min(WIDTH - 20, pos[0]))
    pos[1] = max(20, min(HEIGHT - 90, pos[1]))


def desenhar_menu(mx, my):
    screen.fill(BLACK)

    title = font_lg.render("SOBREVIVÊNCIA MINECRAFT & IA", True, WHITE)
    screen.blit(title, title.get_rect(center=(WIDTH // 2, 120)))

    subtitle = font_sm.render(
        "Escolha como o Sobrevivente Azul vai agir na arena:",
        True,
        (148, 163, 184)
    )
    screen.blit(subtitle, subtitle.get_rect(center=(WIDTH // 2, 170)))

    pygame.draw.rect(
        screen,
        GREEN_BTN if btn_humano.collidepoint(mx, my) else GRAY,
        btn_humano,
        border_radius=10
    )

    pygame.draw.rect(
        screen,
        GREEN_BTN if btn_ia.collidepoint(mx, my) else GRAY,
        btn_ia,
        border_radius=10
    )

    txt_h = font_md.render("OP 1) Jogador no Teclado", True, WHITE)
    txt_i = font_md.render("OP 2) Controlado por IA", True, WHITE)

    screen.blit(txt_h, txt_h.get_rect(center=btn_humano.center))
    screen.blit(txt_i, txt_i.get_rect(center=btn_ia.center))

    footer = font_sm.render(
        "Desenvolvido para Aula de Inteligência Artificial",
        True,
        (71, 85, 105)
    )
    screen.blit(footer, footer.get_rect(center=(WIDTH // 2, HEIGHT - 40)))


def mover_jogador_humano():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_pos[0] -= player_speed

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_pos[0] += player_speed

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_pos[1] -= player_speed

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_pos[1] += player_speed


def mover_jogador_ia():
    global player_pos

    # A IA testa várias direções possíveis e escolhe a melhor.
    # Ela considera:
    # - distância até o ouro
    # - distância até os zumbis
    # - risco de entrar no raio de visão
    # - risco de ficar presa nas bordas

    direcoes = [
        pygame.math.Vector2(1, 0),
        pygame.math.Vector2(-1, 0),
        pygame.math.Vector2(0, 1),
        pygame.math.Vector2(0, -1),
        pygame.math.Vector2(1, 1),
        pygame.math.Vector2(1, -1),
        pygame.math.Vector2(-1, 1),
        pygame.math.Vector2(-1, -1),
        pygame.math.Vector2(0, 0)
    ]

    pos_atual = pygame.math.Vector2(player_pos[0], player_pos[1])
    pos_item = pygame.math.Vector2(item_pos[0], item_pos[1])

    melhor_direcao = pygame.math.Vector2(0, 0)
    melhor_pontuacao = -999999999

    for direcao in direcoes:
        if direcao.length() > 0:
            direcao = direcao.normalize()

        nova_pos = pos_atual + direcao * player_speed

        # Simula limites do mapa
        nova_pos.x = max(20, min(WIDTH - 20, nova_pos.x))
        nova_pos.y = max(20, min(HEIGHT - 90, nova_pos.y))

        pontuacao = 0

        # 1) Buscar o ouro
        distancia_ouro = nova_pos.distance_to(pos_item)
        pontuacao -= distancia_ouro * 0.9

        # 2) Analisar perigo dos zumbis
        perigo_total = 0

        for zumbi in zumbis:
            pos_zumbi = pygame.math.Vector2(zumbi["pos"][0], zumbi["pos"][1])
            distancia_zumbi = nova_pos.distance_to(pos_zumbi)

            if distancia_zumbi < 30:
                perigo_total += 10000

            elif distancia_zumbi < 55:
                perigo_total += 5000

            elif distancia_zumbi < RAIO_VISAO:
                perigo_total += (RAIO_VISAO - distancia_zumbi) * 45

            elif distancia_zumbi < RAIO_VISAO + 90:
                perigo_total += (RAIO_VISAO + 90 - distancia_zumbi) * 10

            else:
                pontuacao += distancia_zumbi * 0.05

        pontuacao -= perigo_total

        # 3) Evitar paredes
        margem = 75

        if nova_pos.x < margem:
            pontuacao -= (margem - nova_pos.x) * 7

        if nova_pos.x > WIDTH - margem:
            pontuacao -= (nova_pos.x - (WIDTH - margem)) * 7

        if nova_pos.y < margem:
            pontuacao -= (margem - nova_pos.y) * 7

        if nova_pos.y > HEIGHT - 90 - margem:
            pontuacao -= (nova_pos.y - (HEIGHT - 90 - margem)) * 7

        # 4) Pequena penalização para ficar parado
        if direcao.length() == 0:
            pontuacao -= 30

        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_direcao = direcao

    player_pos[0] += melhor_direcao.x * player_speed
    player_pos[1] += melhor_direcao.y * player_speed


def atualizar_jogador():
    if modo_jogador == "HUMANO":
        mover_jogador_humano()
    else:
        mover_jogador_ia()

    limitar_posicao(player_pos)


def coletar_item():
    global pontos, item_pos

    dist_coleta = pygame.math.Vector2(player_pos).distance_to(pygame.math.Vector2(item_pos))

    if dist_coleta < 25:
        pontos += 1
        item_pos = sortear_item()


def atualizar_zumbis():
    global estado_jogo

    for zumbi in zumbis:
        dx = player_pos[0] - zumbi["pos"][0]
        dy = player_pos[1] - zumbi["pos"][1]
        dist_ate_player = (dx ** 2 + dy ** 2) ** 0.5

        if dist_ate_player < RAIO_VISAO and dist_ate_player > 0:
            zumbi["estado"] = "CAÇANDO"
            zumbi["pos"][0] += (dx / dist_ate_player) * zumbi_speed_alerta
            zumbi["pos"][1] += (dy / dist_ate_player) * zumbi_speed_alerta
        else:
            zumbi["estado"] = "VAGANDO"

            if random.random() < 0.02:
                zumbi["dir"] = [
                    random.choice([-1, 0, 1]),
                    random.choice([-1, 0, 1])
                ]

            zumbi["pos"][0] += zumbi["dir"][0] * zumbi_speed_vago
            zumbi["pos"][1] += zumbi["dir"][1] * zumbi_speed_vago

        limitar_posicao(zumbi["pos"])

        if dist_ate_player < 25:
            estado_jogo = "MENU"


def desenhar_zumbis():
    for zumbi in zumbis:
        if zumbi["estado"] == "CAÇANDO":
            cor_zumbi = C_ZUMBI_ALERTA
            pygame.draw.line(screen, C_ZUMBI_ALERTA, zumbi["pos"], player_pos, 2)
        else:
            cor_zumbi = C_ZUMBI_VAGO
            pygame.draw.circle(
                screen,
                (210, 215, 210),
                (int(zumbi["pos"][0]), int(zumbi["pos"][1])),
                RAIO_VISAO,
                1
            )

        pygame.draw.circle(
            screen,
            cor_zumbi,
            (int(zumbi["pos"][0]), int(zumbi["pos"][1])),
            18
        )


def desenhar_jogo():
    screen.fill(C_GRAMA)

    # Desenha o ouro
    pygame.draw.rect(
        screen,
        C_ITEM,
        (item_pos[0] - 10, item_pos[1] - 10, 20, 20)
    )

    # Desenha zumbis
    desenhar_zumbis()

    # Desenha jogador
    pygame.draw.circle(
        screen,
        C_JOGADOR,
        (int(player_pos[0]), int(player_pos[1])),
        18
    )

    # Painel inferior
    pygame.draw.rect(screen, BLACK, (0, HEIGHT - 70, WIDTH, 70))

    txt_p = font_sm.render(
        f"PONTOS: {pontos}  |  MODO: {modo_jogador}",
        True,
        WHITE
    )

    txt_i = font_sm.render(
        "Aperte [ ESC ] para voltar ao Menu Principal",
        True,
        (148, 163, 184)
    )

    txt_legenda = font_sm.render(
        "Azul = Sobrevivente | Verde = Zumbi vagando | Vermelho = Zumbi caçando | Amarelo = Ouro",
        True,
        BLUE_LIGHT
    )

    screen.blit(txt_p, (20, HEIGHT - 60))
    screen.blit(txt_i, (20, HEIGHT - 40))
    screen.blit(txt_legenda, (20, HEIGHT - 20))


# Loop principal
while True:
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if estado_jogo == "MENU":
                if btn_humano.collidepoint(mx, my):
                    reset_jogo("HUMANO")

                elif btn_ia.collidepoint(mx, my):
                    reset_jogo("IA")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                estado_jogo = "MENU"

    if estado_jogo == "MENU":
        desenhar_menu(mx, my)

    elif estado_jogo == "JOGANDO":
        atualizar_jogador()
        coletar_item()
        atualizar_zumbis()
        desenhar_jogo()

    pygame.display.update()
    clock.tick(60)