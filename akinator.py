import time

# Banco de dados: 26 convocados do Brasil para a Copa do Mundo de 2026
jogadores_2026 = [
    # GOLEIROS
    {
        "nome": "Alisson",
        "clube": "Liverpool",
        "posicao": "goleiro",
        "setor": "defesa",
        "pais_clube": "inglaterra",
        "joga_brasil": "nao",
        "premier_league": "sim",
        "flamengo": "nao",
        "camisa_10": "nao"
    },
    {
        "nome": "Ederson",
        "clube": "Fenerbahçe",
        "posicao": "goleiro",
        "setor": "defesa",
        "pais_clube": "outros",
        "joga_brasil": "nao",
        "premier_league": "nao",
        "flamengo": "nao",
        "camisa_10": "nao"
    },
    {
        "nome": "Weverton",
        "clube": "Grêmio",
        "posicao": "goleiro",
        "setor": "defesa",
        "pais_clube": "brasil",
        "joga_brasil": "sim",
        "premier_league": "nao",
        "flamengo": "nao",
        "camisa_10": "nao"
    },

    # ZAGUEIROS
    {
        "nome": "Bremer",
        "clube": "Juventus",
        "posicao": "zagueiro",
        "setor": "defesa",
        "pais_clube": "outros",
        "joga_brasil": "nao",
        "premier_league": "nao",
        "flamengo": "nao",
        "camisa_10": "nao"
    },
    {
        "nome": "Gabriel Magalhães",
        "clube": "Arsenal",
        "posicao": "zagueiro",
        "setor": "defesa",
        "pais_clube": "inglaterra",
        "joga_brasil": "nao",
        "premier_league": "sim",
        "flamengo": "nao",
        "camisa_10": "nao"
    },
    {
        "nome": "Ibañez",
        "clube": "Al-Ahli",
        "posicao": "zagueiro",
        "setor": "defesa",
        "pais_clube": "outros",
        "joga_brasil": "nao",
        "premier_league": "nao",
        "flamengo": "nao",
        "camisa_10": "nao"
    },
    {
        "nome": "Léo Pereira",
        "clube": "Flamengo",
        "posicao": "zagueiro",
        "setor": "defesa",
        "pais_clube": "brasil",
        "joga_brasil": "sim",
        "premier_league": "nao",
        "flamengo": "sim",
        "camisa_10": "nao"
    },
    {
        "nome": "Marquinhos",
        "clube": "PSG",
        "posicao": "zagueiro",
        "setor": "defesa",
        "pais_clube": "outros",
        "joga_brasil": "nao",
        "premier_league": "nao",
        "flamengo": "nao",
        "camisa_10": "nao"
    },

    # LATERAIS
    {
        "nome": "Danilo",
        "clube": "Flamengo",
        "posicao": "lateral",
        "setor": "defesa",
        "pais_clube": "brasil",
        "joga_brasil": "sim",
        "premier_league": "nao",
        "flamengo": "sim",
        "camisa_10": "nao"
    },
    {
        "nome": "Wesley",
        "clube": "Roma",
        "posicao": "lateral",
        "setor": "defesa",
        "pais_clube": "outros",
        "joga_brasil": "nao",
        "premier_league": "nao",
        "flamengo": "nao",
        "camisa_10": "nao"
    },
    {
        "nome": "Alex Sandro",
        "clube": "Flamengo",
        "posicao": "lateral",
        "setor": "defesa",
        "pais_clube": "brasil",
        "joga_brasil": "sim",
        "premier_league": "nao",
        "flamengo": "sim",
        "camisa_10": "nao"
    },
    {
        "nome": "Douglas Santos",
        "clube": "Zenit",
        "posicao": "lateral",
        "setor": "defesa",
        "pais_clube": "outros",
        "joga_brasil": "nao",
        "premier_league": "nao",
        "flamengo": "nao",
        "camisa_10": "nao"
    },

    # MEIO-CAMPISTAS
    {
        "nome": "Bruno Guimarães",
        "clube": "Newcastle",
        "posicao": "meia",
        "setor": "meio",
        "pais_clube": "inglaterra",
        "joga_brasil": "nao",
        "premier_league": "sim",
        "flamengo": "nao",
        "camisa_10": "nao"
    },
    {
        "nome": "Casemiro",
        "clube": "Manchester United",
        "posicao": "meia",
        "setor": "meio",
        "pais_clube": "inglaterra",
        "joga_brasil": "nao",
        "premier_league": "sim",
        "flamengo": "nao",
        "camisa_10": "nao"
    },
    {
        "nome": "Danilo Santos",
        "clube": "Botafogo",
        "posicao": "meia",
        "setor": "meio",
        "pais_clube": "brasil",
        "joga_brasil": "sim",
        "premier_league": "nao",
        "flamengo": "nao",
        "camisa_10": "nao"
    },
    {
        "nome": "Fabinho",
        "clube": "Al-Ittihad",
        "posicao": "meia",
        "setor": "meio",
        "pais_clube": "outros",
        "joga_brasil": "nao",
        "premier_league": "nao",
        "flamengo": "nao",
        "camisa_10": "nao"
    },
    {
        "nome": "Lucas Paquetá",
        "clube": "Flamengo",
        "posicao": "meia",
        "setor": "meio",
        "pais_clube": "brasil",
        "joga_brasil": "sim",
        "premier_league": "nao",
        "flamengo": "sim",
        "camisa_10": "nao"
    },

    # ATACANTES
    {
        "nome": "Endrick",
        "clube": "Lyon",
        "posicao": "atacante",
        "setor": "ataque",
        "pais_clube": "outros",
        "joga_brasil": "nao",
        "premier_league": "nao",
        "flamengo": "nao",
        "camisa_10": "nao"
    },
    {
        "nome": "Gabriel Martinelli",
        "clube": "Arsenal",
        "posicao": "atacante",
        "setor": "ataque",
        "pais_clube": "inglaterra",
        "joga_brasil": "nao",
        "premier_league": "sim",
        "flamengo": "nao",
        "camisa_10": "nao"
    },
    {
        "nome": "Igor Thiago",
        "clube": "Brentford",
        "posicao": "atacante",
        "setor": "ataque",
        "pais_clube": "inglaterra",
        "joga_brasil": "nao",
        "premier_league": "sim",
        "flamengo": "nao",
        "camisa_10": "nao"
    },
    {
        "nome": "Luiz Henrique",
        "clube": "Zenit",
        "posicao": "atacante",
        "setor": "ataque",
        "pais_clube": "outros",
        "joga_brasil": "nao",
        "premier_league": "nao",
        "flamengo": "nao",
        "camisa_10": "nao"
    },
    {
        "nome": "Matheus Cunha",
        "clube": "Manchester United",
        "posicao": "atacante",
        "setor": "ataque",
        "pais_clube": "inglaterra",
        "joga_brasil": "nao",
        "premier_league": "sim",
        "flamengo": "nao",
        "camisa_10": "nao"
    },
    {
        "nome": "Neymar",
        "clube": "Santos",
        "posicao": "atacante",
        "setor": "ataque",
        "pais_clube": "brasil",
        "joga_brasil": "sim",
        "premier_league": "nao",
        "flamengo": "nao",
        "camisa_10": "sim"
    },
    {
        "nome": "Raphinha",
        "clube": "Barcelona",
        "posicao": "atacante",
        "setor": "ataque",
        "pais_clube": "outros",
        "joga_brasil": "nao",
        "premier_league": "nao",
        "flamengo": "nao",
        "camisa_10": "nao"
    },
    {
        "nome": "Rayan",
        "clube": "Bournemouth",
        "posicao": "atacante",
        "setor": "ataque",
        "pais_clube": "inglaterra",
        "joga_brasil": "nao",
        "premier_league": "sim",
        "flamengo": "nao",
        "camisa_10": "nao"
    },
    {
        "nome": "Vini Jr.",
        "clube": "Real Madrid",
        "posicao": "atacante",
        "setor": "ataque",
        "pais_clube": "outros",
        "joga_brasil": "nao",
        "premier_league": "nao",
        "flamengo": "nao",
        "camisa_10": "nao"
    }
]


perguntas = [
    {
        "texto": "Ele é goleiro?",
        "chave": "posicao",
        "valor": "goleiro"
    },
    {
        "texto": "Ele é zagueiro?",
        "chave": "posicao",
        "valor": "zagueiro"
    },
    {
        "texto": "Ele é lateral?",
        "chave": "posicao",
        "valor": "lateral"
    },
    {
        "texto": "Ele é meio-campista?",
        "chave": "posicao",
        "valor": "meia"
    },
    {
        "texto": "Ele é atacante?",
        "chave": "posicao",
        "valor": "atacante"
    },
    {
        "texto": "Ele joga em um clube do Brasil?",
        "chave": "joga_brasil",
        "valor": "sim"
    },
    {
        "texto": "Ele joga na Premier League, na Inglaterra?",
        "chave": "premier_league",
        "valor": "sim"
    },
    {
        "texto": "Ele joga no Flamengo?",
        "chave": "flamengo",
        "valor": "sim"
    },
    {
        "texto": "Ele joga em um clube da Inglaterra?",
        "chave": "pais_clube",
        "valor": "inglaterra"
    },
    {
        "texto": "Ele joga em um clube fora do Brasil e fora da Inglaterra?",
        "chave": "pais_clube",
        "valor": "outros"
    },
    {
        "texto": "Ele é o Neymar?",
        "chave": "nome",
        "valor": "Neymar"
    },
    {
        "texto": "Ele é o Vini Jr.?",
        "chave": "nome",
        "valor": "Vini Jr."
    },
    {
        "texto": "Ele joga no Arsenal?",
        "chave": "clube",
        "valor": "Arsenal"
    },
    {
        "texto": "Ele joga no Manchester United?",
        "chave": "clube",
        "valor": "Manchester United"
    },
    {
        "texto": "Ele joga no Zenit?",
        "chave": "clube",
        "valor": "Zenit"
    }
]


def perguntar(texto):
    while True:
        resposta = input(f"\n{texto} (sim/nao): ").strip().lower()

        if resposta in ["sim", "s"]:
            return "sim"
        elif resposta in ["nao", "não", "n"]:
            return "nao"
        else:
            print("Responda apenas com 'sim' ou 'nao'.")


def escolher_melhor_pergunta(lista, perguntas_usadas):
    melhor_pergunta = None
    melhor_diferenca = None

    for pergunta in perguntas:
        if pergunta["texto"] in perguntas_usadas:
            continue

        chave = pergunta["chave"]
        valor = pergunta["valor"]

        quantidade_sim = len([j for j in lista if j[chave] == valor])
        quantidade_nao = len(lista) - quantidade_sim

        if quantidade_sim == 0 or quantidade_nao == 0:
            continue

        diferenca = abs(quantidade_sim - quantidade_nao)

        if melhor_diferenca is None or diferenca < melhor_diferenca:
            melhor_diferenca = diferenca
            melhor_pergunta = pergunta

    return melhor_pergunta


def mostrar_jogadores_restantes(lista):
    print("\nAinda pode ser:")
    for jogador in lista:
        print(f"- {jogador['nome']} ({jogador['clube']})")


def jogar_akinator():
    print("=" * 70)
    print("AKINATOR COPA 2026 - SELEÇÃO BRASILEIRA")
    print("=" * 70)
    print("Pense em um dos 26 jogadores convocados pelo Brasil para a Copa de 2026.")
    input("\nPensou? Pressione ENTER para começar...")

    lista = jogadores_2026.copy()
    perguntas_usadas = set()

    while len(lista) > 1:
        pergunta = escolher_melhor_pergunta(lista, perguntas_usadas)

        if pergunta is None:
            break

        perguntas_usadas.add(pergunta["texto"])
        resposta = perguntar(pergunta["texto"])

        chave = pergunta["chave"]
        valor = pergunta["valor"]

        if resposta == "sim":
            lista = [j for j in lista if j[chave] == valor]
        else:
            lista = [j for j in lista if j[chave] != valor]

        if len(lista) == 0:
            break

    print("\nAnalisando suas respostas...")
    time.sleep(1)

    if len(lista) == 1:
        jogador = lista[0]
        print(f"\nAcho que você pensou em: {jogador['nome']} ({jogador['clube']})!")
    elif len(lista) > 1:
        print("\nAinda fiquei em dúvida entre alguns jogadores.")
        mostrar_jogadores_restantes(lista)

        print("\nVou tentar desempatar perguntando diretamente.")

        for jogador in lista:
            resposta = perguntar(f"O jogador é {jogador['nome']} ({jogador['clube']})?")

            if resposta == "sim":
                print(f"\nAgora sim! Você pensou em: {jogador['nome']} ({jogador['clube']})!")
                return

        print("\nEntão provavelmente alguma resposta anterior ficou diferente do jogador escolhido.")
    else:
        print("\nNão encontrei nenhum jogador com esse perfil.")
        print("Provavelmente alguma resposta foi marcada de forma incorreta.")


while True:
    jogar_akinator()

    resposta = perguntar("Quer testar outro jogador?")

    if resposta == "nao":
        print("\nObrigado por jogar!")
        break