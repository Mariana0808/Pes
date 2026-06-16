# Importa o módulo de números aleatórios
import random

# Pede a escolha do jogador e salva em uma variável
escolha_jogador = input("Diga pedra, papel ou tesoura: ")

# Sorteia um número inteiro entre 1 e 3 (inclusive)
escolhido = random.randint(1, 3)

# Converte o número sorteado em texto (pedra, papel ou tesoura)
if escolhido == 1:
    escolha_maquina = "pedra"
elif escolhido == 2:
    escolha_maquina = "papel"
elif escolhido == 3:
    escolha_maquina = "tesoura"

# Mostra na tela o que a máquina escolheu
print("A maquina escolheu " + escolha_maquina)

# --- Comparação quando o jogador escolhe PEDRA ---
if escolha_jogador == "pedra":
    if escolha_maquina == "papel":
        print("Perde")       # papel ganha de pedra
    elif escolha_maquina == "tesoura":
        print("Ganha")       # pedra ganha de tesoura
    elif escolha_maquina == "pedra":
        print("Empata")

# --- Comparação quando o jogador escolhe PAPEL ---
if escolha_jogador == "papel":
    if escolha_maquina == "tesoura":
        print("Perde")       # tesoura ganha de papel
    elif escolha_maquina == "pedra":
        print("Ganha")       # papel ganha de pedra
    elif escolha_maquina == "papel":
        print("Empata")

# --- Comparação quando o jogador escolhe TESOURA ---
if escolha_jogador == "tesoura":
    if escolha_maquina == "pedra":
        print("Perde")       # pedra ganha de tesoura
    elif escolha_maquina == "papel":
        print("Ganha")       # tesoura ganha de papel
    elif escolha_maquina == "tesoura":
        print("Empata")