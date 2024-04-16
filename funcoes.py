from ast import Return
import random
import os

print("   ____      ")
print("  /    |     ")
print(" |     O     ")
print(" |    /|\    ")
print(" |    / \    ")
print(" |________________________ JOGO DA FORCA______________________")

    # Dicionário de palavras
palavras = {
        '1': ["uva", "gato", "leite", "ceu", "mesa"],
        '2': ["computador", "hamburguer", "sushi", "macarrao", "bebedouro"],
        '3': ["pleonasmo", "paquibaquigrafo", "constelação", "apocalipse"],
          }

resultados_jogadores = []

# Função para sortear uma palavra
def sortear_palavra(categoria):
    return random.choice(palavras[categoria])

# Função para verificar se a letra está na palavra
def letra_na_palavra(palavra, letra):
    return letra in palavra

# Função para mostrar a palavra com as letras acertadas
def mostrar_palavra(palavra, letras_acertadas):
    # Retorna a palavra com espaços entre cada letra
    palavra_com_acertos = " ".join(letra if letra in letras_acertadas else "_" for letra in palavra)
    return palavra_com_acertos

# Função para jogar a rodada
def jogar_rodada(palavra, vidas, jogador_num):    
    letras_acertadas = []
    letras_erradas = []
    saldo_final = 0
    jogador = 0

    # Mostrar a palavra com espaços entre cada letra
    print(f"A palavra tem {len(palavra)} letras: {mostrar_palavra(palavra, letras_acertadas)}")

    while vidas > 0 and "_ " in mostrar_palavra(palavra, letras_acertadas):
        letra = input("\nDigite uma letra: ").lower()

        if letra in letras_acertadas + letras_erradas:
            print("Essa letra já foi utilizada!")
            continue

        if letra_na_palavra(palavra, letra):
            letras_acertadas.append(letra)
            print("\n*****************************************************************************")
            print("\nPARABÉNS!! VOCÊ ACERTOU UMA LETRA!!")
            print(f"\nPalavra: {mostrar_palavra(palavra, letras_acertadas)}")
            print(f"\nVidas: {vidas}")
            print(f"Letras erradas: {letras_erradas}")
            print("\n*****************************************************************************")
        else:
            vidas -= 1
            letras_erradas.append(letra)
            print("\n*****************************************************************************")
            print("\nCONCENTRA QUE VOCÊ AINDA TEM CHANCE!!")
            print(f"\nPalavra: {mostrar_palavra(palavra, letras_acertadas)}")
            print(f"\nVidas: {vidas}")
            print(f"Letras erradas: {letras_erradas}")

            if vidas == 5:
                print("   ____       ")
                print("  /    |      ")
                print(" |     O      ")
                print(" |    /|\     ")
                print(" |      \     ")
                print(" |________________________ JOGO DA FORCA______________________\n")
                print("\n*****************************************************************************")


            if vidas == 4:

              print("   ____       ")
              print("  /    |      ")
              print(" |     O      ")
              print(" |    /|\     ")
              print(" |            ")
              print(" |________________________ JOGO DA FORCA______________________\n\n")
              print("\n*****************************************************************************")


            if vidas == 3:

              print("   ____       ")
              print("  /    |      ")
              print(" |     O      ")
              print(" |    /|      ")
              print(" |            ")
              print(" |________________________ JOGO DA FORCA______________________\n")
              print("\n*****************************************************************************")


            if vidas == 2:

              print("   ____       ")
              print("  /    |      ")
              print(" |     O      ")
              print(" |     |      ")
              print(" |            ")
              print(" |________________________ JOGO DA FORCA______________________\n")
              print("\n*****************************************************************************")

            if vidas == 1:

              print("   ____       ")
              print("  /    |      ")
              print(" |     O      ")
              print(" |            ")
              print(" |            ")
              print(" |________________________ JOGO DA FORCA______________________\n")
              print("\n*****************************************************************************")


            if vidas == 0:

              print("   ____       ")
              print("  /    |      ")
              print(" |    X X     ")
              print(" |     -      ")
              print(" |            ")
              print(" |________________________ JOGO DA FORCA______________________\n")
              print("\n*****************************************************************************")


    if vidas > 0:
        print("Você venceu!")
        print(f"Você acertou {len(letras_acertadas)} letras e ganhou um bonus de 10 por ter acertado a palavra")
        print(f"Saldo final {len(letras_acertadas) + 10}")
        jogador_info = (jogador, saldo_final)  # Aqui estamos criando uma tupla com o jogador e o saldo final
        resultados_jogadores.append(jogador_info) # Aqui estamos adicionando a tupla à lista de resultados


    else:
        print(f"Você perdeu! A palavra era {palavra}")
        print(f"Você acertou {len(letras_acertadas)}")
        jogador_info = (jogador, saldo_final)  # Aqui estamos criando uma tupla com o jogador e o saldo final
        resultados_jogadores.append(jogador_info)  # Aqui estamos adicionando a tupla à lista de resultados


     # Calcular o saldo final da rodada
    saldo_final = len(letras_acertadas) + 10 if "_ " not in mostrar_palavra(palavra, letras_acertadas) else 0
    saldo_final = len(letras_acertadas) * 10 + vidas
    return saldo_final