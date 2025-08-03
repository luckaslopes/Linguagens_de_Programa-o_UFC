
import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 50)
    tentativas = 7
    tentativa_atual = 0

    print("=== Jogo de Adivinhação ===")
    print("Tente adivinhar o número entre 1 e 50.")
    print(f"Você tem {tentativas} tentativas.\n")

    while tentativa_atual < tentativas:
        palpite = input(f"Tentativa {tentativa_atual + 1}: ")

        if not palpite.isdigit():
            print("Por favor, digite um número válido.")
            continue

        palpite = int(palpite)

        if palpite < 1 or palpite > 50:
            print("Número fora do intervalo permitido! Tente entre 1 e 50.")
            continue

        tentativa_atual += 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativa_atual} tentativas.")
            break
        elif palpite < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

    else:
        print(f"Fim de jogo! O número secreto era {numero_secreto}.")

if __name__ == "__main__":
    jogo_adivinhacao()
