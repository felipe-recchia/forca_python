from ast import Return
import random
import os
import pickle

print("   ____      ")
print("  /    |     ")
print(" |     O     ")
print(" |    /|\    ")
print(" |    / \    ")
print(" |________________________ JOGO DA FORCA______________________")

    # Dicionário de palavras
palavras = {
        '1': ["uva", "paz", "ovo", "ceu", "mae"],
        '2': ["computador", "hamburguer", "internauta", "hierarquia", "conjuntura"],
        '3': ["compatibilidade", "paquibaquigrafo", "conscientizacao", "impermeabilizar"],
          }

resultados_jogadores = []

def iniciar_novo_jogo():
    # Código para iniciar um novo jogo
    pass

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
    jogador = jogador_num

    # Mostrar a palavra com espaços entre cada letra
    print(f"A palavra tem {len(palavra)} letras: {mostrar_palavra(palavra, letras_acertadas)}")

    while vidas > 0 and "_" in mostrar_palavra(palavra, letras_acertadas):
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


    # Verificar a condição de vitória
    if vidas > 0:
        print("Você venceu!")
        print(f"Você acertou {len(letras_acertadas)} letras e ganhou um bônus de 10 por ter acertado a palavra")
        print(f"Saldo final {len(letras_acertadas) + 10}")
        saldo_final = len(letras_acertadas) * 10 + vidas
        jogador_info = (jogador, saldo_final)
        resultados_jogadores.append(jogador_info)
    else:
        print(f"Você perdeu! A palavra era {palavra}")
        print(f"Você acertou {len(letras_acertadas)}")
        saldo_final = len(letras_acertadas) * 10 
        jogador_info = (jogador, saldo_final)
        resultados_jogadores.append(jogador_info)
    
    return saldo_final

def salvar_estado_jogo(palavra, letras_acertadas, vidas, jogador_num, saldo_final):
    estado_jogo = {
        "palavra": palavra,
        "letras_acertadas": letras_acertadas,
        "vidas": vidas,
        "jogador_num": jogador_num,
        "saldo_final": saldo_final
       
    }
    with open("estado_jogo.pkl", "wb") as f:
        pickle.dump(estado_jogo, f)

def carregar_estado_jogo():
   try:
        print("Tentando carregar o estado do jogo...")
        with open("estado_jogo.pkl", "rb") as f:
            estado_jogo = pickle.load(f)
        print("Estado do jogo carregado com sucesso!")
        return estado_jogo
   except FileNotFoundError:
        print("Arquivo de estado do jogo não encontrado.")
        return None
   except Exception as e:
        print(f"Erro ao carregar o estado do jogo: {e}")
        return None