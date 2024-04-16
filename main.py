from funcoes import *

def iniciar_jogo():
    # Definir o nivel de dificuldade
    categoria = (input("\nEscolha o nível de dificuldade \n\nFácil   [1] \nMédio   [2] \nDifícil [3]:\n\n"))

    # Definir quantidade de jogadores
    numero_jogadores = int(input("Digite a quantidade de jogadores: "))

    # Definir quantidade de rodadas
    numero_rodadas = int(input("Digite a quantidade de rodadas: "))

    resultados_jogadores = []

    # Loop para jogar com cada jogador
    for jogador_num in range(1, numero_jogadores + 1):
        jogador = []
        print(f"\nJogador {jogador_num}:")
        saldo_final_total=0

        for rodada in range(1, numero_rodadas + 1):
            print(f"Rodada {rodada}:")

            # Selecionar categoria e palavra
            palavra = sortear_palavra(categoria)
           
            # Jogar a rodada
            vidas = 6
            saldo_final = jogar_rodada(palavra, vidas, jogador_num)
            saldo_final_total += saldo_final

        print("- " * 20)

        # Adiciona o número do jogador à lista de resultados
        jogador.append(jogador_num)

        resultados_jogadores.append((jogador_num, saldo_final_total))

    # Classificar os resultados por saldo final
    resultados_jogadores.sort(key=lambda x: x[1], reverse=True)

    # Imprimir o ranking dos jogadores
    print("\nRanking dos Jogadores:")
    if resultados_jogadores:
      for i, (jogador, saldo_final) in enumerate(resultados_jogadores, start=1):
        print(f"{i}. Jogador {jogador}: Saldo Final = {saldo_final}")
    else:
      print("Nenhum jogador no ranking.")

# Executa o jogo
if __name__ == "__main__":
    iniciar_jogo()